from fastapi import FastAPI

app = FastAPI(title="TechRadar API")


@app.get("/health")
def health_check():
    return {"status": "ok"}