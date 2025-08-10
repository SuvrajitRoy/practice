import requests

API_KEY = '6bd06c8acd42d8624b57a7fe98edfcfb'  # এখানেই আপনার API Key বসান
city = 'Dhaka'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"City: {city}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Failed to retrieve data:", response.status_code)
