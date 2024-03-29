""" Tests for the ``words_to_number()`` function. """
import hypothesis.strategies as st
from hypothesis import given
from hypothesis.strategies._internal.core import DataObject

from telephone.utils import find_occurrences
from telephone.words_to_number import words_to_number
from telephone.tests.generators import generate_phoneword
from telephone.tests.test_constants import US_LETTER_MAP, GENERAL_FORMAT, US_FORMAT

# pylint: disable=bad-continuation


@given(st.data(), st.from_regex(GENERAL_FORMAT, fullmatch=True))
def test_words_to_number_places_dashes_correctly(
    data: DataObject, numformat: str
) -> None:
    """
    Tests that we generate numbers with the dashes in the right place.

    Parameters
    ----------
    phoneword : ``str``.
        A string consisting of dashes, numbers, and alpha characters. Always starts
        with ``1`` and ends with an alphanumeric character. At most 1 dash in a row.
        e.g. ``1-ALPHA-54792-BRAVO``.
    """
    phoneword = generate_phoneword(data, numformat=numformat)

    # Translate to a number.
    number = words_to_number(phoneword, letter_map=US_LETTER_MAP, numformat=numformat)
    assert find_occurrences(number, "-") == find_occurrences(numformat, "-")


@given(st.data(), st.from_regex(GENERAL_FORMAT, fullmatch=True))
def test_words_to_number_output_is_numeric(data: DataObject, numformat: str) -> None:
    """
    Tests that the function doesn't return anything with letters in it.

    Parameters
    ----------
    phoneword : ``str``.
        A string consisting of dashes, numbers, and alpha characters. Always starts
        with ``1`` and ends with an alphanumeric character. At most 1 dash in a row.
        e.g. ``1-ALPHA-54792-BRAVO``.
    """
    phoneword = generate_phoneword(data, numformat=numformat)
    number = words_to_number(phoneword, letter_map=US_LETTER_MAP, numformat=numformat)
    dashless_number = number.replace("-", "")
    assert dashless_number.isnumeric()


@given(st.data(), st.from_regex(GENERAL_FORMAT, fullmatch=True))
def test_words_to_number_yields_correct_length(
    data: DataObject, numformat: str
) -> None:
    """
    Tests that we generate numbers with the correct length.

    Parameters
    ----------
    phoneword : ``str``.
        A string consisting of dashes, numbers, and alpha characters. Always starts
        with ``1`` and ends with an alphanumeric character. At most 1 dash in a row.
        e.g. ``1-ALPHA-54792-BRAVO``.
    """
    phoneword = generate_phoneword(data, numformat=numformat)
    number = words_to_number(phoneword, letter_map=US_LETTER_MAP, numformat=numformat)
    assert len(number) == len(numformat)


def test_words_to_number_manual() -> None:
    """ Manual test. """
    number = words_to_number("1-877-KARS-4-KIDS", US_FORMAT, US_LETTER_MAP)
    assert number == "1-877-527-7454"


def test_words_to_number_uses_default_arguments() -> None:
    """ Manual test. """
    number = words_to_number("1-877-KARS-4-KIDS")
    assert number == "1-877-5277-4-5437"
