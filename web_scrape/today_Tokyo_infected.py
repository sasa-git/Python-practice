import requests
from bs4 import BeautifulSoup
import re
import datetime

url = "https://news.tbs.co.jp/index.html"

def main():
    dt_now = datetime.datetime.now()
    fmt_time = dt_now.strftime("%Y年%m月%d日%H:%M")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    today = soup.find("div", attrs={"class": "cp-newsLv1"})

    entry = today.find("div", attrs={"class": "ls-title"})
    match = re.findall("に(.*)人感染", entry.string)
    if match:
        infected_num = int(match[0])
        print(f"{fmt_time}・・・ 今日の都内感染者数{infected_num}人かー")
    else:
        print(f"{fmt_time}・・・ 今は感染者のニュースは出てないよ！")

if __name__ == "__main__":
    main()