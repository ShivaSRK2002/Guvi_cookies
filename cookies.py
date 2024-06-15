import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the chromedriver executable
chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after the script finishes

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

# Configuration
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

try:
    # Open the URL and maximize the window
    driver.get(url)
    driver.maximize_window()

    # Display cookies before login
    print("Cookies before login:")
    cookies_before_login = driver.get_cookies()
    for cookie in cookies_before_login:
        print(cookie)

    # Log in
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Wait until the inventory list page is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Display cookies after login
    print("\nCookies after login:")
    cookies_after_login = driver.get_cookies()
    for cookie in cookies_after_login:
        print(cookie)

    # Log out
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    # Display cookies after logout
    print("\nCookies after logout:")
    cookies_after_logout = driver.get_cookies()
    for cookie in cookies_after_logout:
        print(cookie)

finally:
    # Close the WebDriver
    driver.quit()
