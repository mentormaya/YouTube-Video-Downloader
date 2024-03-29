import re
import random
import json
from pprint import pprint
from requests import Session

s = Session()

streaming_url = 'https://sbplay2.xyz/e/m5cod5c7ole6?caption_1=https://msubload.com/sub/the-good-doctor-season-1-episode-2-mount-rushmore/the-good-doctor-season-1-episode-2-mount-rushmore.vtt&sub_1=English'

domain_pattern = r"(https?://[A-Za-z._\-0-9]+)"

def get_domain(url):
    return re.search(domain_pattern, url).groups()[0]

M3U8_LINK_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'cookie': 'lang=1',
    'dnt': '1',
    'referer': streaming_url,
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
    return get_domain(streaming_url) + path

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
    'accept-language': 'en',
    'connection': 'keep-alive',
    'dnt': '1',
    'host': get_domain(m3u8_url).split('//')[1],
    'origin': get_domain(streaming_url),
    'referer': get_domain(streaming_url) + "/",
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

with open('download.m3u8', 'w') as mf:
    mf.write(m3u8_data.text)

print(f'M3U8 file saved!')