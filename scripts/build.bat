echo off
echo "Building the project..."
pyinstaller^
    --onefile^
    --windowed^
    --icon "assets/images/YouTube.ico"^
    --splash "assets/images/YouTube-icon.png"^
    --name "YouTube Video Downloader"^
    --clean^
    --add-data "assets/images/*.png;assets/images/"^
    --add-data "assets/images/*.ico;assets/images/"^
    --add-data "assets/contents/*.txt;assets/contents/"^
    --add-data ".env;."^
    --add-data ".venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv;nepali_datetime/data/"^
 main.py
echo "EXE Creation Completed Successfully!"
::pyinstaller --noconfirm --onefile --windowed --icon "D:/Ajay/GitHub/YouTube-Video-Downloader/assets/images/YouTube.ico"^
:: --name "YouTube Video Downloader" --clean --log-level "DEBUG" --splash "D:/Ajay/GitHub/YouTube-Video-Downloader/assets/images/YouTube-icon.png"^
:: --add-data ".env;." --add-data "D:/Ajay/GitHub/YouTube-Video-Downloader/assets;assets/"^
:: --add-data "D:/Ajay/GitHub/YouTube-Video-Downloader/.venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv;nepali_datetime/data"^
::  "D:/Ajay/GitHub/YouTube-Video-Downloader/main.py"