# /usr/bin/python3

from email import header
import requests
from pprint import pprint
import m3u8
import m3u8_To_MP4 as mp4


def _get_m3u8_obj_by_uri(m3u8_uri):
        try:
            m3u8_obj = m3u8.load(uri=m3u8_uri)
        except Exception as exc:
            print('failed to load m3u8 file,reason is {}'.format(exc))
            raise Exception('FAILED TO LOAD M3U8 FILE!')

        return m3u8_obj

def download(m3u8_file):
    customized_http_header=dict()

    customized_http_header['Referer'] = 'https://speedostream.com/'

    print('Getting m3u8 file...')

    m3u8_obj = _get_m3u8_obj_by_uri(m3u8_file)

    playlists = m3u8_obj.data['playlists']

    bandwidth = 0

    stream = {}

    for playlist in playlists:
        if bandwidth < playlist['stream_info']['bandwidth']:
            stream = playlist['stream_info']
            stream['url'] = playlist['uri']

    print(f'Selected Best Stream: {stream["resolution"]} ({stream["frame_rate"]} fps)')

    print("Fetching Stream...")

    stream_data = _get_m3u8_obj_by_uri(stream['url'])

    files = stream_data.files

    print(f'Total {len(files)} segments found!')

    mp4.multithread_download(
        stream['url'], customized_http_header=customized_http_header, 
        mp4_file_dir='./Downloads/', 
        mp4_file_name=f'{fname}.mp4'
    )

URL = 'https://prmovies.com/the-batman-2022-hindi-dubbed-Watch-online-on-prmovies/'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept': '-encoding: gzip, deflate, br',
    'accept': '-language: en',
    'cookie': ': domain-alert=1',
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


s = requests.Session()

# r = s.get(URL, headers=HEADERS)

r = s.get("https://speedostream.com/embed-uq5bejn8cnxs.html")

print(r.content)

fname = 'Film'

payload = {'some': 'data'}

m3u8_file = 'https://rhyaat.ydc1wes.me/hls2/01/00003/7lcmarg8yby8_,l,h,.urlset/master.m3u8?t=Hm8QQbzl1z2xJexEHrAjXxha39Llkw8rteI4oNSPdls&s=1663213290&e=21600&f=18552&i=0.0&sp=0'

# download(m3u8_file=m3u8_file)