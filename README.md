# Web Scraper

This interactive Python program allows users to scrape textual content from a given URL and display it directly in the terminal with formatting such as **bold**, *italic*, clickable underlined links, and colored output.  
The scraper validates URLs, handles HTTP errors gracefully, and lets users specify how many lines of text to display from a webpage.

## Features
- URL validation with clear error messages  
- Fetches and parses HTML content via `requests` and `BeautifulSoup`  
- Renders text in the terminal using ANSI escape codes (bold, italic, underline, color)  
- Graceful handling of connection, timeout, and HTTP exceptions  
- Interactive user input and adjustable output length  

## Functions Overview
- **`is_valid_url(url: str) -> bool`**  
  Validates that a string is a properly formatted URL with a scheme and domain.

- **`render_with_styles(element)`**  
  Recursively renders HTML tags (`<b>`, `<i>`, `<a>`) into styled terminal text, including clickable links.

- **`main()`**  
  Runs the full program — prompting the user for a URL, validating it, fetching data, and displaying styled text.


## To Run
1. **Ensure Python 3 is installed on your system.**
2. **Clone this repository:**
   ```bash
   git clone https://github.com/YourUsername/web_scraper_terminal.git
   cd web_scraper_terminal
