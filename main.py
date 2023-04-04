from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

import nltk
nltk.download('punkt')

nltk.download('stopwords')


nltk.download('wordnet')

from starlette.middleware.cors import CORSMiddleware
from TextPreprocessor import TextAnalyzer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class userRequest(BaseModel):
    searchQuery : str
    paraArray: list

@app.get("/")
def handleroot():
    return "Hello"

@app.post('/summarizer')
async def getUserRequest(userR : userRequest):
    mlmodel = TextAnalyzer()
    summ =mlmodel.runnerClass(userR.paraArray,userR.searchQuery)
    return summ
