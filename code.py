# youtube_downloader.py

# Install pytube first: pip install pytube
from pytube import YouTube
import sys
import os

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"\n Title: {yt.title}")
        print("Downloading video...")

        stream = yt.streams.get_highest_resolution()
        stream.download()

        print(f" Download complete! Saved as: {stream.default_filename}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If user passed link as command argument
        link = sys.argv[1]
    else:
        # Ask in terminal
        link = input("Paste YouTube URL: ").strip()

    if link:
        download_video(link)
    else:
        print(" No URL provided.")
