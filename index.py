from flask import Flask, request, jsonify
from flask_cors import CORS
from sync_playlist import sync_playlist 

app = Flask(__name__)
CORS(app)

@app.route('/sync', methods=['POST'])
def sync_music():
    try:
        data = request.json
        playlist_url = data.get("playlist_url")

        if not playlist_url:
            return jsonify({"error": "No playlist URL provided"}), 400

        result = sync_playlist(playlist_url)

        return jsonify({"message": "Sync completed", "output": result})

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
