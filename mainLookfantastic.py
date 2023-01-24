import asyncio
import time
from playwright.async_api import Playwright, async_playwright, expect
from datetime import datetime


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.lookfantastic.se/health-beauty/hair/view-all-haircare.list?pageNumber=2")
    await page.get_by_role("button", name="Stäng").click()
    # await page.get_by_role("navigation", name="Pages Top").get_by_role("link", name="Go to page 2").click()
    start_time = datetime.now()

    for p in range(1, 59):
        await page.goto(f"https://www.lookfantastic.se/health-beauty/hair/view-all-haircare.list?pageNumber={p}")
        # await page.get_by_role("navigation", name="Pages Top").get_by_role("link", name=f"Go to page {p}").click()
        await page.wait_for_selector('div.productBlock')

        all_products = await page.query_selector_all('div.productBlock')
        print(all_products)
        print(len(all_products))

        for i in all_products:
            p_n = await i.query_selector('h3.productBlock_productName')
            product_name = await p_n.inner_text()
            print(product_name.strip())
            # p_d = await i.query_selector('div.subTitle.small.productList')
            # product_description = await p_d.inner_text()
            # print(product_description)
            # p_d_2 = await i.query_selector('div.short-description')
            # product_description_2 = await p_d_2.inner_text()
            # print(product_description_2)
            p_p = await i.query_selector('span.productBlock_priceValue')
            product_price = await p_p.inner_text()
            print(product_price)

    end_time = datetime.now()
    print(f'tttt- {end_time - start_time}')
    time.sleep(5)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())