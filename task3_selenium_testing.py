# Task 03 – Automation Testing with Selenium

'''#Application Under Test (AUT)  
Login Page of Demo Application (https://example.com/login)  

# Objective  
To verify login functionality using Selenium automation with both valid and invalid inputs.  

# Tools & Environment  
- Language: Python  
- Library: Selenium  
- Browser: Google Chrome  
- Driver: ChromeDriver  

# Test Scenarios  
1. **Positive Test** – Login with valid credentials should navigate to Dashboard.  
2. **Negative Test** – Login with invalid credentials should show "Invalid credentials" error.  

## Automation Script  

python'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Give the path of chromedriver.exe
service = Service("C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://example.com/login")

# Positive Test (Valid Credentials)
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "loginBtn").click()

time.sleep(3)  # wait to see result
print("Positive test executed")

driver.quit()

