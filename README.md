# Smart Website Interaction Analyzer & Simulator

This project is a Python-based platform designed to:

- Crawl and analyze web pages.
- Understand site behavior using GitHub's GPT-o4 model.
- Simulate operations via Selenium or requests/Hyper.
- Record user interactions using a built-in browser.
- Generate fully functional Python automation scripts.
- Test all flows automatically to ensure schema and logic validity.
- Store and manage projects locally with export capabilities.

## Features

- **Website Crawler**: Recursively crawls site structure and detects interactive elements.
- **GPT-o4 Powered Analyzer**: Analyzes pages and identifies high-level operations.
- **Simulation & Execution Modes**: Supports Selenium and requests/Hyper modes.
- **Built-in Test Runner**: Validates flows with end-to-end testing.
- **Interactive Browser**: Records user actions and generates operation tables.
- **Python Code Export**: Exports clean Python scripts for automation.
- **Local Project Management**: Stores and manages projects in SQLite.

## Updated Features

- **Enhanced Website Crawler**: Now supports SPAs and shadow DOM elements for better detection of interactive elements.
- **Improved Error Handling and Logging**: Added robust error handling and detailed logging across all modules.
- **Complete GPT-o4 Analyzer**: Fully implemented logic for analyzing web pages using the GPT-o4 API.

## Getting Started

1. Install the required extensions:
   - Python Extension for Visual Studio Code
   - Python Environments Extension for Visual Studio Code

2. Use the configured Python environment for running and testing code.

3. Follow the development flow to analyze, simulate, and export operations.

## Development Flow

1. Input a URL to crawl and analyze.
2. View detected operations and select desired flows.
3. Simulate operations using Selenium or requests.
4. Test and validate flows.
5. Export Python scripts for automation.

## Usage Instructions

1. **Crawling a Website**:
   ```bash
   python app/main.py --url "https://example.com" --depth 2
   ```
   This will crawl the website up to a depth of 2 and detect interactive elements.

2. **Simulating Operations**:
   ```bash
   python app/main.py --url "https://example.com" --mode selenium
   ```
   This will execute detected operations using Selenium.

3. **Exporting Python Scripts**:
   ```bash
   python app/main.py --url "https://example.com" --export "output_script.py"
   ```
   This will export the operations as a Python script.

4. **Analyzing a Web Page**:
   Use the `analyze_page` function in `analyzer/gpt_analyzer.py` to analyze page content with the GPT-o4 API.

## Example Workflow

1. Crawl a website to detect elements.
2. Simulate operations to validate flows.
3. Analyze the page content for insights.
4. Export the operations as a Python script for automation.

## Requirements

- Python 3.13 or higher
- Visual Studio Code with the required extensions
- SQLite for local project management

## License

This project is licensed under the MIT License.
"# ais" 
