import json
from browser_use.llm import ChatGoogle
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
import os


# Tải các biến môi trường từ file .env
load_dotenv()
browser = Browser()

llm = ChatGoogle(
    model="gemini-2.0-flash"
)

with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)
task_id = "1"
task = next((task for task in tasks if task['task_id'] == task_id), None)

if task:
    print(f"Task ID: {task['task_id']}")
    print(f"Task Description: {task['task_description']}")

testcase = task['task_description']  # Lấy mô tả tác vụ từ task_id

agent = Agent(
        # task="Go to thegioididong and then check price of iPhone 15 Pro Max",  # Tác vụ cho agent
        task = (
            f"Role: You are a UI automation agent. Your task is to perform: {testcase}\n"
            "with url http://localhost:8084/"
        ),
        llm=llm,  # Sử dụng mô hình LLM đã khởi tạo
        browser=browser,  # Sử dụng trình duyệt đã cấu hình
    )


# ✅ Đóng trình duyệt sau khi chạy xong
async def main():
    await agent.run()


    input("Press Enter to close the browser...")
    await browser.close()

asyncio.run(main())


