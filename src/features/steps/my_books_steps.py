from behave import when, then
from playwright.sync_api import expect


@when(u'jag går till Mina böcker fliken genom att klicka på fliken')
def step_impl(context):
    context.page.get_by_test_id("favorites").click()


@then(u'boken "{title}" syns under fliken Mina böcker')
def step_impl(context, title):
    expect(context.page.get_by_test_id("fav-" + title)).to_be_visible()