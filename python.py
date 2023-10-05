import requests
from bs4 import BeautifulSoup
import json

url = 'https://velog.io/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
postings = soup.find_all("div", attrs={"class":"sc-iNGGcK fjYyoH"})


data_list = [] 

for posting in postings:
    data = {}
    data["thumbnail_url"] = posting.find("img").get("src")
    data["post_url"] = posting.find("a", class_="sc-lbhJGD bozgeq").get("href")
    data["title"] = posting.find("h4").get_text()
    data["description"] = posting.find("div", class_="description-wrapper").find("p").get_text()
    data["date"] = posting.find("div", class_="sub-info").find_all("span")[0].get_text()
    data["comment_count"] = int(posting.find("div", class_="sub-info").find_all("span")[2].get_text().split("개")[0])
    user_info = posting.find("a", class_="userinfo")
    data["author_profile_url"] = user_info.find("img").get("src")
    data["author_name"] = user_info.find("b").get_text()
    data["likes"] = int(posting.find("div", class_="likes").get_text())
    data_list.append(data)


with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)
