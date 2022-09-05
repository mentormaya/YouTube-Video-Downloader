echo off
echo "Building the project..."
pyinstaller --onefile --windowed --icon "assets/images/YouTube.ico" --splash "assets/images/YouTube-icon.png" --name "YouTube Video Downloader" --clean --add-data "assets/*.*;assets/" --add-data ".env;." --add-data ".venv/Lib/site-packages/nepali_datetime/data/calendar_bs.csv;nepali_datetime/data/" main.py
echo "Exe created Successfully! 💖"