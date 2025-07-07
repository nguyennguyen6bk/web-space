from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
import os

# Tải các biến môi trường từ file .env
load_dotenv()
browser = Browser()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash"
)

testcase = "Purchase 3 units of the product named 'Push It Messenger Bag', then retrieve the total order amount."

agent = Agent(
        # task="Go to thegioididong and then check price of iPhone 15 Pro Max",  # Tác vụ cho agent
        task = (
            f"Role: You are a UI automation agent. Your task is to perform {testcase}\n"
            "Instructions:\n"
            "- Home page : http://localhost:8084/\n"
            "Output:\n"
            "- result return in JSON with format:\n"
            """ 
                    {
                    "string-match": "<result>",
                    "regex-match": {"amount": "<result>"}
                    }
            """
        ),
        llm=llm,  # Sử dụng mô hình LLM đã khởi tạo
        browser=browser,  # Sử dụng trình duyệt đã cấu hình
    )


# ✅ Đóng trình duyệt sau khi chạy xong
async def main():
    await agent.run()
    input("Press Enter to close the browser...")  # Đợi người dùng nhấn Enter trước khi đóng trình duyệt
    await browser.close()  # <-- Đóng trình duyệt ở đây

asyncio.run(main())


