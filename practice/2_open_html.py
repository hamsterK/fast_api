from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/')  # '/' is default address
def root():
    return FileResponse('../index.html')


# uvicorn open_html:app --reload
