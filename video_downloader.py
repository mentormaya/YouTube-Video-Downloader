# /usr/bin/python3

import requests
from pprint import pprint

URL = 'https://prmovies.com/the-batman-2022-hindi-dubbed-Watch-online-on-prmovies/'


s = requests.Session()

r = s.get(URL)

m3u8_file = 'https://leave.ydc1wes.me/hls2/01/00003/c9woiuznhaa2_,l,o,.urlset/master.m3u8?t=4Hcb__PV33j1oMqazeo6WyKdJ3weVcANfOntcnXZl5c&s=1663127503&e=21600&f=16229&i=0.0&sp=0'

r = s.get(m3u8_file)

pprint(r.text)