from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel, validator
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")

# Serve the frontend folder
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

CSV_ROW_LIMIT = 100  # Maximum rows allowed per batch prediction request

@app.get("/")
def root():
    return FileResponse("../frontend/index.html")

@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        return {"fraud": int(prediction), "probability": float(probability)}
    except Exception as e:
        return {"error": str(e)}

class BatchInput(BaseModel):
    rows: List[List[float]]

    @validator("rows")
    def check_row_limit(cls, v):
        if len(v) > CSV_ROW_LIMIT:
            raise ValueError(
                f"Batch exceeds the {CSV_ROW_LIMIT}-row limit. "
                f"Received {len(v)} rows. Please split your data into smaller batches."
            )
        return v

@app.post("/predict_batch")
def predict_batch(data: BatchInput):
    try:
        features = np.array(data.rows)
        predictions = model.predict(features).tolist()
        probabilities = model.predict_proba(features)[:, 1].tolist()
        return {"predictions": predictions, "probabilities": probabilities}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        return {"error": str(e)}
