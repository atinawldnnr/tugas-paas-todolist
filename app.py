from flask import Flask, jsonify
import os

app = Flask(__name__)

env = os.getenv("APP_ENV", "development")

@app.route('/')
def home():
    return jsonify({
    "pesan": "Aplikasi Kehadiran Mahasiswa",
    "status": "aktif",
    "versi": "1.0.0",
    "environment": env
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "sehat"
    })

@app.route('/mahasiswa')
def mahasiswa():
    data = [
        {
            "nama": "Andi",
            "nim": "120123"
        },
        {
            "nama": "Budi",
            "nim": "120124"
        }
    ]

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)