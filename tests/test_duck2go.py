'''
This code used for web testing duckduckgo
'''

import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # initialize geckodriver

    driver = Firefox()

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For clean up, quit the driver
    driver.quit()

def test_duck2go_search(browser):
    # Setup some test case data
    url = 'https://www.duckduckgo.com'
    phrase = 'pytest'

    # Navigate to duckduckgo webpage
    browser.get(url)

    # Locate search input element
    # In the DOM, it has input.js-search-input.search__input--adv as css selector
    search_input = browser.find_element(By.CSS_SELECTOR, 'input.js-search-input.search__input--adv')

    # Send a search phrase and hit RETURN key
    search_input.send_keys(phrase + Keys.RETURN)

    # Verify that result appear on the result page
    link_divs = browser.find_elements(By.CSS_SELECTOR, 'div.results.js-results > div')
    assert len(link_divs) > 0

    # Verify that at least one search result contains the search phrase
    phrase_result = browser.find_elements(By.XPATH, f"//div[@id='links']//*[contains(text(), '{phrase}')]")
    assert len(phrase_result) > 0

    # Verify that the search phrase is the same
    search_input = browser.find_element(By.CSS_SELECTOR, 'input.search__input--adv.js-search-input')
    assert search_input.get_attribute('value') == phrase