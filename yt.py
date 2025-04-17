#!/bin/env python3 python

from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def main():

    #Getting the path
    path = input("\nEnter download path: \n")
    if not os.path.exists(path):
        os.makedirs(path)

    #Getting the video link
    url = input("\nEnter video url:\n")
    yt = YouTube(url, on_progress_callback=on_progress)
    video_title = yt.title
    print("\nThe video title is: " + video_title + ".\n")

    response = input("\nVideo or audio only? (v/a): \n")
    if response == "v":
        yt = YouTube(url, on_progress_callback=on_progress)
        yd = yt.streams.get_highest_resolution()
        yd.download(output_path=path)
    elif response == "a":
        yt = YouTube(url, on_progress_callback=on_progress)
        yd = yt.streams.get_audio_only()
        yd.download(output_path=path)
    else:
        print("\nInvalid option. Please enter 'v' for video or 'a' for audio.\n")

if __name__ == "__main__":
    main()
