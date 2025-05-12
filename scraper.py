import requests
from bs4 import BeautifulSoup
import re


def get_live_scores():
    # sample implementation
    url = "https://www.cricbuzz.com/live-cricket-scores/115345/kkr-vs-csk-57th-match-indian-premier-league-2025"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to fetch the page.")
        soup = BeautifulSoup(response.text, 'html.parser')
        return {"sample": soup.get_text(strip=True)}  # Gets visible text from the HTML
    except requests.exceptions.RequestException as e:
        return f"Error fetching the page: {e}"



# "https://www.cricbuzz.com/live-cricket-scores/115336/mi-vs-gt-56th-match-indian-premier-league-2025"