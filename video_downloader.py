# /usr/bin/python3

import requests
from pprint import pprint

URL = 'https://cms.ntc.net.np'

s = requests.Session()

r = s.get(URL)

pprint(r.__dict__)