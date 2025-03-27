from flask import Flask, request, render_template, jsonify
import subprocess
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Render the existing index.html file
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file is in the request
    if 'gradesheet' not in request.files:
        return "No file part", 400

    file = request.files['gradesheet']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Save the uploaded file to the uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Run the file through main.py
        try:
            result = subprocess.run(
                ['python3', 'main.py', filepath],
                capture_output=True,
                text=True
            )
            # Return the output of main.py
            return result.stdout, 200
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)