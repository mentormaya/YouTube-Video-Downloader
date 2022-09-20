import re
from pprint import pprint
from requests import Session

s = Session()

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept': '-encoding: gzip, deflate, br',
    'accept': '-language: en',
    'cookie': 'domain-alert=1',
    'dnt': '1',
    'referer': 'https://prmovies.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

url = 'https://sbplay2.xyz/e/m5cod5c7ole6?caption_1=https://msubload.com/sub/the-good-doctor-season-1-episode-2-mount-rushmore/the-good-doctor-season-1-episode-2-mount-rushmore.vtt&sub_1=English'

domain_pattern = r"(^https?://[A-Za-z_0-9-]+\.[A-Za-z_0-9-]+)"

js_url = re.search(domain_pattern, url).groups()[0] + "/js/app.min.3.js?v=2"

content = s.get(url = js_url, headers = HEADERS)

with open("latest_app.js", 'w') as f:
    f.write(content.text)

word_list_pattern = r'var\s?\w+\s?=(\[.*?\]);'

word_list = re.search(word_list_pattern, content.text).groups()[0].strip("']['")
word_list = word_list.split("','")

total_words = len(word_list)

print(total_words)