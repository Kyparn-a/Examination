import re
from contextlib import nullcontext
from playwright.sync_api import expect
from behave import when, given, then

@when (u'användaren trycker på knappen "Mina böcker"')
def step_go_to_favorites(context):
    favorites_button = context.page.get_by_test_id('favorites')
    favorites_button.click()


@then (u'texten "När du valt, kommer dina favoritböcker att visas här." syns på sidan')
def step_empty_favorites_list(context):
    favorites_list = context.page.get_by_text('När du valt')
    expect(favorites_list).to_be_visible()

@then (u'användaren trycker på hjärtikonen för "{name}"')
def step_add_book_to_favorites(context, name):
    add_to_favorites = context.page.get_by_test_id('star-' + name)
    add_to_favorites.click()
    expect(add_to_favorites).to_have_class("star selected")


@then (u'texten "När du valt, kommer dina favoritböcker att visas här." syns inte på sidan')
def step_empty_list_text_not_shown(context):
    favorites_list = context.page.get_by_text('När du valt')
    expect(favorites_list).not_to_be_visible()

@then (u'en lista med böckerna "{book1}" och "{book2}" syns på sidan')
def step_favorites_list_shown(context, book1, book2):
    favorite_book_1 = context.page.get_by_test_id('fav-'+book1)
    favorite_book_2 = context.page.get_by_test_id('fav-'+book2)
    expect(favorite_book_1).to_be_visible()
    expect(favorite_book_2).to_be_visible()