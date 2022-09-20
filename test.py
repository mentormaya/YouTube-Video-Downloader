# 513834386a6652764e4d3241 7c7c 6d35636f643563376f6c6536 7c7c 4f614d593335314674774a6a 7c7c 73747265616d7362
# 694b7864377934576b567278 7c7c 6d35636f643563376f6c6536 7c7c 43657139596b64494441564b 7c7c 73747265616d7362
# 545a487965424e346e566b72 7c7c 6d35636f643563376f6c6536 7c7c 6a614f487578676472773973 7c7c 73747265616d7362
# 356c75445569787967553868 7c7c 6d35636f643563376f6c6536 7c7c 415731736b484a597769576b 7c7c 73747265616d7362

# 324152664b3073304563435a 7c7c 6d35636f643563376f6c6536 7c7c 7a42314c5630667068764841 7c7c 73747265616d7362
# 6650394465783035726e3567 7c7c 6d35636f643563376f6c6536 7c7c 4b417a735a42525545596f42 7c7c 73747265616d7362
import re
import random
import json
from pprint import pprint
from requests import Session

s = Session()

url = 'https://sbplay2.xyz/e/m5cod5c7ole6?caption_1=https://msubload.com/sub/the-good-doctor-season-1-episode-3-mount-rushmore/the-good-doctor-season-1-episode-3-mount-rushmore.vtt&sub_1=English'

domain_pattern = r"(https?://[A-Za-z._\-0-9]+)"

def get_domain(url):
    return re.search(domain_pattern, url).groups()[0]

M3U8_LINK_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en',
    'cookie': 'lang=1',
    'dnt': '1',
    'referer': url,
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'watchsb': 'sbstream',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}


def hex_to_decimal(hex):
    decimals = []
    for value in hex.split(','):
        decimals.append(int(value, 16))
    pprint(f'Decimals for {hex} is {decimals}')
    return decimals

def get_random_id(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    id = ''.join(random.choice(chars) for i in range(length))
    return id

def generate_link(path):
    return get_domain(url) + path

def generate_url():
    m5cod5c7ole6 = '6d35636f643563376f6c6536'
    streamsb = '73747265616d7362'
    sep = '7c7c'
    return generate_link('/sources48/') + sep.join([get_random_id(24), m5cod5c7ole6, get_random_id(24), streamsb])

link = generate_url()

print(f'getting the m3u8 link {link}')
m3u8_link = s.get(link, headers=M3U8_LINK_HEADERS)

print(f'writing the m3u8 link to file')
with open('stream_data.json', 'w') as sjf:
    sjf.write(m3u8_link.text)

m3u8_link = json.loads(m3u8_link.text)

m3u8_url = m3u8_link['stream_data']['file']

M3U8_FILE_HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en',
    'connection': 'keep-alive',
    'dnt': '1',
    'host': get_domain(m3u8_url).split('//')[1],
    'origin': get_domain(url),
    'referer': get_domain(url) + "/",
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

print(f'getting the m3u8 file from {m3u8_url}')
m3u8_data = s.get(m3u8_url, headers=M3U8_FILE_HEADERS)

pprint(m3u8_data.text)