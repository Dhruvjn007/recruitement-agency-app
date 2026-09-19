from fastapi import FastAPI

app = FastAPI(title="Recruitment platform API")

@app.get("/health")
def health():
    return {"health":"ok"}


