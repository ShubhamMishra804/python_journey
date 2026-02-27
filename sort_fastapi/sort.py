from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class NumberList(BaseModel):
    numbers: List[int]

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head>
        <title>Second Highest Number</title>
    </head>
    <body>
        <h2>Enter numbers separated by commas:</h2>
        <input type="text" id="numbersInput" size="50" placeholder="e.g. 5,2,8,3">
        <button onclick="sendNumbers()">Submit</button>

        <h3>Result:</h3>
        <div id="result"></div>

        <script>
            async function sendNumbers() {
                const input = document.getElementById('numbersInput').value;
                const numbers = input.split(',')
                                     .map(x => parseInt(x.trim()))
                                     .filter(x => !isNaN(x));
                if(numbers.length === 0) {
                    document.getElementById('result').innerHTML = "<span style='color:red'>Enter valid numbers!</span>";
                    return;
                }
                const res = await fetch('/second_highest', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({numbers})
                });
                const data = await res.json();
                if(data.second_highest !== undefined) {
                    document.getElementById('result').innerHTML = 
                        `Sorted list (ascending): [${data.sorted_list}]<br>Second highest: ${data.second_highest}`;
                } else {
                    document.getElementById('result').innerHTML = 
                        `Sorted list (ascending): [${data.sorted_list}]<br>${data.message}`;
                }
            }
        </script>
    </body>
    </html>
    """

@app.post("/second_highest")
def second_highest_post(data: NumberList):
    alist = sorted(set(data.numbers))  # sort ascending
    if len(alist) < 2:
        return {"sorted_list": alist, "message": "Not enough numbers"}
    return {"sorted_list": alist, "second_highest": alist[-2]}