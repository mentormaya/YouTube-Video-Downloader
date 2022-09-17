# /usr/bin/python3
import re
import m3u8
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import m3u8_To_MP4 as mp4


m3u8_pattern = r'sources: \[{file:\"(.+)\"}\]'

fname_pattern = r'<title>(.+)</title>'

def _get_m3u8_obj_by_uri(m3u8_uri):
        try:
            m3u8_obj = m3u8.load(uri=m3u8_uri)
        except Exception as exc:
            print('failed to load m3u8 file,reason is {}'.format(exc))
            raise Exception('FAILED TO LOAD M3U8 FILE!')

        return m3u8_obj

def download(m3u8_file, fname = 'Film', dir = 'C:\Movies'):
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
        mp4_file_dir = dir, 
        mp4_file_name = f'{fname}.mp4'
    )

URL = 'https://prmovies.com/episode/the-good-doctor-season-1-episode-1/'

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

data = {}

s = requests.Session()

w = s.get(URL, headers=HEADERS)

w_soup = BeautifulSoup(w.text, 'html.parser')

data['fname'] = re.search(fname_pattern, w.text).groups()[0]
data['fname'] = re.sub("Full", "", data['fname'])
data['fname'] = re.sub("Movie", "", data['fname'])
data['fname'] = re.sub("Watch Online", "", data['fname'])
data['fname'] = re.sub("on prmovies", "", data['fname']).strip()

data['iframes'] = w_soup.find_all('iframe')

data['if_links'] = [iframe['src'] for iframe in data['iframes']]

for index, link in enumerate(data['if_links']):
    if 'https:' not in link:
        data['if_links'][index] = 'https:' + link

r = s.get(data['if_links'][0], headers=HEADERS)


data['m3u8_file'] = re.search(m3u8_pattern, r.text).groups()[0]

pprint(data)

download(m3u8_file=data['m3u8_file'], fname=data['fname'], dir='F:\Movies\The Good Doctor')