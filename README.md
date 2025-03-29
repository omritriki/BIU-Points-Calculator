# BIU Points Calculator

A web application for calculating credit points and GPA from PDF transcripts. 
Built with Flask and pdfplumber, this project simplifies the process for BIU engineering students.

## Features

- Upload your PDF gradesheet.
- Select your degree and starting year.
- Calculate total credit points and GPA dynamically.

## Directory Structure

```
biu-points-calculator/
├── app.py                 # Flask app entry point
├── main.py                # Alternative entry point or test script
├── calculator/            # Business logic modules
│   ├── __init__.py
│   ├── cid_to_hebrew.py   # Converts course IDs to Hebrew names
│   ├── calculate_points.py# Computes total points
│   ├── calculate_gpa.py   # Computes GPA
│   ├── points_dict.py     # Data mapping for points
│   └── read_file.py       # File reading and processing
├── templates/             # HTML templates
│   └── index.html
└── static/                # Static files (CSS, images, etc.)
    └── styles.css
```

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   flask run
   ```

## Dependencies

- Flask
- pdfplumber
