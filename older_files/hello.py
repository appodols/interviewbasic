
from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(who:str = Header()):
    return f"Hello? {who}?"




# from fastapi import FastAPI, Body

# app = FastAPI()


# @app.post("/hi")
# def greet(who: str = Body(embed=True)):
#     return f"Hello? {who}?"


# from fastapi import FastAPI

# app = FastAPI()


# # @app.get("/hi/{who}")
# # def greet(who):
# #     return f"Hello? {who}?"

# app = FastAPI()


# @app.get("/hi")
# def greet(who):
#     return f"Hello? {who}?"


# Lubanovic, Bill. FastAPI (p. 54). O'Reilly Media. Kindle Edition.


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/hi")
# def greet():
#     return "Hello? World?"


# if __name__ == "__main__":
#     import uvicorn


# http://localhost:8000/hi Example 3-5. Test /hi with Requests >>> import requests
# >>> r = requests.get("http://localhost:8000/hi")
# >>> r.json()
# 'Hello? World?' Example 3-6. Test /hi with HTTPX, which is almost identical to Requests >>> import httpx
# >>> r = httpx.get("http://localhost:8000/hi")
# >>> r.json()
# 'Hello? World?'

# Lubanovic, Bill. FastAPI (pp. 48-49). O'Reilly Media. Kindle Edition.
