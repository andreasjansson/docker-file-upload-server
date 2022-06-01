import os
import socket

import flask
from flask import Flask, jsonify, send_from_directory

app = Flask("upload_server")
port = int(os.getenv("PORT", "5000"))
uploads_folder = os.getenv("UPLOADS_FOLDER", "/uploads")
hostname = os.getenv("HOST", socket.gethostname())


@app.route("/", methods=["GET"])
def handle_index():
    return "OK"


@app.route("/upload", methods=["PUT"])
def handle_upload():
    f = flask.request.files["file"]
    f.save(os.path.join(uploads_folder, f.filename))
    return jsonify({"url": f"http://{hostname}:{port}/download/{f.filename}"})


@app.route("/download/<name>")
def download(name):
    return send_from_directory(uploads_folder, name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
