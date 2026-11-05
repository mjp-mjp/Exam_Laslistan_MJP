from behave import when, then
from playwright.sync_api import expect


@when(u'jag går till Lägg till bok')
def step_impl(context):
    context.page.get_by_test_id("add-book").click()


@when(u'jag skriver in titeln "{title}"')
def step_impl(context, title):
    context.page.get_by_test_id("add-input-title").fill(title)


@when(u'jag skriver in författaren "{author}"')
def step_impl(context, author):
    context.page.get_by_test_id("add-input-author").fill(author)


@when(u'jag klickar på Lägg till ny bok')
def step_impl(context):
    context.page.get_by_test_id("add-submit").click()


@when(u'jag går till Katalog')
def step_impl(context):
    context.page.get_by_test_id("catalog").click()


@then(u'boken "{title}" finns i katalogen')
def step_impl(context, title):
    expect(context.page.get_by_test_id("star-" + title)).to_be_visible()
