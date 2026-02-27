from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <head><title>Even Odd Checker</title></head>
        <body>
            <h1>Enter a Number</h1>
            <form action="/check" method="get">
                <input type="number" name="num" required>
                <button type="submit">Check</button>
            </form>
        </body>
    </html>
    """

@app.get("/check")
def check_o_e(num: int):
    if num%2 ==0 :
        result= "yes,even"
    else :
        result= "yes,odd"
    return {"number": num, "result": result}