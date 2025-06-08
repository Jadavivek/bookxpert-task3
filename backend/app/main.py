
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .model_handler import generate_response

app = FastAPI()

# CORS for frontend dev (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/query")
async def get_recipe(request: Request):
    body = await request.json()
    query = body.get("query", "")
    response = generate_response(query)
    return {"response": response}
