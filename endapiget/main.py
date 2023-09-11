from fastapi import FastAPI, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/info") 
async def get_info(
    name: str = Query(None),
    course: str = Query(None)  
):

    day = datetime.now(pytz.utc).strftime("%A")
    time = datetime.utcnow().isoformat() + 'Z'

    file_url = "https://github.com/username/repo/blob/main/main.py"
    repo_url = "https://github.com/username/repo"

    return {
        "name": name,
        "day": day,
        "time": time,
        "course": course,
        "file_url": file_url,
        "repo_url": repo_url,
        "status": 200
    }