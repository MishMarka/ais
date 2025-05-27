# Python script generation
from typing import List
import subprocess
import pandas as pd

def export_to_python(operations: List[dict], filename: str):
    """Export operations to a Python script."""
    with open(filename, "w") as file:
        file.write("import time\n")
        file.write("from selenium import webdriver\n")
        file.write("from selenium.webdriver.common.by import By\n\n")
        file.write("driver = webdriver.Chrome()\n")

        for operation in operations:
            if operation["action"] == "click":
                file.write(f"driver.find_element(By.XPATH, \"{operation['selector']}\").click()\n")
            elif operation["action"] == "input":
                file.write(f"driver.find_element(By.XPATH, \"{operation['selector']}\").send_keys(\"{operation['value']}\")\n")

        file.write("driver.quit()\n")

    print(f"Python script exported to {filename}")

def export_to_exe(python_script: str, output_name: str):
    """Export a Python script to an executable using pyinstaller."""
    try:
        subprocess.run([
            "pyinstaller",
            "--onefile",
            "--name",
            output_name,
            python_script
        ], check=True)
        print(f"Executable {output_name}.exe created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating executable: {e}")

def export_to_table(data: list, output_file: str):
    """Export data to a table format (CSV or HTML)."""
    try:
        df = pd.DataFrame(data)
        if output_file.endswith(".csv"):
            df.to_csv(output_file, index=False)
            print(f"Data exported to {output_file} as CSV.")
        elif output_file.endswith(".html"):
            df.to_html(output_file, index=False)
            print(f"Data exported to {output_file} as HTML.")
        else:
            print("Unsupported file format. Please use .csv or .html.")
    except Exception as e:
        print(f"Error exporting data to table: {e}")
