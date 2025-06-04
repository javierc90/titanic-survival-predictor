# Titanic Survival Predictor 🛳️

Aplicación web con **FastAPI** que predice si un pasajero del Titanic habría sobrevivido, usando un modelo de red neuronal entrenado con **scikit-learn**.

---

## 🚀 Demo online

[https://titanic-survival-predictor.onrender.com](https://titanic-survival-predictor.onrender.com)

---

## 📋 Funcionalidades

- Formulario web para ingresar datos del pasajero.
- Predicción inmediata de supervivencia.
- Preprocesamiento automático con pipeline que incluye imputación, escalado, codificación y variables derivadas (grupo de edad, categoría de tarifa, interacción sexo-clase).
- Frontend simple y responsivo con Bootstrap.
- Backend rápido con FastAPI.

---

## 🛠 Tecnologías

- Python 3.9+
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- Jinja2
- Bootstrap 5

---

## 📁 Estructura del proyecto

.
├── app.py # Aplicación FastAPI
├── model/
│ └── titanic_model.joblib # Modelo serializado
├── templates/
│ └── form.html # Formulario HTML
├── requirements.txt # Dependencias
├── README.md
└── .gitignore

---

## 🖥️ Cómo correr localmente

```bash
git clone https://github.com/javierc90/titanic-survival-predictor.git
cd titanic-survival-predictor
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# o venv\Scripts\activate para Windows
pip install -r requirements.txt
uvicorn app:app --reload
