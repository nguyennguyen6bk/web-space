import asyncio
from playwright.async_api import async_playwright
import json
import sys
import os
from evaluate.evaluator import Evaluator


with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

async def test_string_match_exact():
    eva = Evaluator(tasks)

    task_id = "t08"
    agent_result = "Beaumont Summit Kit clothing"

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=False)  # chạy browser hiển thị
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("http://localhost:8084")  # Mở một trang web để kiểm tra

        result = await eva.evaluate_with_playwright(task_id, agent_result=agent_result, browser=page)


        await asyncio.sleep(5)  # Chờ một chút để xem kết quả

        assert result is True  # Hoặc assert result == expected


if __name__ == "__main__":
    asyncio.run(test_string_match_exact())

