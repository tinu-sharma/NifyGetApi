from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "Video URL is required"}), 400
    
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        download_link = stream.url  # Temporary YouTube link
        return jsonify({"download_url": download_link})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
  
