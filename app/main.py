import os, joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
MODEL_PATH = os.path.normpath(MODEL_PATH)

model = joblib.load(MODEL_PATH)

class PersonalityInput(BaseModel):
    Time_spent_Alone: float
    Stage_fear: Literal['Yes', 'No']
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: Literal['Yes', 'No']
    Friends_circle_size: float
    Post_frequency: float

@app.post('/predict')
def predict(data: PersonalityInput):
    sample = pd.DataFrame([data.model_dump()])
    pred = model.predict(sample)[0]
    proba = model.predict_proba(sample)[0]
    label = 'Introvert' if pred == 1 else 'Extrovert'
    return {
        'personality': label,
        'confidence': round(float(max(proba)), 4),
        'introvert_probability': round(float(proba[1]), 4),
        'extrovert_probability': round(float(proba[0]), 4),
    }

@app.get('/', response_class=HTMLResponse)
def ui():
    HTML_PATH = os.path.join(os.path.dirname(__file__), 'index.html')
    return open(HTML_PATH).read()