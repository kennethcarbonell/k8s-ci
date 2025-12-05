from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    html_content = "<h1>Hello Class Demo</h1>"
    # Return an HTML response with the specified content and status code
    return HTMLResponse(content=html_content, status_code=200)
