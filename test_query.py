import unittest
from query import Query
from query_components import OptionList, OptionData, SelectorData, TextData


"""
CONDUCTS A SERIES OF SIMPLE TESTS
"""

testcase_obj = unittest.TestCase()

test_options = testcase_obj.assertRaises(ValueError, OptionData, "selector test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "selector_test", "text")
test_options = testcase_obj.assertRaises(ValueError, OptionData, "selectortest", "")

test_options = testcase_obj.assertEqual(str(OptionData("selector", "text")), "selector) text")

# SHOULD WORK:
test1 = Query().setPrompt("beep boop")\
        .addOption("foo", "bar")\
        .addOption("2", "LALA")\
        .addOption("x", "y")\
        .build()

print(test1.query())

# DUPLICATION
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("foo", "bar")\
        .addOption("foo", "bar")\
        .addOption("x", "y")\
        .build()

print("post duplication")

# REMAINING TESTS:

with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("")

with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("x").build()

with testcase_obj.assertRaises(ValueError):
    Query().build()

with testcase_obj.assertRaises(ValueError):
    test1.build()
    test1.query()
