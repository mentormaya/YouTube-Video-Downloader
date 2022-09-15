# /usr/bin/python3

import requests
from pprint import pprint
import m3u8_To_MP4 as mp4

URL = 'https://prmovies.com/the-batman-2022-hindi-dubbed-Watch-online-on-prmovies/'


s = requests.Session()

r = s.get(URL)

pprint(r.text)

# m3u8_file = 'https://leave.ydc1wes.me/hls2/01/00003/c9woiuznhaa2_,l,o,.urlset/master.m3u8?t=4Hcb__PV33j1oMqazeo6WyKdJ3weVcANfOntcnXZl5c&s=1663127503&e=21600&f=16229&i=0.0&sp=0'

# print('Get m3u8 file...')

customized_http_header=dict()
customized_http_header['Referer'] = 'https://speedostream.com/'

print("Downloaing...")

# r = s.get(m3u8_file)

# pprint(r.text)

# playlist = mp4.multithread_download(m3u8_file,customized_http_header=customized_http_header)

# pprint(r.__dict__)