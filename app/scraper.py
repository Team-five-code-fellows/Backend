# find all links on the page
# check that links are internal to wikipedia
# remove duplicate links
# format links into numbered list of page titles
import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup


def get_links(url):
    response = requests.get(url)
    res_soup = soup(response.content, "html.parser")
    body_content = res_soup.find("div", {"id": "bodyContent"})
    list_links = body_content.findAll("a")
    parsed_links = {}


    for item in list_links:
      

      if "/wiki/" in str(item) and "/wiki/Category" not in str(item) and '/wiki/Help' not in str(item) and 'class=' not in str(item):
          value = str(item).split(" ")[1]
          parsed_links.update({item.text:value[6:-1]}) 
    return parsed_links



