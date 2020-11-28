import unittest
from query import Query
from query_components import OptionList, OptionData, OptionKey, OptionValue

print(dir(OptionList))


"""
CONDUCTS A SERIES OF SIMPLE TESTS
"""

testcase_obj = unittest.TestCase()


# SHOULD WORK:
test1 = Query().setPrompt("beep boop")\
        .addOption("foo", "bar")\
        .addOption("2", "LALA")\
        .addOption("x", "y")\
        .build()
print(test1.query())

# AUTO OPTION - SHOULD WORK
test2 = Query().setPrompt("beep boop")\
        .addOption("bar")\
        .addOption("LALA")\
        .addOption("y")\
        .build()
print(test2.query())

# MIXED OPTION TYPES - STARTS WITH 1 ARG
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("bar")\
        .addOption("LALA")\
        .addOption("x", "y")\
        .build()

##################################################
# MIXED OPTION TYPES - STARTS WITH 2 ARGS
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("foo", "bar")\
        .addOption("LALA")\
        .addOption("x", "y")\
        .build()

# INVALID TYPE - 1
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption(2, "LALA")


# INVALID TYPE - 2
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("2", 3)\
        .build()

# INVALID TYPE - 3
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption(2, 3)\
        .build()

# INVALID TYPE - 4
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("foo", "bar", "spam")\
        .build()

##################################################

# DUPLICATION
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("foo", "bar")\
        .addOption("foo", "bar")\
        .addOption("x", "y")\
        .build()

# DUPLICATION WITH AUTO OPTION
with testcase_obj.assertRaises(ValueError):
    Query().setPrompt("beep boop")\
        .addOption("bar")\
        .addOption("bar")\
        .addOption("y")\
        .build()





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
