# /usr/bin/python3

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

# URL = 'https://prmovies.com/the-batman-2022-hindi-dubbed-Watch-online-on-prmovies/'

s = requests.Session()

# r = s.get(URL)

fname = 'Film'

m3u8_file = 'https://rhyaat.ydc1wes.me/hls2/01/00003/7lcmarg8yby8_,l,h,.urlset/master.m3u8?t=Hm8QQbzl1z2xJexEHrAjXxha39Llkw8rteI4oNSPdls&s=1663213290&e=21600&f=18552&i=0.0&sp=0'

# download(m3u8_file=m3u8_file)