# Built-in browser for recording user actions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from seleniumwire import webdriver
from bs4 import BeautifulSoup
import threading
import time

def record_user_actions(url: str):
    """Record user actions using Selenium."""
    driver = webdriver.Chrome()
    driver.get(url)

    actions = []

    try:
        print("Recording user actions. Perform actions in the browser.")
        input("Press Enter when done...")

        # Example: Capture clicks and inputs (extend as needed)
        elements = driver.find_elements(By.XPATH, "//*")
        for element in elements:
            if element.tag_name in ["button", "a", "input"]:
                actions.append({
                    "action": "click" if element.tag_name != "input" else "input",
                    "selector": element.get_attribute("xpath"),
                    "value": element.get_attribute("value") if element.tag_name == "input" else None
                })

        print("Actions recorded:", actions)
    finally:
        driver.quit()

    return actions

def crawl_website(url: str, max_depth: int = 2):
    """Recursively crawl a website using threading, BeautifulSoup, and selenium-wire."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Block images

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    visited_urls = set()
    elements = []
    lock = threading.Lock()

    def crawl(current_url, depth):
        if depth > max_depth or current_url in visited_urls:
            return

        with lock:
            visited_urls.add(current_url)

        driver.get(current_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Detect interactive elements
        for tag in soup.find_all(["button", "a", "input", "form"]):
            elements.append({
                "tag": tag.name,
                "text": tag.get_text(strip=True),
                "attributes": tag.attrs
            })

        # Handle links for SPAs
        links = [a["href"] for a in soup.find_all("a", href=True)]
        threads = []
        for link in links:
            thread = threading.Thread(target=crawl, args=(link, depth + 1))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    crawl(url, 0)
    driver.quit()
    return elements
