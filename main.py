"""
Web Scraper with Terminal Styling

This interactive program allows users to scrape textual content from a
given URL and display it in the terminal with basic formatting (bold,
italic, unerlined links, colored output). The scraper validates URLs,
handles HTTP errors gracefully, and allows the user to specify how many
lines of text to display from the webpage.

Features:
- URL validation
- Fetching HTML content via requests
- Rendering styled paragraphs in terminal
- Handling connection, timeout, and request exceptions
- ANSI styling for bold, italic, underline, and color

Functions:
- is_valid_url(url:str) -> bool:
    Checks if a string is a properly formatted URL with scheme and
    domain
- render_with_styles(element):
    Recursively renders HTML elements with terminal styles such as bold,
    italic, underline, and clickable links
- main():
    Runs the interactive terminal interface, prompting the user for a 
    URL, validating it, fetching the page content, and displaying styled
    text from the page
"""


import requests
from bs4 import BeautifulSoup  
from requests.exceptions import RequestException, ConnectionError, Timeout
from urllib.parse import urlparse

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

# Check if the given string is a valid URL
def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])


# Render HTML elements with terminal styles (bold, italic, links, etc.)
def render_with_styles(element):
    output = ""
    for child in element.children:
        if child.name in ["b", "strong"]:
            output += f"{BOLD}{render_with_styles(child)}{RESET}"
        elif child.name in ["i", "em"]:
            output += f"{ITALIC}{render_with_styles(child)}{RESET}"
        elif child.name == "a":  # hyperlink → clickable + blue underline
            href = child.get("href", "")
            if href.startswith("/"):  # relative Wikipedia links
                href = "https://en.wikipedia.org" + href
            text = child.get_text()
            # clickable + styled
            link_text = (
                f"\033]8;;{href}\033\\"
                f"{BLUE}{UNDERLINE}{text}{RESET}\033]8;;\033\\"
            )
            output += link_text
        elif child.name:
            output += render_with_styles(child)
        else:
            output += str(child)
    return output


# HTTP Status Code Messages
HTTP_STATUS_MESSAGES = {
    400: "Bad Request – The server could not understand the request.",
    401: "Unauthorized – Authentication is required.",
    403: "Forbidden – You do not have permission to access this resource.",
    404: "Not Found – The requested resource could not be found.",
    408: "Request Timeout – The server timed out waiting for the request.",
    429: "Too Many Requests – You have sent too many requests in short time.",
    500: "Internal Server Error – Something went wrong on the server.",
    502: "Bad Gateway – Invalid response from an upstream server.",
    503: "Service Unavailable – The server is not ready to handle request.",
    504: "Gateway Timeout – The server did not receive a timely response."
}


# To prevent a 403 error with website (make it accessible in Python)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}


# Main program
def main():
    while True:
        # ask for URL
        url = input(
            f"\n{YELLOW}Please Paste URL of Website you want to scrape: {RESET}"
                     ).strip()

        # validate URL format
        if not is_valid_url(url):
            print(
                f'\n{RED} "{url}" is an invalid URL. '
                'Please include http:// or https://' \
                f'{RESET}')
            continue
        
        # try fetching the page
        try:
            print(f"\n{YELLOW}Fetching webpage... please wait.{RESET}")
            response = requests.get(url, timeout=10, headers=headers)
            break
        except (ConnectionError, Timeout):
            print(
                f"{RED}Failed to connect to {url}. The site may be down or unreachable.\n" 
                "Please enter a new URL or try again."
                f"{RESET}")
        except RequestException as e:
            print(f"{RED}An error occurred while trying to fetch {url}: "
                  f"{e}\n Please enter a new URL or try again.{RESET}")
            
    # Number of Lines Input (5 is default)
    while True:
        user_input_lines = input(
            f"\n{YELLOW}Please enter the number of lines "
            f"(or press Enter for the default of 5): {RESET}"
              )
        if user_input_lines.strip() == "":
            num_lines = 5
            break
        try:
            num_lines = int(user_input_lines)
            break
        except ValueError:
            print(f'\n{RED}"{user_input_lines}" is an invalid answer. '
                  'Please type a number.'
                  f'{RESET}\n')

    if response.status_code == 200:
        print(f"\n{GREEN}Successfully retrieved webpage!{RESET}\n")
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")

        # print number of lines in terminal
        for idx, line in enumerate(paragraphs[:num_lines], start=1):
            print(f"{BOLD}{idx}.{RESET} {render_with_styles(line)}")
        print(f"{GREEN}Done! Displayed {num_lines} lines from {url}{RESET}\n")

    else:
        status_code_message = HTTP_STATUS_MESSAGES.get(response.status_code, 
                                                       "Unknown error.")
        print(f"\n{RED}Failed to retrieve the webpage: Status Code "
              f"{response.status_code} – {status_code_message}{RESET}")


if __name__ == "__main__":
    main()
