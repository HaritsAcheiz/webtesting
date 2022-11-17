from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Duck2GoSearch:
    # Locator Attribute
    url = 'https://www.duckduckgo.com'
    search_input_loc = (By.ID, 'search_form_input_home_page')

    # initializer
    def __init__(self, browser):
        self.browser

    # Interaction Methods

    # Load page methods
    def load(self):
        self.browser.get(self.url)

    #
    def search(self, phrase):
        search_input = self.browser.find_element(*self.search_input_loc)
        search_input.send_keys(phrase + Keys.RETURN)