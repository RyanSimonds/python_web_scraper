# Web Scraper

This interactive Python program allows users to scrape textual content from a given URL and display it directly in the terminal with formatting such as **bold**, *italic*, clickable underlined links, and colored output.  
The scraper validates URLs, handles HTTP errors gracefully, and lets users specify how many lines of text to display from a webpage.

## Features
- URL validation with clear error messages  
- Fetches and parses HTML content via `requests` and `BeautifulSoup`  
- Renders text in the terminal using ANSI escape codes (bold, italic, underline, color)  
- Graceful handling of connection, timeout, and HTTP exceptions  
- Interactive user input and adjustable output length  

## To Run
1. Ensure **Python 3.10+** is installed on your system.  
2. Clone the repository:  
   ```
   git clone https://github.com/RyanSimonds/web_scraper.git
   cd web_scraper
   ```
3. Install dependencies:  
   ```
   pip install requests beautifulsoup4
   ```
4. Run the program:  
   ```
   python main.py
   ```
5. Paste any URL when prompted, and the program will scrape and display formatted text in the terminal.

