import requests
from bs4 import BeautifulSoup

# Define URL
url = input("What website do you want to scrape? ") #try and except to make sure it is a url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

# How many lines
num_lines = int(input("The number of lines please. "))



response = requests.get(url, headers=headers)  #getting access to the url

if response.status_code == 200:
    htmlText = response.text
    soup = BeautifulSoup(htmlText, 'html.parser')
    paragraphs = soup.find_all('p')

    for line in paragraphs[:num_lines]:
        print(line.text.strip())
else:
    print(f'Failed to retrieve the webpage: {response.status_code}') #see if you can do something that says 404 is equal to a Not Found Error
