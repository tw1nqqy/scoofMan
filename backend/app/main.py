from fastapi import FastAPI
from backend.app.api import auth_router
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
async def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)