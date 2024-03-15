from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.staticfiles import StaticFiles
from chat_with_felix import analyze_excerpt
from fastapi.templating import Jinja2Templates

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        # Add headers to prevent caching
        response.headers["Cache-Control"] = "no-store"
        return response

app = FastAPI()

# Define a Pydantic model for the request body
class InterviewExcerpt(BaseModel):
    text: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    # Render the HTML template with Jinja2
    return templates.TemplateResponse("basic_file.html", {"request": request})

@app.post("/analyze-text/")
def analyze_text(excerpt: InterviewExcerpt):
    # print("Analyze text called")
    # Assuming `analyze_excerpt` is a function that takes a string and returns analysis
    analysis_result = analyze_excerpt(excerpt.text)
    print(analysis_result)
    return {"analysis": analysis_result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)