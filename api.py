# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================
# Description:
#   This script defines the FastAPI backend for the BIU Points Calculator. It includes endpoints for:
#   - Serving the homepage and static files.
#   - Fetching degree options and starting years.
#   - Uploading and processing a gradesheet PDF to calculate points and GPA.
# ===================================================================================================

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
    allow_origins=["https://biu-points-calculator.onrender.com/"],  
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
        # Fetch degree options and starting years from main.py
        degree_options, starting_years = main.get_degree_options_and_years()
        return {"degree_options": degree_options, "starting_years": starting_years}
    except Exception as e:
        logging.error(f"Error fetching options: {str(e)}")
        return {"error": str(e)}

@app.post("/upload")
async def upload_file(
    gradesheet: UploadFile = Form(...),
    degree: str = Form(...),
    year: str = Form(...)
):
    try:
        # Read the file content
        file_content = await gradesheet.read()

        try:
            # Pass the file content to main
            result = main.main(file_content, degree, year)
            return {"success": True, "result": result}
        except Exception as calc_error:
            logging.error(f"Calculation error: {str(calc_error)}")
            return {"success": False, "error": f"Error calculating points: {str(calc_error)}"}
            
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {"success": False, "error": str(e)}

from fastapi.responses import FileResponse 

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
