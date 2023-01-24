import asyncio
from playwright.async_api import Playwright, async_playwright, expect
from datetime import datetime
import time


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.netonnet.se/")
    await page.get_by_role("button", name="Tillåt alla cookies").click()
    await page.get_by_role("link", name="Dator & Surfplatta").click()
    await page.get_by_role("link", name="Se allt i Dator & Surfplatta").click()
    await page.locator(".arrow-drop-bold-down").first.click()
    await page.locator("#PaginationControl div").filter(has_text="24").nth(4).click()
    start_time = datetime.now()
    all_products = await page.query_selector_all('div.panel.panel-default.personalization')
    print(all_products)
    print(len(all_products))

    for i in all_products:
        p_n = await i.query_selector('a')
        product_name = await p_n.inner_text()
        # print(product_name)
        p_d = await i.query_selector('div.subTitle.small.productList')
        product_description = await p_d.inner_text()
        # print(product_description)
        p_d_2 = await i.query_selector('div.short-description')
        product_description_2 = await p_d_2.inner_text()
        # print(product_description_2)
        p_p = await i.query_selector('span.price')
        product_price = await p_p.inner_text()
        # print(product_price)

    end_time = datetime.now()
    print(f'tttt- {end_time - start_time}')
    time.sleep(30)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())
