import pyarrow as pa
import pyarrow.compute as pc


def _calculate_column_mean(
    table,
    column_name: str
) -> float:
    """
    Use built-in pyarrow compute functions to calculate the mean of a column.
    """
    return pc.mean(table[column_name]).as_py()


def expect_column_mean_greater_than(
    table,
    column_name: str,
    value: float
):
    """
    Given a column name, expect the mean of that column to be greater than value.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    _mean = _calculate_column_mean(table, column_name)
    return _mean > value


def expect_column_mean_greater_or_equal_than(
    table,
    column_name: str,
    value: float
):
    """
    Given a column name, expect the mean of that column to be greater or equal than value.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    _mean = _calculate_column_mean(table, column_name)
    return _mean >= value


def expect_column_mean_smaller_than(
    table,
    column_name: str,
    value: float
):
    """
    Given a column name, expect the mean of that column to be smaller than value.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    _mean = _calculate_column_mean(table, column_name)
    return _mean < value


def expect_column_mean_smaller_or_equal_than(
    table,
    column_name: str,
    value: float
):
    """
    Given a column name, expect the mean of that column to be smaller or equal than value.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    _mean = _calculate_column_mean(table, column_name)
    return _mean <= value


def _column_nulls(
    table,
    column_name: str
) -> bool:
    """
    Return number of nulls in a column.
    """
    return table[column_name].null_count


def expect_column_some_null(
    table,
    column_name: str
):
    """
    Given a column name, expect the column to have nulls.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    return _column_nulls(table, column_name) > 0


def expect_column_no_nulls(
    table,
    column_name: str
):
    """
    Given a column name, expect the column to not have nulls.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    return _column_nulls(table, column_name) == 0


def expect_column_all_null(
    table,
    column_name: str
):
    """
    Given a column name, expect the column to be all nulls.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    return _column_nulls(table, column_name) == table[column_name].length()


def _column_unique(
    table,
    column_name: str
) -> bool:
    """
    Return number of unique values in a column.
    """
    return table[column_name].value_counts()


def expect_column_all_unique(
    table,
    column_name: str
):
    """
    Given a column name, expect the column to have all unique values.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    return _column_unique(table, column_name) == table[column_name].length()


def expect_column_not_unique(
    table,
    column_name: str
):
    """
    Given a column name, expect the column to have non-unique values.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """
    return _column_unique(table, column_name) < table[column_name].length()


def _column_accepted_values(
    table,
    column_name: str,
    accepted_values: list
) -> bool:
    """
    Return number of unique values in a column.
    """
    return pc.all(pc.is_in(table[column_name], pa.array(accepted_values)))


def expect_column_accepted_values(
    table,
    column_name: str,
    accepted_values: list
):
    """
    Given a column name, expect the column to have only accepted values.

    Return a boolean, so that the wrapping function can assert on it and produce
    any custom error messages.
    """

    return _column_accepted_values(table, column_name, accepted_values)
