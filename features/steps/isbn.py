from behave import *
from src.Isbn import isbn

use_step_matcher('re')


@given('number is in (?P<number>.+)')
def step_impl(context, number):
    context.number = number


@when('the length of number is not 13')
def step_impl(context):
    context.result = isbn(context.number)


@when('the types of all number\'s digits are not integers')
def step_impl(context):
    context.result = isbn(context.number)


@then('the program should return (?P<error>.+)')
def step_impl(context, error):
    assert context.result == error


@when('using isbn function')
def step_impl(context):
    context.result = isbn(context.number)


@then('result should be (?P<result>.+)')
def step_impl(context, result):
    if result == 'True':
        res = True
    else:
        res = False
    assert context.result == res
