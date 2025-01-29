from fastapi import FastAPI,status
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/user",status_code=status.HTTP_200_OK)
def user_info():
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return{
        "email" : "mremmatola@gmail.com",
        "current_datetime":current_datetime,
        "github_url":"https://github.com/AyoIbitola/hng-stage-0"
    }