import unittest
from query_components import OptionList, OptionData, OptionKey, TextData

"""
CONDUCTS A SERIES OF SIMPLE TESTS
"""

testcase_obj = unittest.TestCase()
# WORK:
test_key = OptionKey("keyTest")
test_key = OptionKey("keyTest12345")
assert OptionKey("keyTest").getData() == "keyTest"


# DO NOT WORK (NON-ALPHA, NON-DIGIT CHARACTERS):
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "key test")
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "key_test")
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "")

assert OptionKey("keyTest") == OptionKey("keyTest")
assert not (OptionKey("key1234") == OptionKey("key4321"))


# GET TEXT TEST
assert str(TextData("test text")) == "test text"
assert TextData("test text").getData() == "test text"
assert TextData("x123") == TextData("x123")
assert not (TextData("x123") == TextData("123x"))

test_text = testcase_obj.assertRaises(ValueError, TextData, "")

# OPTIONS    test_options = testcase_obj.assertRaises(ValueError, Option, "key test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "key_test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "keytest", "")

assert str(OptionData("key", "text")) == "key) text"

# OPTION LIST

# DUPLICATE OPTION DATA DIFFERING BY CAPITALIZATION - NO EFFECT
new_list = OptionList()
new_list.addOption(OptionData("foo", "bar"))
new_list.addOption(OptionData("FOO", "BAR"))
new_list.getOptionByKey("FOO")


with testcase_obj.assertRaises(ValueError):
    # DUPLICATE KEY
    new_list = OptionList()
    new_list.addOption(OptionData("foo", "bar"))
    new_list.addOption(OptionData("foo", "lala"))

with testcase_obj.assertRaises(ValueError):
    # DUPLICATE TEXT
    new_list = OptionList()
    new_list.addOption(OptionData("foo", "bar"))
    new_list.addOption(OptionData("lala", "bar"))
