from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/', response_class=FileResponse)
def root_html():
    return "calculate.html"


@app.post('/calculate')
def calculate(num1: int = Form(ge=0, lt=111), num2: int = Form(ge=0, lt=111)):
    print(f"num1 = {num1}/nnum2 = {num2}")
    return {"result": num1 + num2}

# ge=0 specifies that the parameter value must be greater than or equal to 0.
# lt=111 specifies that the parameter value must be less than 111.


@app.get("/calculate", response_class=FileResponse)
def calc_form():
    return "calculate.html"


# uvicorn 3_calculate:app --reload
