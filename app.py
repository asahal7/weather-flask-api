from flask import Flask, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

print("Loaded API Key:", os.getenv("WEATHER_API_KEY"))  # 👈 add this

app = Flask(__name__)

# Base URL for the public weather API (we'll use OpenWeatherMap)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Weather Flask API!"})

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city name, e.g. /weather?city=London"}), 400

    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return jsonify({"error": "API key not found. Please set WEATHER_API_KEY in your .env file."}), 500

    # Call the public weather API
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("API Error:", response.status_code, response.text)  # 👈 shows the real reason
        return jsonify({
            "error": "Could not fetch weather data",
            "status_code": response.status_code,
            "details": response.text
        }), response.status_code


    data = response.json()
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

    return jsonify(weather)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


