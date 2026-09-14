import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def browser_context_args(
    browser_context_args,
    playwright: Playwright
):
    iphone = playwright.devices["iPhone 12"]

    return {
        **browser_context_args,
        **iphone,
    }