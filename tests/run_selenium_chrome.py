from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Tạo ChromeDriver
driver = webdriver.Chrome()

# 2. Truy cập URL bạn cần
driver.get("http://localhost:8084/aim-analog-watch.html")

# 3. CHỜ cho phần tử tồn tại trong DOM
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#product-price-36 .price"))
)

# 4. GỌI trực tiếp JS này
agent_result = driver.execute_script(
    "return document.querySelector('#product-price-36 .price').innerText"
)

print("Kết quả:", agent_result)