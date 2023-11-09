from __future__ import annotations

import collections.abc
import datetime
import enum
import functools
import weakref
from typing import TYPE_CHECKING, Any, List, Mapping, Optional, Protocol, Sequence, TypeVar, Union

import pyarrow as pa
from typing_extensions import Self, TypeGuard

from chalk.features._encoding.converter import pyarrow_to_polars
from chalk.features.feature_field import Feature
from chalk.features.feature_wrapper import FeatureWrapper, unwrap_feature
from chalk.features.filter import Filter, TimeDelta, _get_filter_now
from chalk.utils.collections import ensure_tuple

if TYPE_CHECKING:
    import polars as pl


class ParsedExpr(Protocol):
    def __eq__(self, __value: Any, /) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        ...

    def __ne__(self, __value: Any, /) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        ...

    def __gt__(self, __value: Any, /) -> Self:
        ...

    def __lt__(self, __value: Any, /) -> Self:
        ...

    def __le__(self, __value: Any, /) -> Self:
        ...

    def __ge__(self, __value: Any, /) -> Self:
        ...

    def __invert__(self) -> Self:
        ...

    def __add__(self, __value: Any, /) -> Self:
        ...

    def __sub__(self, __value: Any, /) -> Self:
        ...

    def __and__(self, __value: Any, /) -> Self:
        ...

    def __or__(self, __value: Any, /) -> Self:
        ...


class _TableProtocol(Protocol):
    """Protocol describing a PyArrow table. This protocol contains only the methods used by the FilterConverter,
    so it need not be an actual PyArrow table."""

    def column(self, name: str, /) -> Union[pa.Array, pa.ChunkedArray]:
        ...

    def __len__(self) -> int:
        ...


