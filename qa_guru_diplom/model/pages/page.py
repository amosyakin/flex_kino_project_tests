from selene import browser, have


class Page:
    def __init__(self):
        self.page_title = browser.element('.container__title')

    def should_page_title(self, title_name):
        self.page_title.should(have.text(title_name))

    def should_url_redirect(self, url):
        browser.should(have.url(url))


page = Page()
