from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


# website = requests.get("https://example.com")
# print(website.status_code)

# # Extracting text
# response = website.text
# # print(response)

# Generalising website url

# def webExtractor(url):
#     try:

#         website = requests.get(url)
#         website.raise_for_status()
#         soup = BeautifulSoup(website.text, 'html.parser')
#         for tag in soup(['script', 'style', 'title']):
#             tag.decompose()
#         text = soup.get_text(separator = "\n", strip = True)
#         print(f"\n{text}\n")

#     # Handling other status code
#     except requests.exceptions.RequestException as e:
#         print(f"Request error: \n{e}\n")


# url = input("Enter the url for website for text extraction: ")
# webExtractor(url)

def webExtractor(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Wait for React to render
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for tag in soup(['script', 'title', 'style']):
        tag.decompose()

    text = soup.get_text(separator = '\n', strip = True)
    print(text)

    driver.quit()

url = input("Enter the url: ")
webExtractor(url)