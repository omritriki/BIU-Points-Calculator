from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import main

app = FastAPI()

# Mount static files (make sure your "static" folder is in the root)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage route to serve index.html from the root directory
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("index.html")

@app.post("/upload")
async def upload_file(
    gradesheet: UploadFile, degree: str = Form(...), year: str = Form(...)
):
    try:
        # Call the main function with the uploaded file and form data
        result = main.main(gradesheet.file, degree, year)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
