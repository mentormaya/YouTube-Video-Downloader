echo off
echo "Building the project..."
pyinstaller --onefile --windowed --icon "assets/images/YouTube.ico" --name "YouTube Video Downloader" --clean --resource "assets" --add-data ".env;." --add-data ".venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv;nepali_datetime/data/" main.py