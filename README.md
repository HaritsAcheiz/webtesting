# webtesting
Learn web testing

Locator Attributes

The only locator in this class is SEARCH_INPUT, which finds the search input element. It is a class (or “static”) attribute because the value should be the same for all search pages. It is also written as a tuple because every locator has two parts: a type (like By.ID or By.XPATH) and a query. This locator finds the search element by the name “q”. Writing locators as class attribute tuples makes them very readable and accessible. Locators should always have intuitive names, too.
Initializer

All page objects need a reference to the WebDriver instance. Typically, it is injected via the constructor. Here, it is passed into the __init__ method as the browser parameter and then stored as the self.browser attribute. Dependency injection allows page objects to polymorphically use any type of WebDriver, whether it’s ChromeDriver, IEDriver, or something else. It also lets the test framework control setup and cleanup.
Interaction Methods

Interaction methods should be intuitively named. The load method navigates the browser to the search page. Notice that URL is a class attribute. The search method enters the search phrase into the input field, but now the phrase is parametrized so that any phrase may be used.