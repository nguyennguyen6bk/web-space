import json
import sys
import os
import time
from selenium import webdriver

from selenium.webdriver.remote.webdriver import WebDriver


from evaluate.evaluator import Evaluator



with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

def test_dom_match_selenium():
    eva = Evaluator(tasks)

    task_id = "t07";

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ full screen window
    driver = webdriver.Chrome(options=chrome_options)  # Giả sử bạn đã khởi tạo WebDriver đúng cách

    result = eva.evaluate_with_selenium(task_id, browser=driver)
    time.sleep(5)  # GIỮ script chạy x giây

    assert result is True  # Hoặc assert result == expected






if __name__ == "__main__":
    test_dom_match_selenium()
