from flask import Flask, jsonify
import os

app = Flask(__name__)

# Endpoint 1
@app.route('/')
def beranda():
    return jsonify({
        'pesan': 'Aplikasi Kehadiran Mahasiswa',
        'status': 'aktif',
        'versi': '1.0.0'
    })

# Endpoint 2
@app.route('/kesehatan')
def cek_kesehatan():
    return jsonify({
        'status': 'sehat'
    })

# Endpoint 3
@app.route('/mahasiswa')
def mahasiswa():
    data = [
        {
            "nama": "Budi",
            "nim": "1301220001"
        },
        {
            "nama": "Siti",
            "nim": "1301220002"
        }
    ]

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)