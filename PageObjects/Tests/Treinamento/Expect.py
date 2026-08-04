
from playwright.sync_api import expect
def test_expect(page):
    page.goto("https://automationexercise.com/login")
    page.pause()
    page.locator('.login-form h2').dblclick()


def test_hover(page: Page):
    page.goto('https://automationexercise.com')
    page.pause()
    page.locator('.single-products:visible').filter(has_text='Madame Top For Women').hover()
    page.locator(
        'div:nth-child(9) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn').click()
    expect(page.locator('#cartModal')).to_contain_text('Your product has been added to cart.', timeout=10000)
    expect(page.get_by_role('button', name='Continue Shopping')).to_be_visible()
    expect(page.get_by_role('button', name='Continue Shopping')).to_be_enabled()
    page.get_by_role('button', name='Continue Shopping').click()
    expect(page.locator('#cartModal')).not_to_be_visible()
