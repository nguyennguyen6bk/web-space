import asyncio
import json
from playwright.async_api import async_playwright
from evaluate.evaluator import Evaluator  # giả sử bạn đã có Evaluator giống như cũ


async def test_dom_match_playwright():
    with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    eva = Evaluator(tasks)
    task_id = "t07"

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=False)  # chạy browser hiển thị
        context = await browser.new_context()
        page = await context.new_page()
        
        # Giả sử hàm evaluate của bạn biết cách dùng page hoặc browser context Playwright
        result = await eva.evaluate_with_playwright(task_id, browser=page)

        await asyncio.sleep(5)

        assert result is True

       


if __name__ == "__main__":
    asyncio.run(test_dom_match_playwright())