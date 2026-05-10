from flask import Flask, jsonify
import os

app = Flask(__name__)

env = os.getenv("APP_ENV", "development")

@app.route('/')
def home():
    return f"""
    <html>
    <head>
        <title>Aplikasi Kehadiran Mahasiswa</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }}

            .card {{
                background: white;
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #2c3e50;
            }}

            p {{
                font-size: 18px;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Aplikasi Kehadiran Mahasiswa</h1>

            <p>Status:
                <span class="status">Aktif</span>
            </p>

            <p>Versi: 1.0.0</p>

            <p>Environment: {env}</p>

            <hr>

            <h3>Endpoint API</h3>

            <p>/health</p>
            <p>/mahasiswa</p>
        </div>
    </body>
    </html>
    """

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