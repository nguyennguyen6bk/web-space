import ast
import json
import random
from browser_use import Agent, Browser, BrowserConfig
from browser_use import ChatGoogle
from google import genai
import asyncio
from dotenv import load_dotenv
import os
from evaluate.evaluator import Evaluator

# Tải các biến môi trường từ file .env
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY'+"_"+str(random.randint(1, 4)))
print(f"Using API Key: {api_key}")

browser = Browser()

llm = ChatGoogle(
    model="gemini-2.0-flash",
    api_key=api_key
)

planner_llm =  ChatGoogle(
    model="gemini-2.0-flash-lite",
    api_key="AIzaSyCtM8ZsIGjLGt_u1CdQaYAm4b_Zw65ol4k"
)

with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

task_id = "3"
task = next((task for task in tasks if task['task_id'] == task_id), None)

if task:
    print(f"Task ID: {task['task_id']}")
    print(f"Task Description: {task['task_description']}")

testcase = task['task_description']  # Lấy mô tả tác vụ từ task_id
override_system_message = """
You are an AI agent that helps users with web browsing tasks.
You can perform actions like clicking buttons, filling forms, and navigating web pages.
You will receive a task description and a URL to start with.
Your final answer must strictly follow the output format required by the task.
You MUST NOT add any explanation, context, or extra text.
"""
agent = Agent(
        # task="Go to thegioididong and then check price of iPhone 15 Pro Max",  # Tác vụ cho agent
        task = (
            f"{testcase}\n"
            "with url http://localhost:8084/"
        ),
        llm=llm,  # Sử dụng mô hình LLM đã khởi tạo
        browser=browser,  # Sử dụng trình duyệt đã cấu hình
        save_conversation_path="logs/browser_use",
        override_system_message=override_system_message,
        # planner_llm=planner_llm, 
        # planner_interval=4
    )


# ✅ Đóng trình duyệt sau khi chạy xong
async def main():
    history = await agent.run()

    history.save_to_file("agentresults.json")
    agent_result = history.final_result()    
    print(f"agent result: {agent_result}")
    if isinstance(agent_result, str):
        try:
            agent_result = json.loads(agent_result)
        except json.JSONDecodeError:
            try:
                agent_result = ast.literal_eval(agent_result)
            except (ValueError, SyntaxError):
                pass

    evaluator = Evaluator(tasks)
    result = await evaluator.evaluate_with_playwright(task_id, agent_result=agent_result, browser=browser)
    assert result is True



    await asyncio.sleep(10)
    await browser.close()

asyncio.run(main())


