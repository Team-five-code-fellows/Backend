# find all links on the page
# check that links are internal to wikipedia
# remove duplicate links
# format links into numbered list of page titles
import requests
import re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/python_(programming_language)"

soup = BeautifulSoup


def get_links(url):
    response = requests.get(url)
    res_soup = soup(response.content, "html.parser")
    # for nav in res_soup("nav"):
    #     nav.remove()
    # for footer in res_soup("footer"):
    #     footer.()
    # for script in res_soup("script"):
    #     script.remove()
    list_links = res_soup.find("div", {"id": "bodyContent"})
    parsed_links = []
    print(list_links)
    for item in list_links:
        if "/wiki/" in str(item) and "language" not in str(item):
            parsed_links.append(item.text)
    print(parsed_links)


get_links(url)
