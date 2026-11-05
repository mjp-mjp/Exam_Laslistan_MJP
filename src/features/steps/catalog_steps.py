import re
from behave import given, when, then
from playwright.sync_api import expect


@given(u'jag är på startsidan')
def step_impl(context):
    context.page.goto(context.base_url)


@when(u'jag klickar på hjärtat för "{title}"')
def step_impl(context, title):
    context.page.get_by_test_id("star-" + title).click()


@then(u'boken "{title}" är markerad som favorit')
def step_impl(context, title):
    heart = context.page.get_by_test_id("star-" + title)
    expect(heart).to_have_class(re.compile("selected"))
    