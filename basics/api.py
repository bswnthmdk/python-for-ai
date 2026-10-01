import requests

def get_weather(latitude, longitude):
    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()

    return data

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

data = get_weather(latitude, longitude)

temperature = data['current']['temperature_2m']
temperature_unit = data['current_units']['temperature_2m']
print(f"Temperature in Paris: {temperature} {temperature_unit}")