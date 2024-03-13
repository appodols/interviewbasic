from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.staticfiles import StaticFiles
from chat_with_felix import analyze_excerpt
import os


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


@app.get("/", response_class=FileResponse)
def get_root():
    # Use the absolute path to return the HTML file as a response
    absolute_path_to_html = os.path.join(
        "/Users/alexanderpodolsky/Documents/InterviewCoPilot/static", "basic_file.html"
    )
    return FileResponse(absolute_path_to_html)


@app.post("/analyze-text/")
def analyze_text(excerpt: InterviewExcerpt):
    # print("Analyze text called")
    # Assuming `analyze_excerpt` is a function that takes a string and returns analysis
    analysis_result = analyze_excerpt(excerpt.text)
    print(analysis_result)
    # You return a dictionary because FastAPI automatically converts it to JSON
    return {"analysis": analysis_result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
