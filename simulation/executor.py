import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import logging
import subprocess
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_random_data():
    """Generate random data for form filling."""
    return {
        "email": f"{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com",
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
        "name": ''.join(random.choices(string.ascii_letters, k=6)),
        "address": f"{random.randint(1, 999)} {random.choice(['Main St', 'Broadway', 'Elm St'])}"
    }

def execute_operations(operations: list, mode: str = "selenium", cookies: dict = None):
    """Execute a list of operations using Selenium or requests, with support for cookies."""
    if mode == "selenium":
        driver = webdriver.Chrome()
        try:
            if cookies:
                for cookie_name, cookie_value in cookies.items():
                    driver.add_cookie({"name": cookie_name, "value": cookie_value})

            for operation in operations:
                try:
                    if operation["action"] == "click":
                        element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, operation["selector"]))
                        )
                        element.click()
                        logger.info(f"Clicked on element with selector: {operation['selector']}")
                    elif operation["action"] == "input":
                        element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, operation["selector"]))
                        )
                        element.send_keys(operation["value"])
                        logger.info(f"Input value into element with selector: {operation['selector']}")
                except Exception as e:
                    logger.error(f"Error executing operation {operation}: {e}")
        finally:
            driver.quit()
    elif mode == "requests":
        session = requests.Session()
        if cookies:
            session.cookies.update(cookies)

        for operation in operations:
            try:
                if operation["action"] == "get":
                    response = session.get(operation["url"], headers=operation.get("headers", {}))
                    logger.info(f"GET request to {operation['url']} returned status {response.status_code}")
                elif operation["action"] == "post":
                    response = session.post(operation["url"], data=operation.get("data", {}), headers=operation.get("headers", {}))
                    logger.info(f"POST request to {operation['url']} returned status {response.status_code}")
            except Exception as e:
                logger.error(f"Error executing operation {operation}: {e}")

def test_operations_with_curl(url: str, operation_type: str, data: dict = None, headers: dict = None):
    """Test login, registration, and other operations using curl."""
    try:
        curl_command = ["curl", "-X", operation_type.upper(), url]

        if headers:
            for key, value in headers.items():
                curl_command.extend(["-H", f"{key}: {value}"])

        if data:
            curl_command.extend(["-d", "&".join(f"{k}={v}" for k, v in data.items())])

        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        print(f"Curl Response: {result.stdout}")

        # Extract CSRF token dynamically using regex
        csrf_token = re.search(r'name="csrf_token" value="(.*?)"', result.stdout)
        if csrf_token:
            print(f"CSRF Token Found: {csrf_token.group(1)}")
        else:
            print("No CSRF token found.")

    except subprocess.CalledProcessError as e:
        print(f"Error testing operation with curl: {e}")
