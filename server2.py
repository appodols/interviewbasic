# from fastapi import FastAPI, Request, WebSocket
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# from typing import Dict, Callable
# import uvicorn
# import requests
# import os
# from dotenv import load_dotenv
# from deepgram import Deepgram
# from chat_with_felix import analyze_excerpt

# load_dotenv()

# app = FastAPI()


# class InterviewExcerpt(BaseModel):
#     text: str


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )


# dg_client = Deepgram("c63446f4d781c3f89dff8f0528fe5289ac4269c7")

# templates = Jinja2Templates(directory="templates")


# @app.post("/analyze-text/")
# def analyze_text(excerpt: InterviewExcerpt):
#     print("analyze text called")
#     analysis_result = analyze_excerpt(excerpt.text)
#     # print("anaylze text has been called")
#     return analysis_result


# async def process_audio(fast_socket: WebSocket):
#     async def get_transcript(data: Dict) -> None:
#         if "channel" in data:
#             transcript = data["channel"]["alternatives"][0]["transcript"]

#             if transcript:
#                 await fast_socket.send_text(transcript)

#     deepgram_socket = await connect_to_deepgram(get_transcript)

#     return deepgram_socket


# async def connect_to_deepgram(transcript_received_handler: Callable[[Dict], None]):
#     try:
#         socket = await dg_client.transcription.live(
#             {"punctuate": True, "interim_results": False}
#         )
#         socket.registerHandler(
#             socket.event.CLOSE, lambda c: print(f"Connection closed with code {c}.")
#         )
#         socket.registerHandler(
#             socket.event.TRANSCRIPT_RECEIVED, transcript_received_handler
#         )

#         return socket
#     except Exception as e:
#         raise Exception(f"Could not open socket: {e}")


# @app.get("/", response_class=HTMLResponse)
# def get(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.websocket("/listen")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()

#     try:
#         deepgram_socket = await process_audio(websocket)

#         while True:
#             data = await websocket.receive_bytes()
#             deepgram_socket.send(data)
#     except Exception as e:
#         raise Exception(f"Could not process audio: {e}")
#     finally:
#         await websocket.close()
