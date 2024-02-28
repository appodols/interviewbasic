from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from chat_with_felix import (
    analyze_excerpt,
)  # Ensure chat_with_felix.py is properly imported

app = FastAPI()


class InterviewExcerpt(BaseModel):
    text: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/analyze-text/")
def analyze_text(excerpt: InterviewExcerpt):
    analysis_result = analyze_excerpt(excerpt.text)
    print("anaylze text has been called")
    return analysis_result


@app.get("/get-jwt")
def get_jwt():
    response = requests.post(
        TOKEN_ENDPOINT,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"ttl": 3600},  # Token valid for 1 hour
    )
    if response.status_code == 200:
        return response.json()  # Return the JWT to the client
    else:
        return {"error": "Failed to generate JWT"}


@app.websocket("/listen")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_bytes()
    except Exception as e:
        raise Exception(f"Could not process audio: {e}")
    finally:
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
