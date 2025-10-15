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
                capture_screenshot(playwright, security_url, project_folder)
            return security_url
        elif response.status_code == 404:
            print(f"\033[91m[-] No security.txt found at {security_url}\033[0m")
            print("Still taking screenshot of the page...")
            with sync_playwright() as playwright:
                capture_screenshot(playwright, security_url, project_folder)
        else:
            print(f"\033[91m[!] Received unexpected status code {response.status_code} from {security_url}\033[0m")
            print("Still taking screenshot of the page...")
            with sync_playwright() as playwright:
                capture_screenshot(playwright, security_url, project_folder)
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

def capture_screenshot(playwright,security_url, project_folder):
    domain = domain_input.split(".")[0].title()
    filename = "Security.txt_Screenshot.png"
    filepath = os.path.join(project_folder, filename)
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(security_url)
    page.wait_for_load_state("networkidle")
    page.screenshot(path = filepath, full_page=True)
    browser.close()
    print(f"\033[92m[+] Screenshot saved as: {filepath}\033[0m")

def create_project_folder(name):
    folder_name = name.strip().replace(" ", "_")  # Clean up name
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

if __name__ == "__main__":
    animate_banner(banner_lines)
    project_name = input("Please enter project name: ").strip()
    print(f"\033[93m[~] Creating folder {project_name}...\033[0m")
    domain_input = input("Please enter a domain (e.g., example.com): ").strip()
    project_folder = create_project_folder(project_name)
    check_security_txt(domain_input)
