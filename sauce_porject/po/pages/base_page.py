from typing import Union

from playwright.sync_api import Locator, Page


class BasePage:
    """
    A base class for page objects in UI automation frameworks.

    This class provides common functionality for interacting with web pages,
    such as managing the Playwright Page instance and handling locators.

    Attributes:
        _page (Page): The Playwright Page instance used for browser interactions.
        _timeout (int): Default timeout (in milliseconds) for page actions.

    Args:
        page (Page): The Playwright Page object to interact with.
        timeout (int, optional): Default timeout for actions, in milliseconds. Defaults to 10000.
    """

    def __init__(self, page: Page, timeout: int = 10000) -> None:
        """
        Initializes the BasePage with a Playwright Page instance and an optional timeout.

        Args:
            page (Page): The Playwright Page object to interact with.
            timeout (int, optional): Default timeout for actions, in milliseconds. Defaults to 10000.
        """
        self._page = page
        self._timeout = timeout

    def locator(self, selector_or_locator: Union[str, Locator]) -> Locator:
        """
        Returns a Playwright Locator object for the given selector or locator.

        Args:
            selector_or_locator (Union[str, Locator]): A CSS selector string or an existing Locator object.

        Returns:
            Locator: A Playwright Locator object corresponding to the selector or the provided Locator.
        """
        if isinstance(selector_or_locator, str):
            return self._page.locator(selector_or_locator)
        else:
            return selector_or_locator
