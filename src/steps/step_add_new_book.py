import re
from contextlib import nullcontext
from playwright.sync_api import expect
from behave import when, given, then

base_url = 'https://tap-vt25-testverktyg.github.io/exam--reading-list/'

@given (u'användaren är på startsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url, timeout=5000)

@when (u'användaren trycker på knappen "Lägg till bok"')
def step_click_add_new_book__show_form(context):
    show_form_button = context.page.get_by_test_id('add-book')
    show_form_button.click(timeout=300)

@then (u'"Lägg till ny bok" knappen går inte att trycka på med tomma textfält')
def step_add_book_button_disabled(context):
    submit_button = context.page.get_by_test_id('add-submit')
    expect(submit_button).to_be_disabled()

@then (u'användaren skriver in "{titel}" och "{forfattare}" i text fälten')
def step_fill_book_title_and_author(context,titel, forfattare):
    title_textbox = context.page.get_by_test_id('add-input-title')
    title_textbox.fill(titel)
    forfattare_textbox = context.page.get_by_test_id('add-input-author')
    forfattare_textbox.fill(forfattare)

@then (u'användaren trycker på "Lägg till ny bok"')
def step_add_new_book_to_list(context):
    commit_button = context.page.get_by_test_id('add-submit')
    commit_button.click()

@then (u'Titel och Författare fälten töms')
def step_clear_title_and_authour_field(context):
    title_textbox = context.page.get_by_test_id('add-input-title')
    forfattare_textbox = context.page.get_by_test_id('add-input-author')
    expect(title_textbox).to_be_empty()
    expect(forfattare_textbox).to_be_empty()

@then (u'användaren trycker på knappen "Katalog"')
def step_go_to_start_page(context):
    context.page.get_by_test_id('catalog').click()

@then (u'En ny bok som heter "{titel}" av "{forfattare}" har lagts till sist i Katalogen')
def step_books_added_to_catalog(context, titel, forfattare):
    new_book_title = context.page.get_by_text(titel)
    new_book_author = context.page.get_by_text(forfattare)
    expect(new_book_title).to_be_visible()
    expect(new_book_author).to_be_visible()