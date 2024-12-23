from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Adewale does little magic!",
        "timestamp": int(time.time())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)