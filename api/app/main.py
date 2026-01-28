from fastapi import FastAPI

app = FastAPI(title="DailyFocus Copilot App")

@app.get("/health")
def health():
    return {"status": "ok"}
