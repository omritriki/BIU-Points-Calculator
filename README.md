# BIU Points Calculator

A web application for calculating credit points and GPA from PDF transcripts.  
Built with FastAPI and pdfplumber, this project simplifies the process for BIU engineering students.

## Live Website

You can access the application here:  
[https://biu-points-calculator.onrender.com/](https://biu-points-calculator.onrender.com/)

## Features

- Upload your PDF gradesheet
- Select your degree and starting year
- Calculate total credit points and GPA
- Accessible online from any device

## Directory Structure

```
biu-points-calculator/
├── api.py                 # FastAPI app entry point
├── main.py                # Core logic for processing PDFs
├── calculator/            # Business logic modules
│   ├── __init__.py
│   ├── cid_to_hebrew.py   # Converts course IDs to Hebrew names
│   ├── calculate_points.py# Computes total points
│   ├── calculate_gpa.py   # Computes GPA
│   ├── points_dict.py     # Data mapping for points
│   └── read_file.py       # File reading and processing
├── static/                # Static files (CSS, images, etc.)
│   └── styles.css
├── templates/             # HTML templates
│   └── index.html
├── example_gradesheet.pdf # Example gradesheet for testing
└── requirements.txt       # Python dependencies
```

## Installation (For Local Development)

If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/biu-points-calculator.git
   cd biu-points-calculator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Update the `index.html` fetch commands:
   - Open `index.html` in a text editor.
   - Replace all instances of:
     ```javascript
     fetch('https://biu-points-calculator.onrender.com/...')
     ```
     with:
     ```javascript
     fetch('http://127.0.0.1:8000/...')
     ```
   - This ensures the frontend communicates with the locally running backend.

5. Run the application:
   ```bash
   uvicorn api:app --reload
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Example Gradesheet

An example gradesheet is included in the repository to help you test the application. You can find it at:

```
example_gradesheet.pdf
```

To use the example:
1. Open the application (either locally or on the live website).
2. Upload the `example_gradesheet.pdf` file.
3. Select a degree and starting year.
4. Click "Calculate" to see the results.

## Dependencies

- FastAPI
- pdfplumber
- uvicorn
- Jinja2

## Contributing

Contributions are welcome! Feel free to suggest new features, and inform me on bugs you found.


