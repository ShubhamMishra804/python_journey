# write a fastapi  code to check  whether the  given string  is  a  palindrome or not for example naman
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse

app = FastAPI()

@app.get("/")
def index():
    return HTMLResponse(open("templates\palindrome.html").read())

@app.get("/palindrome")
def palindrome(text):
    a=text[::-1]
    # print(text[::-1])
    if a == text:
        return JSONResponse({"result": f'"{text}" is a palindrome ✅'})
    else:
        return JSONResponse({"result": f'"{text}" is NOT a palindrome ❌'})
 
