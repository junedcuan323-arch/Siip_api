from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy database KPJ
data_kpj = {
    "09006104187": {"nama": "Andi Saputra", "status": "Aktif", "upah": 5500000},
    "09001234567": {"nama": "Budi Santoso", "status": "Nonaktif", "upah": 4800000},
    "09002223334": {"nama": "Citra Dewi", "status": "Aktif", "upah": 6000000},
}

@app.route("/")
def home():
    return jsonify({"message": "SIIP API aktif"})

@app.route("/cek_kpj")
def cek_kpj():
    nomor = request.args.get("nomor")
    if nomor in data_kpj:
        return jsonify(data_kpj[nomor])
    else:
        return jsonify({"error": "Data tidak ditemukan"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)