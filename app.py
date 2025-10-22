from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Weather Flask API! Use /weather?city=CityName"
    })

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name, e.g., /weather?city=London"}), 400

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "Failed to get weather data")}), response.status_code

    weather_info = {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
