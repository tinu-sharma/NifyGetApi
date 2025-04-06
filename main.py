import os
from flask import Flask, request, jsonify, render_template
from pytube import YouTube
import instaloader
from facebook_scraper import get_posts

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get("url")

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        # Handle YouTube Shorts link
        if "youtube.com/shorts/" in url:
            url = url.replace("youtube.com/shorts/", "youtube.com/watch?v=")

        if "youtube.com" in url or "youtu.be" in url:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            return jsonify({"platform": "YouTube", "download_url": stream.url})

        elif "instagram.com" in url:
            loader = instaloader.Instaloader()
            shortcode = url.strip("/").split("/")[-1]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            return jsonify({"platform": "Instagram", "download_url": post.video_url})

        elif "facebook.com" in url:
            for post in get_posts(post_urls=[url]):
                if "video" in post:
                    return jsonify({"platform": "Facebook", "download_url": post["video"]})
            return jsonify({"error": "No video found."})

        else:
            return jsonify({"error": "Unsupported URL"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
            
