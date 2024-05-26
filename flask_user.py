from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from pydub import AudioSegment
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_data = request.json['message']
    audio_bytes = base64.b64decode(audio_data)
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="webm")
    file_location = "user_audio.wav"
    audio.export(file_location, format="wav")
    return jsonify({'status': 'Audio processed and saved!', 'file': file_location})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
