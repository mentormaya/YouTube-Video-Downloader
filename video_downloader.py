# /usr/bin/python3

import requests
from pprint import pprint
import m3u8

def _get_m3u8_obj_by_uri(m3u8_uri):
        try:
            m3u8_obj = m3u8.load(uri=m3u8_uri)
        except Exception as exc:
            pprint('failed to load m3u8 file,reason is {}'.format(exc))
            raise Exception('FAILED TO LOAD M3U8 FILE!')

        return m3u8_obj

URL = 'https://prmovies.com/the-batman-2022-hindi-dubbed-Watch-online-on-prmovies/'

s = requests.Session()

r = s.get(URL)

m3u8_file = 'https://rhyaat.ydc1wes.me/hls2/01/00003/7lcmarg8yby8_,l,h,.urlset/master.m3u8?t=Hm8QQbzl1z2xJexEHrAjXxha39Llkw8rteI4oNSPdls&s=1663213290&e=21600&f=18552&i=0.0&sp=0'


print('Get m3u8 file...')

customized_http_header=dict()

customized_http_header['Referer'] = 'https://speedostream.com/'

print("Downloading...")

m3u8_obj = _get_m3u8_obj_by_uri(m3u8_file)

pprint(m3u8_obj.__dict__)

# r = s.get(m3u8_file)

# pprint(r.text)

# playlist = mp4.multithread_download(m3u8_file,customized_http_header=customized_http_header)

# pprint(r.__dict__)