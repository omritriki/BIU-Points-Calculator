from fastapi import FastAPI, UploadFile, Form
#from calculator import main
import main

app = FastAPI()

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