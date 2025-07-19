import json
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
import os
from evaluate.evaluator import Evaluator

# Tải các biến môi trường từ file .env
load_dotenv()
browser = Browser()

llm = ChatGoogleGenerativeAI(
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
override_system_message = """
You are an AI agent that helps users with web browsing tasks.
You can perform actions like clicking buttons, filling forms, and navigating web pages.
You will receive a task description and a URL to start with.
"""

extend_system_message = """
REMEMBER the most important RULE:
Only return what is required by the task.
If the task requires to return a specific information, only return that information.
"""

agent = Agent(
        # task="Go to thegioididong and then check price of iPhone 15 Pro Max",  # Tác vụ cho agent
        task = (
            f"{testcase}\n"
            "with url http://localhost:8084/"
        ),
        llm=llm,  # Sử dụng mô hình LLM đã khởi tạo
        browser=browser,  # Sử dụng trình duyệt đã cấu hình
        override_system_message=override_system_message,
        extend_system_message=extend_system_message  # Thay thế hệ thống tin nhắn
    )


# ✅ Đóng trình duyệt sau khi chạy xong
async def main():
    history = await agent.run()

    history.save_to_file("agentresults.json")
    agent_result = history.final_result()    
    print(f"agent result: {agent_result}")

    evaluator = Evaluator(tasks)
    result = await evaluator.evaluate_with_playwright(task_id, agent_result=agent_result, browser=browser)
    assert result is True



    # input("Press Enter to close the browser...")
    await asyncio.sleep(10)
    await browser.close()

asyncio.run(main())


