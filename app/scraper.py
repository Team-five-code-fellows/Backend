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
    body_content = res_soup.find("div", {"id": "bodyContent"})
    list_links = body_content.findAll("a")
    parsed_links = {}
    pattern = r'href=\"(.+)\"'

   # print(list_links)
    for item in list_links:

      
      if "/wiki/" in str(item) and "language" not in str(item):
          
          key = item.split(" ")[0]
          value = item.split(" ")[1]
          parsed_links.update({key:value}) 
           # print(re.match(pattern,str(item)))
      print(parsed_links)


get_links(url)
