# import pytest

from dekatrian_date_conversion import (
    dek_to_week,
    greg_to_dek,
    dekatrian_week,
    week_day_on_first_auroran,
    year_day_on_deka_date,
    year_day_on_greg_date,
    dek_to_greg,
)

# given = pytest.mark.parametrize


# @given("fn", [BaseClass(), base_function])
# def test_parameterized(fn):
#     assert "hello from" in fn()


def test_dek_to_week_function():
    assert dek_to_week(28, 13, 2015) == 5


def test_dekatrian_week_function():
    assert dekatrian_week(1, 0) == 0


def test_week_day_on_first_auroran_function():
    assert week_day_on_first_auroran(2016) == 1


def test_year_day_on_deka_date_function():
    assert year_day_on_deka_date(3, 1, 2017) == 4


def test_dek_to_greg_function():
    assert dek_to_greg(10, 10, 2017) == (10, 10, 2017)  # error


def test_year_day_on_greg_date_function():
    assert year_day_on_greg_date(29, 12, 2016) == 364


def test_greg_to_dek_function():
    assert greg_to_dek(3, 1, 2016) == (1, 1, 2016)
