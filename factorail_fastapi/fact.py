from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def index():
    return HTMLResponse(open("templates/index.html").read())

@app.get("/num")
def cal_factorial(num: int):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return {"number": num, "factorial": result}