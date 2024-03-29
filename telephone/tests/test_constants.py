""" Constants for the telephone test suite. """
import re
import json

PHONEWORD = re.compile(r"^1((-([A-Z]){1,10})|(-([0-9]){1,10})){1,10}$")
US_NUMBER = re.compile(r"1-[0-9]{3}-[0-9]{3}-[0-9]{4}")
US_NUMBER_NODASH = re.compile(r"^1[0-9]{10}$")
US_ALPHANUMERIC = re.compile(r"^1[A-Z0-9]{10}$")
UPPERCASE_ALPHA = re.compile(r"[A-Z]+")
LOWERCASE_ALPHA = re.compile(r"[a-z]+")
GENERAL_FORMAT = re.compile(r"^0+(-0+)+$")
US_FORMAT = "0-000-000-0000"
TEST_FORMAT = US_FORMAT
with open("telephone/settings/mapping.json", "r") as MAPPING_FILE:
    US_LETTER_MAP = json.load(MAPPING_FILE)
