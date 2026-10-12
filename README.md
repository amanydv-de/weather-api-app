
# Weather API App 🌦️

## Introduction

The Weather API App is a desktop application built using Python and PyQt5 that allows users to check real-time weather information for any city. It fetches weather data from the OpenWeatherMap API and displays the current temperature, weather description, and a corresponding weather emoji.

The application provides a simple graphical user interface (GUI) that makes checking weather conditions quick and easy.

## Features

- **City-Based Weather Search:** Enter a city name to retrieve its current weather information.
- **Real-Time Weather Data:** Fetches weather information using the OpenWeatherMap API.
- **Temperature Conversion:** Converts temperature from Kelvin to Celsius and displays it in Celsius.
- **Weather Description:** Displays conditions such as clear sky, rain, clouds, and snow.
- **Weather Emojis:** Shows an emoji based on the weather condition.
- **Error Handling:** Handles invalid city names, HTTP errors, connection issues, and request timeouts.
- **User-Friendly Interface:** Provides a desktop GUI with a city input field, a weather button, and weather information labels.

## Technologies Used

- **Python:** Core programming language used to develop the application.
- **PyQt5:** Used to build the desktop graphical user interface.
- **Requests:** Used to send HTTP requests and retrieve weather data from the API.
- **OpenWeatherMap API:** Provides real-time weather information.
- **VS Code:** Used for writing and running the Python code.
- **Git & GitHub:** Used for version control and project hosting.

## How It Works

1. The user enters a city name in the input field.
2. The application sends a request to the OpenWeatherMap API.
3. The API returns weather information in JSON format.
4. The application extracts the temperature, weather condition, and weather ID.
5. The temperature is converted from Kelvin to Celsius.
6. A weather emoji is selected based on the weather ID.
7. The results are displayed in the application window.

## Project Structure

```text
weather-api-app/
│
├── weather.py
├── README.md
└── requirements.txt
```

*Note: Update the filenames above to match the actual files in your repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/amanydv-de/weather-api-app.git
cd weather-api-app
```

### 2. Install Dependencies

```bash
pip install PyQt5 requests
```

Alternatively, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Get an API key from [OpenWeatherMap](https://openweathermap.org/api).

For security, store your API key in an environment variable instead of hardcoding it in your source code.

For example, on Windows PowerShell:

```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

Then retrieve it in Python:

```python
import os

api_key = os.getenv("OPENWEATHER_API_KEY")
```

Replace the hardcoded `api_key` in the application with this environment-variable approach.

### 4. Run the Application

```bash
python weather.py
```

## Error Handling

The application handles several potential errors:

- **400 Bad Request:** Checks whether the request is valid.
- **401 Unauthorized:** Indicates an invalid or unauthorized API key.
- **404 Not Found:** Displays an error when a city cannot be found.
- **Connection Error:** Notifies the user when the internet connection fails.
- **Timeout Error:** Handles requests that take too long to respond.
- **Other HTTP Errors:** Displays an appropriate error message.

## What I Learned

- Working with a third-party REST API using Python.
- Sending HTTP requests and processing JSON responses.
- Building desktop applications with PyQt5.
- Handling HTTP errors, network failures, and request exceptions.
- Using conditional statements to map weather codes to emojis.
- Converting temperature values between measurement units.
- Organizing Python code using classes, methods, and static methods.

## Future Improvements

- Display humidity, wind speed, and atmospheric pressure.
- Add a loading indicator while fetching weather information.
- Improve the interface with custom colors, icons, and responsive layouts.
- Add weather forecasts for upcoming days.
- Store the API key securely using environment variables.
- Add support for displaying temperatures in Celsius, Fahrenheit, and Kelvin.

## Conclusion

This project demonstrates how Python, PyQt5, and a third-party weather API can be combined to create a functional desktop application. It strengthened my understanding of API integration, GUI development, JSON processing, exception handling, and building practical Python projects.
