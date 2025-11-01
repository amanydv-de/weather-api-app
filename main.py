import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class Weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city")
        self.city_input.setObjectName("input")
        self.weather_button.setObjectName("button")
        self.temp_label.setObjectName("temp")
        self.emoji.setObjectName("emoji")
        self.description_label.setObjectName("des")

        self.setStyleSheet("""
             QLabel,QPushButton{
                 font-family:calibri;
                 
             }
             QLabel#city{
                 font-size:40px;
                 font-style:italic;
             }
             QLineEdit#input{
                 font-size:40px;
                 font-style:Arial;
             }
             QPushButton#button{
                 font-size:35px;
                 font-style:italic;
             }
             QLabel#temp{
                 font-size:35px;
             }
             QLabel#emoji{
                 font-size:100px;
                 font-family:Segoe UI emoji;
             }
             QLabel#des{
                 font-size:50px;
                 font-style:italic;
             }     
                """)
        self.weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "4ca2cf53b842df17a8afd78f4862a636"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:

            response = requests.get(url)
            response.raise_for_status()  # raise exceptions if there is http error #
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease Check Your Input ")
                case 401:
                    self.display_error("Unauthorised\nInvalid API Key ")
                case 403:
                    self.display_error("Forbidden\nAccess is Denied ")
                case 404:
                    self.display_error("Not Found\nCity Not Found")
                case 500:
                    self.display_error(
                        "Internal Server Error\nPlease Try Again Later ")
                case 502:
                    self.display_error(
                        "Bad Gateway\nInvalid Response From The Server")
                case 503:
                    self.display_error("Service Unavailbale\nServer is down")
                case 504:
                    self.display_error(
                        "Gateway timeout\nNo response from the server")
                case _:
                    self.display_error(f"HTTP Error {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection Error\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout error\nRequest timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the url")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error\n{req_error}")

    def display_error(self, message):

        self.temp_label.setStyleSheet("font-size:20px;"
                                      "color:red;")

        self.temp_label.setText(message)
        self.emoji.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size:35px;")
        temp_k = data["main"]["temp"]
        temp_c = round(temp_k-273.15, 2)
        temp_f = (temp_k*9/5)-459.67
        self.temp_label.setText(f"{temp_c}°C")
        weather_id = data["weather"][0]["id"]

        weather_des = data["weather"][0]["description"]
        self.description_label.setText(weather_des)

        print(data)
        self.emoji.setText(self.getweather_emoji(weather_id))

    @staticmethod
    def getweather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "⛅"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = Weatherapp()
    weather_app.show()
    sys.exit(app.exec_())
