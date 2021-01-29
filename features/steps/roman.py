from behave import *
from src.Roman import Roman

use_step_matcher("re")


@given('we have (?P<arabic>.+) number and number convertion program')
def step_impl(context, arabic):
    context.arabic = int(arabic)
    context.roman_convert = Roman()


@when('we have (?P<roman>.+) number')
def step_impl(context, roman):
    context.roman = roman


@then('the program\'s result should be correct')
def step_impl(context):
    assert context.roman == context.roman_convert.roman(context.arabic)
