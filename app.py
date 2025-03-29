# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================


from flask import Flask, request, render_template, jsonify
import subprocess
import os
from pointsDict import points 
from main import main  

app = Flask(__name__)

@app.route('/')
def index():
    # Get the degree options and their starting years dynamically from pointsDict
    degree_options = list(points.keys())
    starting_years = {degree: list(points[degree].keys()) for degree in degree_options}
    return render_template('index.html', degree_options=degree_options, starting_years=starting_years)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'gradesheet' not in request.files:
        return "No file part", 400

    file = request.files['gradesheet']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Extract degree and starting year from the form
        degree = request.form.get('degree')
        year = request.form.get('starting-year')

        if not degree or not year:
            return "Degree or starting year not provided", 400

        try:
            # from main import main  # Import the main function
            result = main(file, degree, year)  # Pass the file and form data to main
            return result, 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return f"{str(e)}", 500

if __name__ == '__main__':
    # This line is ignored when running with Gunicorn
    app.run(debug=False)  