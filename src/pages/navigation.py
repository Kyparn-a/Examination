class Navigation:
    def __init__(self, page):
        self.page = page
        self.add_book_page = page.get_by_test_id('add-book')
        self.favorites_page = page.get_by_test_id('favorites')
        self.catalog_page = page.get_by_test_id('catalog')

    def startpage(self):
        self.page.goto("https://tap-vt25-testverktyg.github.io/exam--reading-list/")

    def go_to_add_book(self):
        self.add_book_page.click()

    def go_to_favorites(self):
        self.favorites_page.click()

    def go_to_catalog(self):
        self.catalog_page.click()