from flask import Flask, request, jsonify, render_template, send_from_directory
import json
import os
import uuid

app = Flask(__name__)

MARKER_FILE = 'markers.txt'
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def load_markers():
    markers = []
    if os.path.exists(MARKER_FILE):
        with open(MARKER_FILE, 'r') as file:
            markers = [json.loads(line) for line in file]
    return markers


def save_marker(marker):
    with open(MARKER_FILE, 'a') as file:
        file.write(json.dumps(marker) + '\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_marker', methods=['POST'])
def add_marker():
    data = request.form
    files = request.files.getlist('mediaFiles')

    ip_address = request.remote_addr

    marker = {
        'name': data['name'],
        'description': data['description'],
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'informant': data['informant'],
        'mediaLink': data.get('mediaLink', ''),
        'ip': ip_address,
        'mediaFiles': []
    }

    for file in files:
        if file:
            filename = str(uuid.uuid4()) + '_' + file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            marker['mediaFiles'].append(filename)

    save_marker(marker)
    return jsonify({'success': True})


@app.route('/get_markers')
def get_markers():
    markers = load_markers()
    return jsonify(markers)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)