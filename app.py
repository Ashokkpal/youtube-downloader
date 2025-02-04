from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get("url")
    
    if not video_url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_path = os.path.join(DOWNLOAD_FOLDER, f"{info['title']}.{info['ext']}")
        
        return send_file(file_path, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
