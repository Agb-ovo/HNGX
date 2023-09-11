from fastapi import FastAPI, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/") 
async def get_info(
    slack_name: str = "agbrokoogheneovo",
    course: str = "backend" 
):

    day = datetime.now(pytz.utc).strftime("%A")
    time = datetime.utcnow().isoformat() + 'Z'

    file_url = "https://github.com/Agb-ovo/HNGX/blob/b8ee70f1375a5d79b95cdfc064fa0687d3b81e1e/endapiget/main.py"
    repo_url = "https://github.com/Agb-ovo/HNGX.git"

    return {
        "name": slack_name,
        "day": day,
        "time": time,
        "course": course,
        "file_url": file_url,
        "repo_url": repo_url,
        "status": 200
    }
