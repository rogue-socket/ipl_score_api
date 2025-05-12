from fastapi import FastAPI
from scraper import get_live_scores
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to IPL Scores API"}


@app.get("/scores")
def get_score():
    try:
        data = get_live_scores()
        return {"scores": data}

    except Exception as e:
        return {"error": e}

