import unittest
from query_components import OptionList, OptionData, SelectorData, TextData

"""
CONDUCTS A SERIES OF SIMPLE TESTS
"""

testcase_obj = unittest.TestCase()
# WORK:
test_selector = SelectorData("selectorTest")
test_selector = SelectorData("SelectorTest12345")
assert SelectorData("selectorTest").getData() == "selectorTest"


# DO NOT WORK (NON-ALPHA, NON-DIGIT CHARACTERS):
test_selector = testcase_obj.assertRaises(ValueError, SelectorData, "selector test")
test_selector = testcase_obj.assertRaises(ValueError, SelectorData, "selector_test")
test_selector = testcase_obj.assertRaises(ValueError, SelectorData, "")

assert SelectorData("selectorTest") == SelectorData("selectorTest")
assert not (SelectorData("selector1234") == SelectorData("selector4321"))


# GET TEXT TEST
assert str(TextData("test text")) == "test text"
assert TextData("test text").getData() == "test text"
assert TextData("x123") == TextData("x123")
assert not (TextData("x123") == TextData("123x"))

test_text = testcase_obj.assertRaises(ValueError, TextData, "")

# OPTIONS    test_options = testcase_obj.assertRaises(ValueError, Option, "selector test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "selector_test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "selectortest", "")

assert str(OptionData("selector", "text")) == "selector) text"

# OPTION LIST

# DUPLICATE OPTION DATA DIFFERING BY CAPITALIZATION - NO EFFECT
new_list = OptionList()
new_list.addOption(OptionData("foo", "bar"))
new_list.addOption(OptionData("FOO", "BAR"))
new_list.getOptionBySelector("FOO")


with testcase_obj.assertRaises(ValueError):
    # DUPLICATE SELECTOR
    new_list = OptionList()
    new_list.addOption(OptionData("foo", "bar"))
    new_list.addOption(OptionData("foo", "lala"))

with testcase_obj.assertRaises(ValueError):
    # DUPLICATE TEXT
    new_list = OptionList()
    new_list.addOption(OptionData("foo", "bar"))
    new_list.addOption(OptionData("lala", "bar"))
