# easy-5-upload-avatar/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD = "/tmp/uploads"
os.makedirs(UPLOAD, exist_ok=True)

FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    # BUG: only filename check
    if not f.filename.lower().endswith(".png"):
        return jsonify({"error":"only png"}),400

    path = os.path.join(UPLOAD, f.filename)
    f.save(path)

    with open(path,"rb") as fd:
        if b"AVATAR_ADMIN" in fd.read():
            return jsonify({"flag":FLAG})

    return jsonify({"status":"uploaded"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
