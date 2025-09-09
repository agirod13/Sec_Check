import requests
import time
import sys
import os
os.system("")  # Enables ANSI escape codes on Windows

from urllib.parse import urljoin

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
        elif response.status_code == 404:
            print(f"\033[91m[-] No security.txt found at {security_url}\033[0m")
        else:
            print(f"\033[91m[!] Received unexpected status code {response.status_code} from {security_url}\033[0m")
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

# Example usage
if __name__ == "__main__":
    animate_banner(banner_lines)
    domain_input = input("Please enter a domain (e.g., example.com): ").strip()
    check_security_txt(domain_input)