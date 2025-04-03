import os
from flask import Flask, request, jsonify
from pytube import YouTube
import instaloader
from facebook_scraper import get_posts

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Video Downloader! Send a video link to get the download link."

def download_youtube(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    return stream.url

def download_instagram(url):
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        video_url = post.video_url
        return video_url
    except Exception as e:
        return str(e)

def download_facebook(url):
    try:
        for post in get_posts(post_urls=[url]):
            if "video" in post:
                return post["video"]
        return "No video found."
    except Exception as e:
        return str(e)
from flask import Flask, request, jsonify
import some_video_downloader_library  # अपने वीडियो डाउनलोड लाइब्रेरी का नाम डालें

      if "youtube.com" in url:
    print("This is a YouTube URL")
          
        elif "instagram.com" in url:
            download_url = download_instagram(url)
        elif "facebook.com" in url:
            download_url = download_facebook(url)
        else:
            return jsonify({"error": "Unsupported URL"}), 400

        return jsonify({"download_url": download_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
        
app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('videoUrl')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        download_link = some_video_downloader_library.get_download_link(url)
        return jsonify({"download_link": download_link}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        url = data.get("url")
        
