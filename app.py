import requests
from bs4 import BeautifulSoup

# website = requests.get("https://example.com")
# print(website.status_code)

# # Extracting text
# response = website.text
# # print(response)

# # Parsing html
# parsed_text = BeautifulSoup(response, 'html.parser')
# for para in parsed_text:
#     print(para.get_text())

# # if website.status_code == 200:
# #     data = website.json()
# #     print(data)

# if website.status_code == 200:
#     soup = BeautifulSoup(website.text, 'html.parser')
#     for tag in soup(['script', 'style', 'title']):
#         tag.decompose()
#     text = soup.get_text(separator = "\n", strip = True)
#     print(text)

# Generalising website url

def webExtractor(url):
    try:

        website = requests.get(url)
        website.raise_for_status()
        soup = BeautifulSoup(website.text, 'html.parser')
        for tag in soup(['script', 'style', 'title']):
            tag.decompose()
        text = soup.get_text(separator = "\n", strip = True)
        print(f"\n{text}\n")

    # Handling other status code
    except requests.exceptions.RequestException as e:
        print(f"Request error: \n{e}\n")


url = input("Enter the url for website for text extraction: ")
webExtractor(url)