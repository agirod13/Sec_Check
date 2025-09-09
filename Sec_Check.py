import requests
from urllib.parse import urljoin

def check_security_txt(domain):
    # Ensure domain starts with http or https
    if not domain.startswith(('http://', 'https://')):
        domain = 'https://' + domain

    # Construct the URL for the security.txt file
    security_url = urljoin(domain, '/.well-known/security.txt')

    try:
        response = requests.get(security_url, timeout=10)
        if response.status_code == 200:
            print(f"[+] Found security.txt at {security_url}")
            print("\n--- Contents ---\n")
            print(response.text)
        elif response.status_code == 404:
            print(f"[-] No security.txt found at {security_url}")
        else:
            print(f"[!] Received unexpected status code {response.status_code} from {security_url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {security_url}: {e}")

# Example usage
if __name__ == "__main__":
    domain_input = input("Enter a domain (e.g., example.com): ").strip()
    check_security_txt(domain_input)