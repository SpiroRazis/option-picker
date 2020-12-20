import unittest
from query_components import OptionList, OptionData, OptionKey, OptionValue, PromptStatement

"""
CONDUCTS A SERIES OF SIMPLE TESTS
"""

testcase_obj = unittest.TestCase()

test_prompt = PromptStatement("promptTest")
assert PromptStatement("promptTest").getData() == "promptTest"
test_prompt = testcase_obj.assertRaises(ValueError, PromptStatement, "")
test_prompt = testcase_obj.assertRaises(TypeError, PromptStatement.isValidContent, 1)

# WORK:
test_key = OptionKey("keyTest")
test_key = OptionKey("keyTest12345")
assert OptionKey("keyTest").getData() == "keyTest"


# DO NOT WORK (NON-ALPHA, NON-DIGIT CHARACTERS):
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "key test")
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "key_test")
test_key = testcase_obj.assertRaises(ValueError, OptionKey, "")
test_key = testcase_obj.assertRaises(TypeError, OptionKey.isValidContent, 1)

assert OptionKey("keyTest") == OptionKey("keyTest")
assert not (OptionKey("key1234") == OptionKey("key4321"))


# GET TEXT TEST
assert str(OptionValue("test text")) == "test text"
assert OptionValue("test text").getData() == "test text"
assert OptionValue("x123") == OptionValue("x123")
assert not (OptionValue("x123") == OptionValue("123x"))

test_text = testcase_obj.assertRaises(ValueError, OptionValue, "")
test_text = testcase_obj.assertRaises(TypeError, OptionValue.isValidContent, 1)


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
