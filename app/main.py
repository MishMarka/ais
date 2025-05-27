import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from browser.recorder import crawl_website
from simulation.executor import execute_operations
from exporter.python_exporter import export_to_python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Smart Website Interaction Analyzer & Simulator")
    parser.add_argument("--url", type=str, help="URL to crawl and analyze")
    parser.add_argument("--depth", type=int, default=2, help="Depth for crawling")
    parser.add_argument("--mode", type=str, choices=["selenium", "requests"], default="selenium", help="Execution mode")
    parser.add_argument("--export", type=str, help="File to export Python script")

    args = parser.parse_args()

    if args.url:
        print(f"Crawling website: {args.url}")
        elements = crawl_website(args.url, max_depth=args.depth)
        print(f"Detected elements: {elements}")

        operations = []
        for element in elements:
            if element["tag"] == "button":
                operations.append({"action": "click", "selector": element["attributes"].get("id", "")})

        print("Executing operations...")
        execute_operations(operations, mode=args.mode)

        if args.export:
            print(f"Exporting operations to {args.export}")
            export_to_python(operations, args.export)

if __name__ == "__main__":
    main()
