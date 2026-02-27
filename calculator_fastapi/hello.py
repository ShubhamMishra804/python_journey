from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def index():
    return HTMLResponse(open("templates\index.html").read())

@app.get("/add")
def add(num1: int, num2: int):
    plus = num1 + num2
    return {"result": plus}

@app.get("/sub")
def sub(num1: int, num2: int):
    gap = num1 - num2 
    return {"result": gap}

@app.get("/mul")
def sub(num1: int, num2: int):
    prod = num1 * num2 
    return {"result": prod}

@app.get("/div")
def sub(num1: int, num2: int):
    divi = num1 / num2 
    return {"result": divi}
 
