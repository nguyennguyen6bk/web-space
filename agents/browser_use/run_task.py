import ast
import json
from multiprocessing import context
import random
import sys
from browser_use import Agent, ChatGoogle, Browser, BrowserConfig, BrowserSession
from matplotlib import cm
from playwright.async_api import async_playwright
from google import genai
import asyncio
from dotenv import load_dotenv
import os

from evaluate.evaluator import Evaluator
from utils.credential_manager import CredentialManager




override_system_message = """
You are an AI agent that helps users with web browsing tasks.
You can perform actions like clicking buttons, filling forms, and navigating web pages.
You will receive a task description and a URL to start with.
Your final answer must strictly follow the output format required by the task.
Only return what is found on website without any explanation, intro or extra text
No explanation, intro or extra text, prefix, or suffix.
"""

# Tải các biến môi trường từ file .env
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY'+"_"+str(random.randint(1, 7)))
print(f"Using API Key: {api_key}")

model = "gemini-2.5-flash"

llm = ChatGoogle(
    model=model,
    api_key=api_key
)

planner_llm =  ChatGoogle(
    model="gemini-2.0-flash-lite",
    api_key="AIzaSyCtM8ZsIGjLGt_u1CdQaYAm4b_Zw65ol4k"
)


async def login(page, task):
    cm = CredentialManager('./credentials.json')
    site_credential = cm.get_credential(task["start_url"])
    if not site_credential:
        print(f"No credential found for the URL: {task['start_url']}")
    if task["start_url"] == "__SHOPPING_ADMIN__" and task["require_login"]:
        await page.goto(site_credential.get('url'))
        await page.fill('#username', site_credential.get('username'))
        await page.fill('#login', site_credential.get('password'))
        await page.click(".action-login")
    elif task["start_url"] == "__SHOPPING__" and task["require_login"]:
        await page.goto(site_credential.get('url')+"/customer/account/login")
        await page.fill('#email', site_credential.get('username'))
        await page.fill('#pass', site_credential.get('password'))
        await page.click("#send2")
    elif task["start_url"] == "__PROJECT__" and task["require_login"]:
        await page.goto(site_credential.get('url')+"/login")
        await page.fill('#username', site_credential.get('username'))
        await page.fill('#password', site_credential.get('password'))
        await page.click("#login-submit")
    elif task["start_url"] == "__ERP__" and task["require_login"]:
        await page.goto(site_credential.get('url')+"/web/login")
        await page.fill('#login', site_credential.get('username'))
        await page.fill('#password', site_credential.get('password'))
        await page.click("button[type='submit']")
    else:
        await page.goto(site_credential.get('url')) 



async def main(my_arg):
    with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    task_id = my_arg
    task = next((task for task in tasks if task['task_id'] == task_id), None)

    if task:
        print(f"Task ID: {task['task_id']}")
        print(f"Task Description: {task['task_description']}")
    else:
        print(f"Task ID {task_id} not found.")
        return

    testcase = task['task_description']  # Lấy mô tả tác vụ từ task_id


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
        # Run login function to navigate to the start URL and perform login if required
        await login(page, task)
        # create browser session for agent
        browser_session = BrowserSession(
            keep_alive=True,
            browser_context=context,  # all these are supported
            browser=browser,
            playwright=p,
            override_system_message=override_system_message
            
        )

        # Bắt đầu phiên trình duyệt
        await browser_session.start()  

        agent = Agent(
                task = (
                    f"{testcase}\n"                   
                    "Only return what is found without any explanation, intro or extra text. "
                    "Your final answer must be simplest."
                    "Your final answer must strictly follow the output format required by the task."
                    
                ),
                llm=llm,  # Sử dụng mô hình LLM đã khởi tạo        
                save_conversation_path="logs/browser_use",
                override_system_message=override_system_message,
                # browser=browser,
                browser_session=browser_session,  # Sử dụng phiên trình duyệt đã tạo
            )
    
        # Chạy agent và lưu lịch sử cuộc trò chuyện

        history = await agent.run()
        history.save_to_file("agentresults.json")
        agent_result = history.final_result()    
        print(f"agent result on model {model}: {agent_result}")
        if isinstance(agent_result, str):
            try:
                agent_result = json.loads(agent_result)
            except json.JSONDecodeError:
                try:
                    agent_result = ast.literal_eval(agent_result)
                except (ValueError, SyntaxError):
                    pass
         

        #   Đánh giá kết quả của agent
        evaluator = Evaluator(tasks)
        try:
            result = await evaluator.evaluate_with_playwright(task_id, agent_result=agent_result, browser=page)
            print(f"-------------- Evaluation result: {result}")
            assert result is True            
        except Exception as e:
            print(f"An error occurred during evaluation: {e}")
        finally:
            input("Press Enter to close the browser...")
            await browser.close()
        


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = "default"
    asyncio.run(main(arg))



