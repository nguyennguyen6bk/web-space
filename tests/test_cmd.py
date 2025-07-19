import ast
import asyncio
import json
import sys

from playwright.async_api import async_playwright
from browser_use import Agent
from utils.logs_utils import logger


async def main(my_args):
    for i in my_args:
        print(f"Running test with argument: {i}")
        logger.info(f"Running test with argument: {i}")
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                channel="chrome",
                headless=False,
                args=[
                    "--disable-notifications",
                    "--window-size=1280,720"
                ],
            )  
            # chạy browser hiển thị
            context = await browser.new_context(viewport={"width": 1280, "height": 720})  # Thiết lập kích thước cửa sổ trình duyệt
            page = await context.new_page()        
            await page.goto("https://www.google.com")
            await page.wait_for_timeout(5000)  # Chờ 5 giây để trang tải xong
            # Run login function to navigate to the start URL and perform login if required        

def parse_args(args):
    tasks = []
    for arg in args:
        if '-' in arg:
            start, end = arg.split('-')
            start = (int(start) if start.isdigit() else 0)
            end = (int(end) if end.isdigit() else 0)
            tasks.extend(range(start, end + 1))
        else:
            tasks.append(arg)
    return tasks

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1:]
    else:
        arg = ["1"]

    args = parse_args(arg)
    asyncio.run(main(args))