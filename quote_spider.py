import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.doubao.com/',
    'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
}

results = [
    ["名言", "作者", "标签"],
]

response = requests.get('https://quotes.toscrape.com/', headers=headers)
soup = BeautifulSoup(response.text, "lxml")

# find_all方法返回所有符合条件的标签
quote_data = soup.find_all(name='div', attrs={'class': 'quote'})

for item in quote_data:
    # find方法返回第一个符合条件的标签
    quote = item.find("span", attrs={'class': 'text', 'itemprop': 'text'}).get_text(strip=True)

    # string属性获取标签内的文本内容, 但要注意: 如果标签内有子标签, 则返回None
    author = item.small.string

    # select方法, 传入相应的CSS选择器, 返回所有符合条件的标签
    tag = []
    for tag_item in item.select('a[class="tag"]'):
        tag.append(tag_item.get_text(strip=True))
    tag_str = "-".join(tag)

    data = [quote, author, tag_str]
    results.append(data)

with open("./名言.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)










