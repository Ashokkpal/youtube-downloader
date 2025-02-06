# 🎬 YouTube Video Downloader

🚀 **Download YouTube videos easily in various formats**

![YouTube Downloader](https://raw.githubusercontent.com/Ashokkpal/youtube-downloader/main/assets/banner.png)  
_A lightweight, fast, and easy-to-use YouTube video downloader built with Flask & yt-dlp._

---

## 🌟 Features
✅ Download YouTube videos in **HD quality**  
✅ Supports **MP4, MP3, and other formats**  
✅ **Bypass restrictions** using `--cookies-from-browser` (Local use) or `cookies.txt` (Render/VPS)  
✅ **Easy-to-use API** – Just paste the video link & download!  
✅ **Fast & Secure** – No ads, no tracking!  

---

## 🚀 Live Demo
🔗 **Try it here** 👉 [YouTube Downloader](https://ashokkpal.github.io/youtube-downloader/)

---

## 🛠️ Installation & Setup

### 🔥 1. Clone the Repository
```bash
git clone https://github.com/Ashokkpal/youtube-downloader.git
cd youtube-downloader
```

### 📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🖥️ 3. Run the Flask Server
#### 🔹 Local Machine (With `--cookies-from-browser`)
```bash
python app.py
```
#### 🔹 VPS / Render (Using `cookies.txt`)
1. **Extract Cookies from Chrome:** [Get cookies.txt Extension](https://chrome.google.com/webstore/detail/get-cookiestxt/lgmpobddfdigpfojgnmgamkpejpmpkdo)
2. **Upload `cookies.txt` to the project folder**
3. Run the server:
```bash
python app.py
```

---

## 🔥 API Usage
### 🎥 **Download a Video**
```http
GET /download?url=YOUTUBE_VIDEO_URL
```
#### ✅ **Example**:
```http
GET https://your-app.onrender.com/download?url=https://www.youtube.com/watch?v=VIDEO_ID
```
#### 🔥 **Response:**
```json
{
  "success": "Download complete",
  "file": "downloads/sample_video.mp4"
}
```

---

## 🌈 Frontend UI Preview
![UI Preview](https://raw.githubusercontent.com/Ashokkpal/youtube-downloader/main/assets/ui-preview.png)

---

## 🚀 Deployment (Render)
1. **Create a Render Web Service**: [Render Dashboard](https://dashboard.render.com/web/new?newUser=true)
2. **Connect GitHub Repo**: Select `youtube-downloader`
3. **Set Build Command**: `pip install -r requirements.txt`
4. **Set Start Command**: `python app.py`
5. **Deploy & Enjoy!** 🎉

---

## 🤝 Contributing
Contributions are **welcome & appreciated!** 🚀
1. **Fork the repo**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Make your changes & commit** (`git commit -m "Added new feature"`)
4. **Push & open a pull request** (`git push origin feature-branch`)

---

## 📄 License
📝 This project is licensed under the [**MIT License**](https://github.com/Ashokkpal/youtube-downloader/blob/main/License)

---

## 🎯 Author
👤 **Ashok Pal**  
🔗 **GitHub**: [Ashokkpal](https://github.com/Ashokkpal)  
🔗 **Portfolio**: [ashokkpal.github.io/](https://ashokkpal.github.io/)  
💌 **Contact**: [ashokpal2094@gmail.com](mailto:ashokpal2094@gmail.com)

---

⭐ **If you like this project, give it a star!** ⭐