class PyArrowParsedExpr(ParsedExpr):
    def __init__(
        self, col: Union[pa.Array, pa.ChunkedArray, pa.Scalar], table: weakref.ReferenceType[_TableProtocol] | None
    ):
        self.col = col
        if isinstance(self.col, (pa.Array, pa.ChunkedArray)):
            assert table is not None, "If an array is given, then the table binding must be provided"
        else:
            assert isinstance(self.col, pa.Scalar)
        self.table = table

    def _get_equivalent_table_reference(self, other: PyArrowParsedExpr, /):
        if self.table is not None:
            x_deref = self.table()
            if x_deref is None:
                raise ValueError("Table went out of scope; this expression will be invalid")
        else:
            x_deref = None
        if other.table is not None:
            y_deref = other.table()
            if y_deref is None:
                raise ValueError("Table went out of scope; this expression will be invalid")
        else:
            y_deref = None
        if x_deref is not None and y_deref is not None and x_deref is not y_deref:
            raise ValueError("Tables are not equivalent")
        return self.table or other.table

    def __eq__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(pa.compute.equal(self.col, __value.col), self._get_equivalent_table_reference(__value))

    def __ne__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.not_equal(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __gt__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.greater(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __lt__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(pa.compute.less(self.col, __value.col), self._get_equivalent_table_reference(__value))

    def __le__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.less_equal(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __ge__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.greater_equal(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __invert__(self) -> Self:
        return PyArrowParsedExpr(pa.compute.invert(self.col), self.table)

    def __add__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.add_checked(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __sub__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(
            pa.compute.subtract_checked(self.col, __value.col), self._get_equivalent_table_reference(__value)
        )

    def __and__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(pa.compute.and_(self.col, __value.col), self._get_equivalent_table_reference(__value))

    def __or__(self, __value: object, /) -> Self:
        if not isinstance(__value, PyArrowParsedExpr):
            raise TypeError("A PyArrowParsedExpr can only be compared to a PyArrowParsedExpr")
        return PyArrowParsedExpr(pa.compute.or_(self.col, __value.col), self._get_equivalent_table_reference(__value))


TExpr = TypeVar("TExpr", bound=ParsedExpr)


class FilterConverter(Protocol[TExpr]):
    """
    Converts a Filter expression tree into a polars or pyarrow expression
    that can be used to filter tables of the corresponding type.
    """

    def _is_expr(self, o: Any) -> TypeGuard[TExpr]:
        """Need this for isinstance() checks, TypeVar is insufficient :-("""
        ...

    def col(self, name: str) -> TExpr:
        """Expression for selecting a column by the given name"""
        ...

    def lit(self, value: Any, dtype: pa.DataType) -> TExpr:
        """Expression for a literal value"""
        ...

    def is_null(self, expr: TExpr) -> TExpr:
        """Expression for checking null"""
        ...

    def is_not_null(self, expr: TExpr) -> TExpr:
        """Should be equivalent to `not is_null(expr)`."""
        ...

    def if_else(self, cond: TExpr, true_case: TExpr, false_case: TExpr) -> TExpr:
        """For every row where ``cond`` is true, return the ``true_case``. Otherwise, return ``false_case``."""
        ...

    def fill_null(self, expr: TExpr, fill_with: TExpr) -> TExpr:
        return self.if_else(self.is_null(expr), fill_with, expr)

    def _expr_is_in_sequence_lit(self, expr: TExpr, values: Sequence[TExpr], dtype: pa.DataType) -> TExpr:
        """
        Returns an expression that checks whether `expr` is in a sequence of literal values.
        i.e. analogous to `lambda x: expr(x) in values`
        """
        # Using expr == values[0] OR expr == values[2] OR expr == values[3] so we can do our fuzzy eq_missing logic
        exprs = [self._eq_missing(expr, x, dtype) for x in values]
        if len(exprs) == 0:
            return self.lit(False, pa.bool_())
        return functools.reduce(lambda a, b: a | b, exprs)

    def convert_filters(
        self,
        filters: Sequence[Filter],
        df_schema: Mapping[str, pa.DataType],
        timestamp_feature: Optional[Feature] = None,
        now: Optional[Union[datetime.datetime, TExpr]] = None,
        now_col_name: Optional[str] = None,
    ) -> Optional[TExpr]:
        if len(filters) == 0:
            return None
        parsed_filters = [
            self._convert_filter_to_expr(f, df_schema, timestamp_feature, now, now_col_name) for f in filters
        ]
        return functools.reduce(lambda a, b: a & b, parsed_filters)

    def _eq_missing(self, lhs: TExpr, rhs: TExpr, dtype: pa.DataType) -> TExpr:
        # If either side is a struct, then recursively do eq_missing on each struct member
        if pa.types.is_struct(dtype):
            assert isinstance(dtype, pa.StructType)
            sub_exprs: List[TExpr] = []
            sa = self._get_struct_adapter(dtype)
            for f in dtype:
                lhs_expr, lhs_dtype = sa.get_expr_for_field(lhs, f.name)
                rhs_expr, rhs_dtype = sa.get_expr_for_field(rhs, f.name)
                if lhs_dtype != rhs_dtype:
                    raise TypeError(
                        f"Struct field '{f.name}' has a different lhs dtype ({lhs_dtype}) than the RHS dtype ({rhs_dtype})"
                    )
                sub_exprs.append(self._eq_missing(lhs_expr, rhs_expr, lhs_dtype))
            if len(sub_exprs) == 0:
                sub_ans = self.lit(True, pa.bool_())
            else:
                sub_ans = functools.reduce(lambda a, b: a & b, sub_exprs)
        else:
            # FIXME: It is too hard to do eq_missing for sub elements of variable size lists. Probably need to do some sort of join / aggregation
            sub_ans = lhs == rhs
        return self.if_else(
            self.is_null(lhs) == self.is_null(rhs),
            self.fill_null(  # If both sides have the same nullability, return the sub answer, coalescing null values to true (b/c we want null==null)
                sub_ans, self.lit(True, pa.bool_())
            ),
            self.lit(  # If both sides have different nullability, then return False, because Null != (anything other than null)
                False, pa.bool_()
            ),
        )

    def _convert_filter_to_expr(
        self,
        f: Filter,
        df_schema: Mapping[str, pa.DataType],
        timestamp_feature: Optional[Feature] = None,
        now: Optional[Union[datetime.datetime, TExpr]] = None,
        now_col_name: Optional[str] = None,
    ) -> TExpr:
        # Passing `now` in explicitly instead of using datetime.datetime.now() so that multiple filters
        # relying on relative timestamps (e.g. before, after) will have the same "now" time.
        def _convert_sub_filter(sub_filter: Filter, side_name: str):
            assert isinstance(sub_filter, Filter), f"{side_name} must be a filter"
            return self._convert_filter_to_expr(sub_filter, df_schema, timestamp_feature, now, now_col_name)

        if f.operation == "not" or f.operation == "~":
            assert isinstance(f.lhs, Filter)
            assert f.rhs is None, "not has just one side"
            return ~_convert_sub_filter(f.lhs, "lhs")
        elif f.operation == "and" or f.operation == "&":
            return _convert_sub_filter(f.lhs, "lhs") & _convert_sub_filter(f.rhs, "rhs")
        elif f.operation == "or" or f.operation == "|":
            return _convert_sub_filter(f.lhs, "lhs") | _convert_sub_filter(f.rhs, "rhs")

        lhs = self._parse_feature_or_value(f.lhs, timestamp_feature, now, now_col_name)
        rhs = self._parse_feature_or_value(f.rhs, timestamp_feature, now, now_col_name)

        lhs_converter = None
        dtype = None
        if isinstance(lhs, Feature):
            lhs_converter = lhs.converter
            col_name = str(lhs)
            if col_name not in df_schema:
                raise KeyError(f"Feature {col_name} not in DataFrame with columns [{', '.join(df_schema.keys())}]")
            lhs = self.col(col_name)
            dtype = lhs_converter.pyarrow_dtype

        rhs_converter = None
        if isinstance(rhs, Feature):
            rhs_converter = rhs.converter
            col_name = str(rhs)
            if col_name not in df_schema:
                raise KeyError(f"Feature {col_name} not in DataFrame with columns [{', '.join(df_schema.keys())}]")
            rhs = self.col(col_name)
            dtype = rhs_converter.pyarrow_dtype
        assert dtype is not None, "One side must be an expression"

        if lhs_converter is None:
            # LHS is literal. Encode it into the rhs_dtype
            assert rhs_converter is not None, "One side of the filter must be an expression"
            if not self._is_expr(lhs):
                lhs = self.lit(rhs_converter.from_rich_to_primitive(lhs), rhs_converter.pyarrow_dtype)
        if rhs_converter is None:
            # RHS is literal. Encode it into the lhs_dtype
            assert lhs_converter is not None, "One side of the filter must be an expression"
            if not self._is_expr(rhs):
                if f.operation in ("in", "not in"):
                    assert isinstance(rhs, collections.abc.Iterable)
                    rhs = [self.lit(lhs_converter.from_rich_to_primitive(x), lhs_converter.pyarrow_dtype) for x in rhs]
                else:
                    rhs = self.lit(lhs_converter.from_rich_to_primitive(rhs), lhs_converter.pyarrow_dtype)

        if f.operation in ("in", "not in"):
            assert lhs_converter is not None
            assert self._is_expr(lhs)
            assert isinstance(rhs, collections.abc.Iterable)
            ret = self._expr_is_in_sequence_lit(lhs, rhs, lhs_converter.pyarrow_dtype)
            if f.operation == "not in":
                ret = ~ret
        elif f.operation == "==" or f.operation == "!=":
            if lhs_converter is None or rhs_converter is None:
                # If comparing against a literal value, then use eq_missing
                assert self._is_expr(rhs), "The rhs must be an expression if doing equality"
                ret = self._eq_missing(lhs, rhs, dtype)
            else:
                # If both are not None, then do a normal eq
                ret = lhs == rhs
            if f.operation == "!=":
                # Invert it
                ret = ~ret
        elif f.operation == ">=":
            ret = lhs >= rhs
        elif f.operation == ">":
            ret = lhs > rhs
        elif f.operation == "<":
            ret = lhs < rhs
        elif f.operation == "<=":
            ret = lhs <= rhs
        else:
            raise ValueError(f'Unknown operation "{f.operation}"')
        assert self._is_expr(ret)
        return ret

    def _parse_feature_or_value(
        self,
        f: Union[Feature, Any],
        timestamp_feature: Optional[Feature],
        now: Optional[Union[datetime.datetime, TExpr]],
        now_column_name: Optional[str],
    ):
        """Parse a feature or value into the correct type that can be used for filtering."""
        f = self._feature_type_or_value(f)
        f = self._maybe_convert_timedelta_to_timestamp(f, now, now_column_name)
        f = self._maybe_replace_timestamp_feature(f, timestamp_feature)
        if isinstance(f, enum.Enum):
            f = f.value
        return f

    def _feature_type_or_value(self, e: Union[Feature, FeatureWrapper, Any]) -> Union[Feature, Any]:
        if isinstance(e, FeatureWrapper):
            e = unwrap_feature(e)
        return e

    def _maybe_convert_timedelta_to_timestamp(
        self,
        f: Union[TimeDelta, datetime.timedelta, Any],
        now: Optional[Union[datetime.datetime, TExpr]],
        now_column_name: Optional[str] = None,
    ) -> Union[TExpr, datetime.datetime, Any]:
        """Convert timedeltas relative to ``now`` into absolute datetimes."""
        if now is not None and now_column_name is not None:
            raise ValueError(
                (
                    "Can't specify both now and now_column_name -- one or the other must be used as a point of reference for "
                    "the time delta"
                )
            )
        if isinstance(f, TimeDelta):
            f = f.to_std()
        if isinstance(f, datetime.timedelta):
            if now is None and now_column_name is None:
                raise ValueError(
                    (
                        "The filter contains a relative timestamp. The current datetime or current date column "
                        "must be provided to evaluate this filter."
                    )
                )
            if now_column_name is not None:
                # creates a polars/pyarrow expression∂ that evaluates to dates that are within the timedelta specified by `f`
                return self.col(now_column_name) + self.lit(f, pa.duration("us"))
            assert now is not None
            if not self._is_expr(now):
                now = self.lit(now, pa.timestamp("us", "UTC"))
            return now + self.lit(f, pa.duration("us"))

        return f

    def _maybe_replace_timestamp_feature(
        self, f: Union[Feature, Any], observed_at_feature: Optional[Feature]
    ) -> Feature:
        """Replace the ``CHALK_TS`` pseudo-feature with the actual timestamp column."""
        if not isinstance(f, Feature) or f.fqn != "__chalk__.CHALK_TS":
            return f
        if observed_at_feature is not None:
            return observed_at_feature
        raise ValueError("No Timestamp Feature Found")

    def _get_struct_adapter(self, dtype: pa.StructType) -> StructAdapter[TExpr]:
        ...


class PolarsFilterConverter(FilterConverter["pl.Expr"]):
    def _is_expr(self, o: Any) -> TypeGuard[pl.Expr]:
        import polars as pl

        return isinstance(o, pl.Expr)

    def col(self, name: str) -> pl.Expr:
        import polars as pl

        return pl.col(name)

    def lit(self, value: Any, dtype: pa.DataType) -> pl.Expr:
        import polars as pl

        if pa.types.is_struct(dtype):
            # Polars cannot handle structs directly.
            # Instead, we will convert each field, and wrap it in a pl.struct
            assert isinstance(dtype, pa.StructType)
            sub_fields = []
            for f in dtype:
                name = f.name
                try:
                    val = value[name]
                except KeyError:
                    val = getattr(value, name)
                except AttributeError:
                    raise ValueError(f"Literal value has no attribute or key for field '{name}'")
                sub_fields.append(self.lit(val, f.type).alias(name))
            return pl.struct(sub_fields)

        if pa.types.is_list(dtype) or pa.types.is_large_list(dtype) or pa.types.is_fixed_size_list(dtype):
            # If it's a list, then we will convert each value by hand, and return a polars literal of these values
            assert isinstance(dtype, (pa.ListType, pa.LargeListType, pa.FixedSizeListType))
            return pl.lit([self.lit(x, dtype.value_type) for x in value])

        pl_dtype = pyarrow_to_polars(dtype)

        if (
            isinstance(value, datetime.datetime)
            and value.tzinfo is not None
            and isinstance(pl_dtype, pl.Datetime)
            and pl_dtype.time_zone is not None
        ):
            # If given a datetype with a timezone, and we have a target timezone on the datetime type,
            # we will first interpret the datetime in polars with the provided time zone, and then convert it to the desired time zone
            # Polars does not allow literal datetimes with a timezone to be directly interpreted as a datetime with time zone
            return pl.lit(value, pl.Datetime(pl_dtype.time_unit)).dt.convert_time_zone(pl_dtype.time_zone)

        return pl.lit(value, dtype=pl_dtype)

    def is_null(self, expr: pl.Expr) -> pl.Expr:
        return expr.is_null()

    def is_not_null(self, expr: pl.Expr) -> pl.Expr:
        return expr.is_not_null()

    def if_else(self, cond: pl.Expr, true_case: pl.Expr, false_case: pl.Expr) -> pl.Expr:
        import polars as pl

        return pl.when(cond).then(true_case).otherwise(false_case)

    def _get_struct_adapter(self, dtype: pa.StructType) -> StructAdapter[pl.Expr]:
        return _PolarsStructAdapter(dtype)


class PyArrowFilterConverter(FilterConverter[ParsedExpr]):
    def __init__(self, tbl: Union[_TableProtocol, weakref.ReferenceType[_TableProtocol]]):
        if not isinstance(tbl, weakref.ReferenceType):
            tbl = weakref.ref(tbl)
        self._table = tbl

    def _is_expr(self, o: Any) -> TypeGuard[PyArrowParsedExpr]:
        return isinstance(o, PyArrowParsedExpr)

    def _validate_table_is_equivalent(self, other: PyArrowParsedExpr, /):
        """Validate that the table in the expression matches the table in the filter converter"""
        x_deref = self._table()
        if x_deref is None:
            raise ValueError("Table went out of scope; this expression will be invalid")
        if other.table is not None:
            y_deref = other.table()
            if y_deref is None:
                raise ValueError("Table went out of scope; this expression will be invalid")
        else:
            y_deref = None
        if y_deref is not None and x_deref is not y_deref:
            raise ValueError("Tables are not equivalent")

    def col(self, name: str) -> ParsedExpr:
        table = self._table()
        if table is None:
            raise RuntimeError("The underlying table went out of scope. The filter will be invalid.")
        return PyArrowParsedExpr(table.column(name), self._table)

    def lit(self, value: Any, dtype: pa.DataType) -> ParsedExpr:
        return PyArrowParsedExpr(pa.scalar(value, dtype), None)

    def is_null(self, expr: ParsedExpr) -> ParsedExpr:
        if not isinstance(expr, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression; got {type(expr)}")
        if isinstance(expr.col, pa.Scalar):
            is_null = pa.scalar(not expr.col.is_valid, pa.bool_())
        else:
            is_null = expr.col.is_null()
            self._validate_table_is_equivalent(expr)
        return PyArrowParsedExpr(is_null, self._table)

    def is_not_null(self, expr: ParsedExpr) -> ParsedExpr:
        if not isinstance(expr, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression; got {type(expr)}")
        if isinstance(expr.col, pa.Scalar):
            is_not_null = pa.scalar(expr.col.is_valid, pa.bool_())
        else:
            is_not_null = expr.col.is_valid()
            self._validate_table_is_equivalent(expr)
        return PyArrowParsedExpr(is_not_null, self._table)

    def if_else(self, cond: ParsedExpr, true_case: ParsedExpr, false_case: ParsedExpr):
        if not isinstance(cond, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression for the condition; got {type(cond)}")
        self._validate_table_is_equivalent(cond)
        if not isinstance(true_case, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression for the true case; got {type(true_case)}")
        self._validate_table_is_equivalent(true_case)
        if not isinstance(false_case, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression for the false case; got {type(false_case)}")
        self._validate_table_is_equivalent(false_case)
        return PyArrowParsedExpr(
            pa.compute.if_else(cond.col, true_case.col, false_case.col),
            self._table,
        )

    def _get_struct_adapter(self, dtype: pa.StructType) -> StructAdapter[ParsedExpr]:
        return _PyArrowStructAdapter(dtype)

    def convert_filters(
        self,
        filters: Sequence[Filter],
        df_schema: Mapping[str, pa.DataType],
        timestamp_feature: Optional[Feature] = None,
        now: Optional[Union[datetime.datetime, TExpr]] = None,
        now_col_name: Optional[str] = None,
    ) -> Optional[Union[pa.Array, pa.ChunkedArray]]:
        ans = super().convert_filters(filters, df_schema, timestamp_feature, now, now_col_name)
        if ans is None:
            return None
        # Need to convert from a PyArrowParsedExpr to a column, so it can be passed directly into a PyArrow table
        assert isinstance(ans, PyArrowParsedExpr)
        if isinstance(ans.col, pa.Scalar):
            # If it's a scalar, extend it to an array
            table_deref = self._table()
            if table_deref is None:
                raise ValueError("Table went out of scope")
            return pa.nulls(len(table_deref), pa.bool_()).fill_null(ans.col)
        return ans.col


def convert_filters_to_pl_expr(
    filters: Sequence[Filter],
    df_schema: Mapping[str, pl.PolarsDataType],
    timestamp_feature: Optional[Feature] = None,
    now: Optional[datetime.datetime] = None,
    now_col_name: Optional[str] = None,
) -> Optional[pl.Expr]:
    import polars as pl

    tbl = pl.DataFrame({k: [] for k in df_schema}, df_schema).to_arrow()
    pa_schema = {k: v for (k, v) in zip(tbl.schema.names, tbl.schema.types)}
    ans = PolarsFilterConverter().convert_filters(filters, pa_schema, timestamp_feature, now, now_col_name)
    assert isinstance(ans, pl.Expr) or ans is None
    return ans


class StructAdapter(Protocol[TExpr]):
    """
    Wrapper for a polars or pyarrow struct.
    """

    def get_expr_for_field(self, expr: TExpr, name: str) -> tuple[TExpr, pa.DataType]:
        ...


class _PolarsStructAdapter(StructAdapter["pl.Expr"]):
    def __init__(self, struct_type: pa.StructType):
        self._struct_type = struct_type
        self._name_to_dtype = {f.name: f.type for f in struct_type}

    def get_expr_for_field(self, expr: pl.Expr, name: str) -> tuple[pl.Expr, pa.DataType]:
        return expr.struct.field(name), self._name_to_dtype[name]


class _PyArrowStructAdapter(StructAdapter[ParsedExpr]):
    def __init__(self, struct_type: pa.StructType):
        self._struct_type = struct_type
        self._name_to_dtype = {f.name: f.type for f in struct_type}

    def get_expr_for_field(self, expr: ParsedExpr, name: str) -> tuple[ParsedExpr, pa.DataType]:
        if not isinstance(expr, PyArrowParsedExpr):
            raise TypeError(f"Expected a PyArrow filter expression; got {type(expr)}")

        if isinstance(expr.col, pa.Scalar):
            assert isinstance(expr.col, pa.StructScalar)
            val = expr.col.get(name)
            if val is None:
                raise ValueError(f"Subfield {name} does not exist")
            return PyArrowParsedExpr(val, expr.table), self._name_to_dtype[name]
        if isinstance(expr.col, pa.Array):
            assert isinstance(expr.col, pa.StructArray)
            return PyArrowParsedExpr(expr.col.field(name), expr.table), self._name_to_dtype[name]
        else:
            assert isinstance(expr.col, pa.ChunkedArray)
            projected_chunks: list[pa.Array] = []
            for chunk in expr.col.chunks:
                assert isinstance(chunk, pa.StructArray)
                projected_chunks.append(chunk.field(name))
            return PyArrowParsedExpr(pa.chunked_array(projected_chunks), expr.table), self._name_to_dtype[name]


def filter_data_frame(
    item: Any,
    underlying: Union[pl.DataFrame, pl.LazyFrame],
    namespace: Optional[str],
) -> Union[pl.DataFrame, pl.LazyFrame]:
    # Use the Chalk projection / selection syntax, where we support our Filter objects and
    # selection by column name
    from chalk.features.feature_set import FeatureSetBase

    projections: list[str] = []
    filters: List[Filter] = []
    for x in ensure_tuple(item):
        if isinstance(x, (FeatureWrapper, Feature, str)):
            projections.append(str(x))

        elif isinstance(x, Filter):
            filters.append(x)
        else:
            raise TypeError(
                "When indexing by Filters or Features, it is not simultaneously possible to perform other indexing operations."
            )
    now = _get_filter_now()
    # now = datetime.datetime.now(tz=datetime.timezone.utc)
    timestamp_feature = None if namespace is None else FeatureSetBase.registry[namespace].__chalk_ts__
    pl_expr = convert_filters_to_pl_expr(filters, underlying.schema, timestamp_feature, now)
    df = underlying
    if pl_expr is not None:
        df = df.filter(pl_expr)
    # Do the projection
    if len(projections) > 0:
        polars_cols_set = set(df.columns)
        missing_cols = [c for c in projections if c not in polars_cols_set]
        if len(missing_cols) > 0:
            raise KeyError(
                (
                    f"Attempted to select missing columns [{', '.join(sorted(missing_cols))}] "
                    f"from DataFrame with columns [{', '.join(sorted(list(polars_cols_set)))}]"
                )
            )

        df = df.select(projections)
    return df
