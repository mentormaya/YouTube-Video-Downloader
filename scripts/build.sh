echo off
echo "Building the project..."
pyinstaller\
    --onefile\
    --windowed\
    --icon "assets/images/YouTube.ico"\
    --splash "assets/images/YouTube-icon.png"\
    --name "YouTube Video Downloader"\
    --clean\
    --add-data "assets/images/*.png:assets/images/"\
    --add-data "assets/images/*.ico:assets/images/"\
    --add-data "assets/contents/*.txt:assets/contents/"\
    --add-data ".env:."\
    --add-data ".venv/lib/python3.10/site-packages/nepali_datetime/data/calendar_bs.csv:nepali_datetime/data/"\
 main.py
echo "EXE Creation Completed Successfully!"