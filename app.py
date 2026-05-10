from flask import Flask
import os

app = Flask(__name__)

env = os.getenv("APP_ENV", "development")

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="id">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Aplikasi Kehadiran Mahasiswa</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

        <style>
            body {{
                background: linear-gradient(to right, #141e30, #243b55);
                min-height: 100vh;
                color: white;
                font-family: Arial, sans-serif;
            }}

            .main-card {{
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
                animation: fadeIn 1s ease;
            }}

            .title {{
                font-weight: bold;
                font-size: 40px;
            }}

            .subtitle {{
                color: #dfe6e9;
            }}

            .endpoint-btn {{
                margin: 10px;
                transition: 0.3s;
            }}

            .endpoint-btn:hover {{
                transform: scale(1.05);
            }}

            table {{
                margin-top: 20px;
            }}

            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}

                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
        </style>
    </head>

    <body>

        <div class="container d-flex justify-content-center align-items-center min-vh-100">

            <div class="main-card text-center w-100">

                <h1 class="title">
                    📚 Aplikasi Kehadiran Mahasiswa
                </h1>

                <p class="subtitle">
                    Deployment Flask di Heroku
                </p>

                <hr class="border-light">

                <div class="row text-center mt-4">

                    <div class="col-md-4">
                        <div class="card bg-dark text-white shadow">
                            <div class="card-body">
                                <h5>Status</h5>
                                <p class="text-success fw-bold">
                                    Aktif
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card bg-dark text-white shadow">
                            <div class="card-body">
                                <h5>Versi</h5>
                                <p>1.0.0</p>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card bg-dark text-white shadow">
                            <div class="card-body">
                                <h5>Environment</h5>
                                <p>{env}</p>
                            </div>
                        </div>
                    </div>

                </div>

                <h3 class="mt-5">
                    👨‍🎓 Data Mahasiswa
                </h3>

                <table class="table table-dark table-striped table-hover mt-3">
                    <thead>
                        <tr>
                            <th>No</th>
                            <th>Nama</th>
                            <th>NIM</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Andi</td>
                            <td>120123</td>
                        </tr>

                        <tr>
                            <td>2</td>
                            <td>Budi</td>
                            <td>120124</td>
                        </tr>
                    </tbody>
                </table>

                <h3 class="mt-5">
                    🔗 Endpoint API
                </h3>

                <a href="/health" class="btn btn-success endpoint-btn">
                    Health Check
                </a>

                <a href="/mahasiswa" class="btn btn-primary endpoint-btn">
                    Endpoint Mahasiswa
                </a>

            </div>

        </div>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {
        "status": "sehat"
    }

@app.route('/mahasiswa')
def mahasiswa():
    return [
        {
            "nama": "Andi",
            "nim": "120123"
        },
        {
            "nama": "Budi",
            "nim": "120124"
        }
    ]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)