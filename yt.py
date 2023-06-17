from pytube import YouTube
import os

#Getting the Desktop path
path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")

#Getting the URL
yt = YouTube(input("Please enter a URL: ")).streams

#Audio or video?
answer = input("Would you like to download video (1) or audio-only (2)?: ")

def vo():
	
	#Filters and download
	yt.filter(progressive = True).order_by("resolution").desc().first().download(output_path = path)

def ao():
	
	#Filters and download
	yt.filter(only_audio = True).order_by("bitrate").desc().first().download(output_path = path)


#Main loop
if answer == "1":
	vo()
elif answer == "2":
	ao()
