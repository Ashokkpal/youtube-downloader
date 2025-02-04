from pytube import YouTube
import os

def download_video(youtube_url, save_path="Downloads"):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")
        stream.download(output_path=save_path)
        print(f"Downloaded successfully to {save_path}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("YouTube Video Downloader by Ashok Pal")
    print("GitHub: https://github.com/Ashokkpal")
    url = input("Enter YouTube Video URL: ")
    download_video(url, save_path=os.path.expanduser("~/Downloads"))
