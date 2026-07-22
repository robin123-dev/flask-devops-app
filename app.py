from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Devops is live!",
        "version": "1.0.1",
        "timestamp": datetime.datetime.now().isoformat() 
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "uptime": "24h" 
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

