from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        forecast = len(df) * 2  # Example logic

        return f"Forecast completed! Estimated days: {forecast}"
    return 'Invalid file format. Please upload a CSV.'

if __name__ == '__main__':
    app.run(debug=True)