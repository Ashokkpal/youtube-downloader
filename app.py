from flask import Flask, request, send_file, render_template
from pytube import YouTube
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_video():
    try:
        youtube_url = request.form["url"]
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        video_path = os.path.join(DOWNLOAD_FOLDER, yt.title + ".mp4")
        stream.download(output_path=DOWNLOAD_FOLDER, filename=yt.title + ".mp4")
        
        return send_file(video_path, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
