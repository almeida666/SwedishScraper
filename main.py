from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.netonnet.se/")
    page.get_by_role("button", name="Tillåt alla cookies").click()
    page.get_by_role("link", name="Dator & Surfplatta").click()
    page.get_by_role("link", name="Se allt i Dator & Surfplatta").click()
    page.locator(".arrow-drop-bold-down").first.click()
    page.locator("#PaginationControl div").filter(has_text="96").nth(4).click()
    for i in range(1, 97):
        try:
            product_name = page.inner_text(f'#productList > div > div:nth-child({i}) > div > div.panel-body > div:nth-child(2) > div.col-xs-7.col-sm-12 > div > div.smallHeader > div.shortText > a')
            product_description = page.inner_text(f'#productList > div > div:nth-child({i}) > div > div.panel-body > div:nth-child(2) > div.col-xs-7.col-sm-12 > div > div.short-description > ul')
            product_price = page.inner_text(f'#productList > div > div:nth-child({i}) > div > div.panel-body > div:nth-child(3) > div > div.footer > div > div > span.price')
            print(product_name)
            print(product_description)
            print(product_price)
        except Exception as e:
            print(e)

    # page.get_by_role("link", name="Datorkomponenter").click()
    # page.get_by_role("link", name="Gaming").click()
    # page.get_by_role("link", name="Hem & Fritid").click()
    # page.get_by_role("link", name="TV").first.click()
    # page.get_by_role("link", name="Ljud").click()
    # page.get_by_role("link", name="Mobil & Smartwatch").click()
    # page.get_by_role("link", name="Vitvaror").click()

    # ---------------------
    context.close()
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)






