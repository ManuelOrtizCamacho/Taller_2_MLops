from pandas import DataFrame
from joblib import load
from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException

model = load("best_gbr_model.pkl")

app = FastAPI()

class JSON(BaseModel):
  Age: float
  Gender: float
  Ethnicity: float
  ParentalEducation: float
  StudyTimeWeekly: float
  Absences: float
  Tutoring: float
  ParentalSupport: float
  Extracurricular: float
  Sports: float
  Music: float
  Volunteering: float
  GPA: float
  
@app.post("/predict")
def predict(request: JSON):
  try:
    df_data = DataFrame(request)
    prediction = model.predict(df_data)
    return {"prediction": prediction.tolist()}
  except ValidationError as ve:
    raise HTTPException(status_code=400, detail=ve.errors())
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
  return {'Universidad EIA': 'Our Work'}
