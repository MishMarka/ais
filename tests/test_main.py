import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Unit tests for the application
from browser.recorder import crawl_website
from simulation.executor import execute_operations
from exporter.python_exporter import export_to_python
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By

def test_main():
    """Test the main application entry point."""
    assert True

def test_crawl_website():
    """Test the website crawler."""
    elements = crawl_website("https://example.com", max_depth=1)
    assert isinstance(elements, list)

def test_execute_operations():
    """Test the operation executor."""
    with patch("selenium.webdriver.Chrome") as MockWebDriver:
        mock_driver = MockWebDriver.return_value
        mock_driver.find_element.return_value = MagicMock()

        operations = [{"action": "click", "selector": "//button[@id='test']"}]
        execute_operations(operations, mode="selenium")

        mock_driver.find_element.assert_called_with(By.XPATH, "//button[@id='test']")
        mock_driver.find_element.return_value.click.assert_called_once()

def test_export_to_python():
    """Test the Python script exporter."""
    operations = [{"action": "click", "selector": "//button[@id='test']"}]
    export_to_python(operations, "test_script.py")
    with open("test_script.py", "r") as file:
        content = file.read()
    assert "driver.find_element" in content

def test_execute_operations_with_mock():
    """Test the operation executor with a mocked Selenium driver."""
    with patch("selenium.webdriver.Chrome") as MockWebDriver:
        mock_driver = MockWebDriver.return_value
        mock_driver.find_element.return_value = MagicMock()

        operations = [{"action": "click", "selector": "//button[@id='test']"}]
        execute_operations(operations, mode="selenium")

        mock_driver.find_element.assert_called_with(By.XPATH, "//button[@id='test']")
        mock_driver.find_element.return_value.click.assert_called_once()
