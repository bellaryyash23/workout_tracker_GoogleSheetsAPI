import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = "male"
WEIGHT_KG = "65"
HEIGHT_CM = "180"
AGE = "20"

nutrition_API_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_get_endpoint = os.environ.get("SHEETY_GET")
sheety_post_endpoint = os.environ.get("SHEETY_POST")

today = datetime.now().date()
TIME = datetime.now().time().strftime("%X")
TODAY_DATE = str(today.strftime("%d/%m/%Y"))

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = str(input("Tell me which exercise you did: "))

nutrition_query = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutrition_API_endpoint, json=nutrition_query, headers=headers)
response.raise_for_status()
exercise_data = response.json()["exercises"]

for exercise in exercise_data:
    sheet_inputs = {
        "workout": {
            "date": TODAY_DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "authorization": "Bearer Secure@007"
    }

    sheet_response = requests.post(url=sheety_post_endpoint, json=sheet_inputs, headers=headers)
    sheet_response.raise_for_status()
