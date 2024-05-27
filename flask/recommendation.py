from flask import Blueprint, jsonify
import csv
import os

# Buat Blueprint untuk modularisasi
recommendation_bp = Blueprint('recommendation', __name__)

# Path file CSV hasil rekomendasi
CSV_FILE_PATH = {
    'recommendationak': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\ak.csv',
    'recommendationaudit': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\audit.csv',
    'recommendationekonomi': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\ek.csv',
    'recommendationlk': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\lk.csv',
    'recommendationmk': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\mk.csv',
    'recommendationmnj': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\mnj.csv',
    'recommendationmarketing': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\marketing.csv',
    'recommendationmp': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\mp.csv',
    'recommendationpajak': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\perpajakan.csv',
    'recommendationsastra': r'D:\KULIAH\SKRIPSI\flask\rekomendasi\1.csv'
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
@recommendation_bp.route('/recommendation_ak', methods=['GET'])
def get_recommendation_ak():
    file_path = CSV_FILE_PATH.get('recommendationak')
    if os.path.exists(file_path):
        recommendation_ak = read_csv_file(file_path)
        return jsonify(recommendation_ak), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_audit', methods=['GET'])
def get_recommendation_audit():
    file_path = CSV_FILE_PATH.get('recommendationaudit')
    if os.path.exists(file_path):
        recommendation_audit = read_csv_file(file_path)
        return jsonify(recommendation_audit), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_ekonomi', methods=['GET'])
def get_recommendation_ekonomi():
    file_path = CSV_FILE_PATH.get('recommendationekonomi')
    if os.path.exists(file_path):
        recommendation_ekonomi = read_csv_file(file_path)
        return jsonify(recommendation_ekonomi), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_lk', methods=['GET'])
def get_recommendation_lk():
    file_path = CSV_FILE_PATH.get('recommendationlk')
    if os.path.exists(file_path):
        recommendation_lk = read_csv_file(file_path)
        return jsonify(recommendation_lk), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_mk', methods=['GET'])
def get_recommendation_mk():
    file_path = CSV_FILE_PATH.get('recommendationmk')
    if os.path.exists(file_path):
        recommendation_mk = read_csv_file(file_path)
        return jsonify(recommendation_mk), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_mnj', methods=['GET'])
def get_recommendation_mnj():
    file_path = CSV_FILE_PATH.get('recommendationmnj')
    if os.path.exists(file_path):
        recommendation_mnj = read_csv_file(file_path)
        return jsonify(recommendation_mnj), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_marketing', methods=['GET'])
def get_recommendation_marketing():
    file_path = CSV_FILE_PATH.get('recommendationmarketing')
    if os.path.exists(file_path):
        recommendation_marketing = read_csv_file(file_path)
        return jsonify(recommendation_marketing), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_mp', methods=['GET'])
def get_recommendation_mp():
    file_path = CSV_FILE_PATH.get('recommendationmp')
    if os.path.exists(file_path):
        recommendation_mp = read_csv_file(file_path)
        return jsonify(recommendation_mp), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_pajak', methods=['GET'])
def get_recommendation_pajak():
    file_path = CSV_FILE_PATH.get('recommendationpajak')
    if os.path.exists(file_path):
        recommendation_pajak = read_csv_file(file_path)
        return jsonify(recommendation_pajak), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@recommendation_bp.route('/recommendation_sastra', methods=['GET'])
def get_recommendation_sastra():
    file_path = CSV_FILE_PATH.get('recommendationsastra')
    if os.path.exists(file_path):
        recommendation_sastra = read_csv_file(file_path)
        return jsonify(recommendation_sastra), 200
    else:
        return jsonify({'error': 'File not found'}), 404
