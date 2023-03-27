# /usr/bin/python3
import re
import json
import m3u8
import random
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import m3u8_To_MP4 as mp4


m3u8_pattern = r"sources: \[{file:\"(.+)\"}\]"

fname_pattern = r"<title>(.+)</title>"

domain_pattern = r"(https?://[A-Za-z._\-0-9]+)"

download_folder = "F:\Movies"

URL = input("Enter the url: ")

customized_http_header = dict()

customized_http_header["Referer"] = "https://speedostream.nl/"


def _get_m3u8_obj_by_uri(m3u8_uri, headers):
    try:
        m3u8_obj = m3u8.load(uri=m3u8_uri, headers=headers)
    except Exception as exc:
        print("failed to load m3u8 file,reason is {}".format(exc))
        raise Exception("FAILED TO LOAD M3U8 FILE!")

    return m3u8_obj


def download(m3u8_file, fname="Film", dir="C:\Movies", headers=customized_http_header):
    print("Getting m3u8 file...")

    m3u8_obj = _get_m3u8_obj_by_uri(m3u8_file, headers)

    # print(f'getting the m3u8 file from {m3u8_url}')
    # m3u8_data = s.get(m3u8_url, headers=M3U8_FILE_HEADERS)

    # with open('download.m3u8', 'w') as mf:
    #     mf.write(m3u8_data.text)

    # print(f'M3U8 file saved!')

    playlists = m3u8_obj.data["playlists"]

    bandwidth = 0

    stream = {}

    for playlist in playlists:
        if bandwidth < playlist["stream_info"]["bandwidth"]:
            stream = playlist["stream_info"]
            stream["url"] = playlist["uri"]

    print(f'Selected Best Stream: {stream["resolution"]} ({stream["frame_rate"]} fps)')

    print("Fetching Stream...")

    stream_data = _get_m3u8_obj_by_uri(stream["url"], headers)

    files = stream_data.files

    print(f"Total {len(files)} segments found!")

    mp4.multithread_download(
        stream["url"],
        customized_http_header=headers,
        mp4_file_dir=dir,
        mp4_file_name=f"{fname}.mp4",
    )


def get_domain(url):
    return re.search(domain_pattern, url).groups()[0]


def hex_to_decimal(hex):
    decimals = []
    for value in hex.split(","):
        decimals.append(int(value, 16))
    pprint(f"Decimals for {hex} is {decimals}")
    return decimals


def get_random_id(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    id = "".join(random.choice(chars) for i in range(length))
    return id


def generate_link(streaming_url, path):
    return get_domain(streaming_url) + path


def generate_url(streaming_url):
    m5cod5c7ole6 = "6d35636f643563376f6c6536"
    streamsb = "73747265616d7362"
    sep = "7c7c"
    return generate_link(streaming_url, "/sources48/") + sep.join(
        [get_random_id(24), m5cod5c7ole6, get_random_id(24), streamsb]
    )


HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en",
    "cookie": "domain-alert=1",
    "dnt": "1",
    "referer": "https://prmovies.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}

data = {}

s = requests.Session()

print("getting main page...")

w = s.get(URL, headers=HEADERS, verify=False)

w_soup = BeautifulSoup(w.text, "html.parser")

data["fname"] = re.search(fname_pattern, w.text).groups()[0]
data["fname"] = re.sub("Full", "", data["fname"]).strip()
data["fname"] = re.sub("Movie", "", data["fname"]).strip()
data["fname"] = re.sub("Watch", "", data["fname"]).strip()
data["fname"] = re.sub("Online", "", data["fname"]).strip()
data["fname"] = re.sub("online", "", data["fname"]).strip()
data["fname"] = re.sub("-", "", data["fname"]).strip()
data["fname"] = re.sub("  ", " ", data["fname"]).strip()
data["fname"] = re.sub("prmovies", "", data["fname"]).strip()
data["fname"] = re.sub("on prmovies", "", data["fname"]).strip()

print(f'Film Name extracted: {data["fname"]}')

data["iframes"] = w_soup.find_all("iframe")

data["if_links"] = [iframe["src"] for iframe in data["iframes"]]

for index, link in enumerate(data["if_links"]):
    if "https:" not in link:
        data["if_links"][index] = "https:" + link

print(f'Links extracted: {data["if_links"]}')

r = s.get(data["if_links"][0], headers=HEADERS)

if ".m3u8" in data["if_links"][0]:
    data["m3u8_file"] = re.search(m3u8_pattern, r.text).groups()[0]
    pprint(data)
    download(m3u8_file=data["m3u8_file"], fname=data["fname"], dir=download_folder)
else:
    r = s.get(data["if_links"][0], headers=HEADERS)
    print(f'Link fetched: [{data["if_links"][0]}]')
    html_file_name = data["fname"] + ".html"
    with open("html/" + html_file_name, "w") as html_file:
        html_file.write(r.text)
    print(f"Page written: {html_file_name}")
    if ".m3u8" in r.text:
        pprint("M3U8 file found!")
        data["m3u8_file"] = re.search(m3u8_pattern, r.text).groups()[0]
        pprint(data)
        download(m3u8_file=data["m3u8_file"], fname=data["fname"], dir=download_folder)
    else:
        pprint("M3U8 file not found!")
        w_soup = BeautifulSoup(r.text, "html.parser")
        links = [li.get("data-video") for li in w_soup.find_all("li")]
        print(links)
        for streaming_url in links:
            if streaming_url != "":
                r = s.get(streaming_url, headers=HEADERS, verify=False)
                # print(r.text)
                if r.status_code == 200:
                    M3U8_LINK_HEADERS = {
                        "accept": "application/json, text/plain, */*",
                        "accept-language": "en",
                        "cookie": "lang=1",
                        "dnt": "1",
                        "referer": streaming_url,
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "Windows",
                        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "watchsb": "sbstream",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                    }

                    link = generate_url(streaming_url)

                    print(f"getting the m3u8 link {link}")
                    m3u8_link = s.get(link, headers=M3U8_LINK_HEADERS)

                    print(f"writing the m3u8 link to file")
                    with open("stream_data.json", "w") as sjf:
                        sjf.write(m3u8_link.text)

                    m3u8_link = json.loads(m3u8_link.text)

                    m3u8_url = m3u8_link["stream_data"]["file"]

                    M3U8_FILE_HEADERS = {
                        "accept": "*/*",
                        "accept-language": "en",
                        "connection": "keep-alive",
                        "dnt": "1",
                        "host": get_domain(m3u8_url).split("//")[1],
                        "origin": get_domain(streaming_url),
                        "referer": get_domain(streaming_url) + "/",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "Windows",
                        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "cross-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                    }

                    download(
                        m3u8_file=m3u8_url,
                        fname=data["fname"],
                        dir=download_folder,
                        headers=M3U8_FILE_HEADERS,
                    )

                    print(f'{data["fname"]} saved successfully!')

                    break
