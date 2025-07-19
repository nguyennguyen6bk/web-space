
# Open Chrome browser by playwrightser
import asyncio
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from playwright.async_api import async_playwright

async def test_async_profile():
    async with async_playwright() as playwright:
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir="D:\\Profiles\\Profile 7\\Chrome",
            headless=False,
            channel="chrome"
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await page.set_viewport_size({"width": 1536, "height": 864})
        await page.goto("https://www.google.com")
        await page.goto("http://localhost:8070/web?reload=true#action=119&cids=1&menu_id=76")
        await page.wait_for_timeout(5000)  # Chờ 5 giây để trang tải xong
        js_result = await page.evaluate("[...document.querySelectorAll('button.o-mail-DiscussSidebarChannel')].some(btn => btn.innerText.includes('Dev Team Chat'))")
        print(f"JS Result: {js_result}")
        input("Press Enter to close the browser...")
        await context.close()


asyncio.run(test_async_profile())

