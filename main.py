import uvicorn
from fastapi import FastAPI
from pdf2docx import Converter

app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello':"World"}

@app.get("/convert/")
async def convert_pdf_to_word():
    pdf_file = "./test.pdf"
    docx_file = "./test.docx"

    # Convert PDF to Word
    cv=Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
    
    return {'success':"成功"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True # 启用热重载
    )