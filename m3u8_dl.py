import m3u8_To_MP4 as mp4

download_folder = "/Users/ajaysingh/YouTube Videos"

if __name__ == '__main__':
    m3u8_url = input("Please Enter the M3U8 URL: ")
    fname = input("Enter the title of movie: ")
    # 1. Download videos from uri.
    mp4.multithread_download(m3u8_url, 
        mp4_file_dir = download_folder, 
        mp4_file_name = f'{fname}.mp4')