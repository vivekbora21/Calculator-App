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
@app.get("/add") # performs addition
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub") # performs subtraction
def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul") # performs multiplication
def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div") # performs division
def div(a: float, b: float):
    return {"result": "Infinity" if b == 0 else a / b}