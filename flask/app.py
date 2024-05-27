from flask import Flask, jsonify
from flask_cors import CORS
import csv
import os
from recommendation import recommendation_bp 

app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk semua rute
app.register_blueprint(recommendation_bp, url_prefix='/api')
# Path file CSV hasil rekomendasi
CSV_FILE_PATH = {
    'populer': r'D:\KULIAH\SKRIPSI\flask\dataset-populer.csv',
    'populerakuntansi': r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Akuntansi.csv',
    'populeraudit': r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Audit Keuangan.csv',
    'populerekonomi': r'10kategori/popular_books.xlsx - Buku Populer - Ekonomi Keuangan.csv',
    'populermk': r'10kategori/popular_books.xlsx - Buku Populer - Manajemen Keuangan.csv',
    'populermp': r'10kategori/popular_books.xlsx - Buku Populer - Manajemen Pemasaran.csv',
    'populermnj': r'10kategori/popular_books.xlsx - Buku Populer - Manajemen.csv',
    'populermarketing': r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Marketing.csv',
    'populerpajak': r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Perpajakan.csv',
    'populersastra': r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Retorika & Kumpulan Karya Sastra.csv',
    'populerlk' : r'D:\KULIAH\SKRIPSI\flask\10kategori\popular_books.xlsx - Buku Populer - Laporan Keuangan.csv' 
}

# Fungsi untuk membaca file CSV
def read_csv_file(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data

# Endpoint untuk mendapatkan data rekomendasi
@app.route('/populer', methods=['GET'])
def get_populer():
    file_path = CSV_FILE_PATH.get('populer')
    if os.path.exists(file_path):
        populer = read_csv_file(file_path)
        return jsonify(populer), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_akuntansi', methods=['GET'])
def get_populerakuntansi():
    file_path = CSV_FILE_PATH.get('populerakuntansi')
    if os.path.exists(file_path):
        populerakuntansi = read_csv_file(file_path)
        return jsonify(populerakuntansi), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_audit', methods=['GET'])
def get_populeraudit():
    file_path = CSV_FILE_PATH.get('populeraudit')
    if os.path.exists(file_path):
        populeraudit = read_csv_file(file_path)
        return jsonify(populeraudit), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_ekonomi', methods=['GET'])
def get_populerekonomi():
    file_path = CSV_FILE_PATH.get('populerekonomi')
    if os.path.exists(file_path):
        populerekonomi = read_csv_file(file_path)
        return jsonify(populerekonomi), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_mk', methods=['GET'])
def get_populermk():
    file_path = CSV_FILE_PATH.get('populermk')
    if os.path.exists(file_path):
        populermk = read_csv_file(file_path)
        return jsonify(populermk), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_mp', methods=['GET'])
def get_populermp():
    file_path = CSV_FILE_PATH.get('populermp')
    if os.path.exists(file_path):
        populermp = read_csv_file(file_path)
        return jsonify(populermp), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_mnj', methods=['GET'])
def get_populermnj():
    file_path = CSV_FILE_PATH.get('populermnj')
    if os.path.exists(file_path):
        populermnj = read_csv_file(file_path)
        return jsonify(populermnj), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_marketing', methods=['GET'])
def get_populermarketing():
    file_path = CSV_FILE_PATH.get('populermarketing')
    if os.path.exists(file_path):
        populermarketing = read_csv_file(file_path)
        return jsonify(populermarketing), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_pajak', methods=['GET'])
def get_populerpajak():
    file_path = CSV_FILE_PATH.get('populerpajak')
    if os.path.exists(file_path):
        populerpajak = read_csv_file(file_path)
        return jsonify(populerpajak), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/populer_sastra', methods=['GET'])
def get_populersastra():
    file_path = CSV_FILE_PATH.get('populersastra')
    if os.path.exists(file_path):
        populersastra = read_csv_file(file_path)
        return jsonify(populersastra), 200
    else:
        return jsonify({'error': 'File not found'}), 404
    
@app.route('/populer_lk', methods=['GET'])
def get_populerlk():
    file_path = CSV_FILE_PATH.get('populerlk')
    if os.path.exists(file_path):
        populerlk = read_csv_file(file_path)
        return jsonify(populerlk), 200
    else:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
