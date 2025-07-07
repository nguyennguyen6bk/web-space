import json
import sys
import os
import time
from selenium import webdriver
from evaluate.evaluator import Evaluator


with open('./data/tasks_temp.json', 'r', encoding='utf-8') as file:
    tasks = json.load(file)

def test_string_match_exact():
    eva = Evaluator(tasks)

    task_id = "t08";
    agent_result = "BeaBeaumont Summit Kit clothing"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ full screen window
    driver = webdriver.Chrome(options=chrome_options)  # Giả sử bạn đã khởi tạo WebDriver đúng cách
    driver.get("http://localhost:8084")  # Mở một trang web để kiểm tra

    result = eva.evaluate_with_selenium(task_id, agent_result, browser=driver)

    time.sleep(10)

    assert result is True  # Hoặc assert result == expected





if __name__ == "__main__":
    test_string_match_exact()

