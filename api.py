from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles # type: ignore
import main
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

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
        return {"error": str(e)}

@app.post("/upload")
async def upload_file(
    gradesheet: UploadFile, degree: str = Form(...), year: str = Form(...)
):
    try:
        # Log the received inputs
        logging.info(f"Received file: {gradesheet.filename}, degree: {degree}, year: {year}")

        # Read the uploaded file
        file_content = await gradesheet.read()

        # Pass the file content, degree, and year to the main function
        result = main.main(file_content, degree, year)

        # Return the result to the frontend
        return {"success": True, "result": result}
    except Exception as e:
        # Log the error
        logging.error(f"Error processing file: {str(e)}")
        # Handle errors and return them to the frontend
        return {"success": False, "error": str(e)}

from fastapi.responses import FileResponse

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
