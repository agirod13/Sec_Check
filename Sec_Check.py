import requests
import time
import sys
import os

os.system("")  # Enables ANSI escape codes on Windows

from urllib.parse import urljoin
from playwright.sync_api import sync_playwright

banner_lines = [
"""
███████╗███████╗ ██████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██╔════╝██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
███████╗█████╗  ██║         ██║     ███████║█████╗  ██║     █████╔╝
╚════██║██╔══╝  ██║         ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗
███████║███████╗╚██████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝╚══════╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝                                                                  
                                                
               >> Sec Check <<
            >>> by Anthony Girod <<<
"""
]

def check_security_txt(domain):
    # Ensures domain starts with http or https
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain

    # Constructs the URL for the security.txt file
    security_url = urljoin(domain, '/.well-known/security.txt')

    try:
        response = requests.get(security_url, timeout=10)
        if response.status_code == 200:
            print(f"\033[92m[+] Found security.txt at {security_url}\033[0m")
            print("\n--- Contents ---\n")
            print(response.text)
            with sync_playwright() as playwright:
                capture_screenshot(playwright,security_url)
            return security_url
        elif response.status_code == 404:
            print(f"\033[91m[-] No security.txt found at {security_url}\033[0m")
            print("Still taking screenshot of the page...")
            with sync_playwright() as playwright:
                capture_screenshot(playwright,security_url)
        else:
            print(f"\033[91m[!] Received unexpected status code {response.status_code} from {security_url}\033[0m")
            print("Still taking screenshot of the page...")
            with sync_playwright() as playwright:
                capture_screenshot(playwright,security_url)
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[!] Error connecting to {security_url}: {e}\033[0m")

def animate_banner(lines, delay=0.1):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay / 150)  # Faster per character
        print()
        time.sleep(delay)  # Pause between lines

def capture_screenshot(playwright,security_url):
    domain = domain_input.split(".")[0].title()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(security_url)
    page.screenshot(path=domain + ' Security.txt Screenshot.png', full_page=True)
    browser.close()
    print("Saving to:", os.getcwd())

# Example usage
if __name__ == "__main__":
    animate_banner(banner_lines)
    domain_input = input("Please enter a domain (e.g., example.com): ").strip()
    check_security_txt(domain_input)