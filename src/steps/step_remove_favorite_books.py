import re
from asyncio import timeout
from contextlib import nullcontext
from playwright.sync_api import expect
from behave import when, given, then




@then (u'användaren tar bort på hjärtikonen för "{name}"')
def step_fill_book_title_and_author(context,name):
    remove_from_favorites = context.page.get_by_test_id('star-' + name)
    remove_from_favorites.click(timeout=5000)

    expect(remove_from_favorites).to_have_class("star")

@then (u'boken "{name}" har tagits bort från favorit listan')
def step_book_removed_from_list(context,name):
    book_name = context.page.get_by_text(name)
    expect(book_name).not_to_be_visible()

