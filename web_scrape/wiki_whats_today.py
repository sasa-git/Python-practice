import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://ja.wikipedia.org/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

today = soup.find("div", attrs={"id": "mf-itn"})
entries = today.find_all("li")

today_list = []
# enumerate()でリスト[a,b,c]にインデックス番号をつけて取り出す関数[[0, a],[1, b],[2,c]]みたいな
for i, entry in enumerate(entries):
    match = re.findall("(（.*?）)", entry.get_text())
    if match:
        today_list.append([i+1, entry.get_text(), match[-1]])
    else:
        today_list.append([i+1, entry.get_text()])
# with open("output.csv", "w", encoding="UTF-8") as file:
#     writer = csv.writer(file, lineterminator="\n")
#     writer.writerows(today_list)

for item in today_list:
    print(item)