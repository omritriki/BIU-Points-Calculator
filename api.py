from fastapi import FastAPI, UploadFile, Form 
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse 
from fastapi.staticfiles import StaticFiles 
import main
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000/"],  # Replace "*" with your frontend's URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (make sure your "static" folder is in the root)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage route to serve index.html from the root directory
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("index.html")

# Endpoint to fetch degree options and starting years
@app.get("/options", response_class=JSONResponse)
async def get_options():
    try:
        logging.info("Fetching degree options and starting years.")
        # Fetch degree options and starting years from main.py
        degree_options, starting_years = main.get_degree_options_and_years()
        return {"degree_options": degree_options, "starting_years": starting_years}
    except Exception as e:
        logging.error(f"Error fetching options: {str(e)}")
        return {"error": str(e)}

@app.post("/upload")
async def upload_file(
    gradesheet: UploadFile = Form(...),  # File input
    degree: str = Form(...),            # Degree selection
    year: str = Form(...)               # Starting year selection
):
    try:
        logging.info(f"Received request to /upload")
        logging.info(f"Received file: {gradesheet.filename}")
        logging.info(f"Degree: {degree}")
        logging.info(f"Year: {year}")

        # Read the uploaded file
        file_content = await gradesheet.read()
        logging.info(f"File content size: {len(file_content)} bytes")

        # Pass the file content, degree, and year to the main function
        result = main.main(file_content, degree, year)
        logging.info("File processed successfully.")
        return {"success": True, "result": result}
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {"success": False, "error": str(e)}

from fastapi.responses import FileResponse 

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
