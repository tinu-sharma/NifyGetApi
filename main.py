from flask import Flask, render_template  # सबसे पहले इम्पोर्ट्स लिखें

app = Flask(__name__)  # Flask ऐप को इनिशियलाइज़ करें

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html लोड करें

if __name__ == "__main__":
    app.run(debug=True)  # ऐप रन करें
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
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        return stream.url
    except Exception as e:
        return str(e)

def download_instagram(url):
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        return post.video_url
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

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        if "youtube.com" in url:
            download_url = download_youtube(url)
        elif "instagram.com" in url:
            download_url = download_instagram(url)
        elif "facebook.com" in url:
            download_url = download_facebook(url)
        else:
            return jsonify({"error": "Unsupported URL"}), 400

        return jsonify({"download_url": download_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True
