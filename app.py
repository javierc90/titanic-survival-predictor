from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
import pandas as pd

# Cargar modelo
model = joblib.load("model/titanic_model.joblib")

# FastAPI setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
def form_post(
    request: Request,
    age: float = Form(...),
    family_size: int = Form(...),
    fare: float = Form(...),
    pclass: int = Form(...),
    sex: str = Form(...),
    embarked: str = Form(...)
):
    # Crear DataFrame base
    df = pd.DataFrame([{
        "age": age,
        "family_size": family_size,
        "fare": fare,
        "pclass": pclass,
        "sex": sex,
        "embarked": embarked
    }])

    # Añadir columnas derivadas

    # age_group
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 5, 12, 18, 30, 50, 100],
        labels=["infant", "child", "teen", "young_adult", "adult", "senior"]
    )
    if fare > 600:
        df["fare"] = 600
        
    # fare_category
    df["fare_category"] = pd.cut(
        df["fare"],
        bins=[-1, 10, 30, 100, 600],
        labels=["low", "medium", "high", "very_high"]
    )

    # sex_class
    df["sex_class"] = df["sex"] + "_class" + df["pclass"].astype(str)

    # Predicción
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    result = {
        "prediction": prediction,
        "probability": round(probability * 100, 2),
        "message": "¡Sobreviviría! 🎉" if prediction == 1 else "No sobreviviría 😢"
    }

    return templates.TemplateResponse("form.html", {"request": request, "result": result})
