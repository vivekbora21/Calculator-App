from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Serve index.html at "/"
@app.get("/", response_class=HTMLResponse)
def get_home():
    with open("index.html", "r") as f:
        html_content = f.read()
    return html_content

# Calculator API endpoint
@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
def div(a: float, b: float):
    return {"result": "Cannot divide by zero!" if b == 0 else a / b}