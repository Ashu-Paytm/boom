from flask import Flask, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Path to the directory where the MP3 files are stored
MP3_DIRECTORY = "npo3.mp3"

@app.route("/download/<filename>", methods=["GET"])
def download_mp3(filename):
    try:
        # Construct the full path to the file
        file_path = os.path.join(MP3_DIRECTORY, filename)

        # Check if the file exists
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found."}), 404

        # Send the file to the client
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the MP3 directory exists
    os.makedirs(MP3_DIRECTORY, exist_ok=True)

    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
