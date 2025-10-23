# Weather Flask API

A simple Flask API that returns current weather data for a given city using OpenWeatherMap.

## Setup

1. Clone the repo:
git clone https://github.com/asahal7/weather-flask-api.git

2. Create a virtual environment and activate it:
python3 -m venv venv
source ../venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file in the project root:
WEATHER_API_KEY=your_openweathermap_api_key

5. Run the API:
python3 app.py

## Usage

Visit:
http://127.0.0.1:5001/weather?city=London

Returns:
```json
{
  "city": "London",
  "temperature": 9.61,
  "description": "light rain"
}



