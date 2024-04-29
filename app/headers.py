from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.get("/headers")
def root(request: Request):
    headers = dict()
    try:
        headers["User-Agent"] = request.headers["User-Agent"]
        headers["Accept-Language"] = request.headers["Accept-Language"]
    except KeyError:
        raise HTTPException(status_code=400, detail="Missing headers in request")
    return str(headers)

# uvicorn app.headers:app --reload