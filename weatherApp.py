# Source: https://www.youtube.com/watch?v=-_z2RPAH0Qk
# Source: https://www.youtube.com/watch?v=8ULl4PxgAzw
# Source: https://www.blog.pythonlibrary.org/2022/01/25/pysimplegui-an-intro-to-laying-out-elements/
# Source: https://www.youtube.com/watch?v=UwpJtqTXxSI
import PySimpleGUI as py
import json
import requests
from socket import *

class WeatherApp:
    def __init__(self):
        self._data = False
        self._prevlocation = None
        self._currlocation = None
        self._cel = False
        py.theme("NeutralBlue")
        # "NeutralBlue"
        # "DarkBlue1"

    def create_main(self):
        """
        Creates the current weather window
        """
        self._main = True
        gobutton = [
            [py.Button("History", font=100, button_color='teal'), py.Button("Undo", button_color="teal", font=100), py.InputText("", font=("helvetica", 15, "bold"), do_not_clear=False, key='-LOCATION-'), py.Button("Save", size = (5,2), button_color='yellow'), py.Button("Go", size=(5,2), button_color="green")],
        ]

        tempbutton = [
            [py.Button('Temp Type', button_color="DarkGrey", font=100), py.Button('Refresh', font=100, button_color='yellow')],
        ]

        curheader = [
            [py.Text("CURRENT WEATHER", font= ("Helvetica", 20))]
        ]

        # Current Location
        curlocationcolumn = [
            [py.Text("CURRENT LOCATION: "), py.Text(key='-CURLOCATION-', font=("Helvetica", 10, "bold"))],
            [py.Text("REGION: "), py.Text(key='-REGION-', font=("Helvetica", 10, "bold"))],
            [py.Text("Local Time: "), py.Text(key='-TIME-', font=("Helvetica", 10, "bold"))],
            [py.HSeparator()],
            [py.Image(key='-PICTURE-', pad=(25, 25)), py.Push(), py.Text("TEMP:"), py.Text(key='-TEMP-', font=("Helvetica", 70, "bold"), justification= 'right')],
            [py.Text("Description: "), py.Text(key='-DESCRIPTION-', font=("Helvetica", 10, "bold"))],
            [py.Text("Long:"), py.Text(key='-LONG-',font=("Helvetica", 10, "bold")),py.Text("Lat: "), py.Text(key='-LAT-', font=("Helvetica", 10, "bold"))],
            [py.Text("Wind Direction: "), py.Text(key='-WINDDIR-',  font=("Helvetica", 10, "bold"))],
            [py.Text("Wind Speed: "), py.Text(key='-WINDSPEED-', font=("Helvetica", 10, "bold")), py.Text("MPH")],
            [py.Text(pad=(25, 25))],
        ]

        # Right columns
        rightcolumn1 = [
            [py.Button("7-day-forecast")],
            [py.Button("Hourly weather summary")],
        ]

        # Main layout
        layout1 = [
            [py.Column(curheader, vertical_alignment='center', justification='center')],
            [py.HSeparator()],
            [py.Column(curlocationcolumn, vertical_alignment='top'), py.VerticalSeparator(pad=(50, 50)),
             py.Column(rightcolumn1)],
            [tempbutton],
            [py.HSeparator()],
            [gobutton],
            []
        ]

        # Creates the Window
        window = py.Window("Totally Awesome Weather App", layout1, margins=(50, 50))

        while True:
            event, values = window.read()

            # when the window is closed -- what happens
            if event == py.WIN_CLOSED:
                break

            if event == "Refresh" and self._currlocation:
                print("Refreshing the data...")
                # Load Json file
                with open('weather.json', 'r') as weather:
                    weatherdata = json.load(weather)

                # Updates variables
                window['-CURLOCATION-'].update(weatherdata['location']['name'])
                window['-REGION-'].update(weatherdata['location']['region'])
                window['-TIME-'].update(weatherdata['location']['localtime'])
                window['-TEMP-'].update(weatherdata['current']['temp_f'])
                imageget = requests.get("https:"+weatherdata['current']['condition']['icon'])                #Gets image
                window['-PICTURE-'].update(data=imageget.content)
                window['-DESCRIPTION-'].update(weatherdata['current']['condition']['text'])
                window['-LONG-'].update(weatherdata['location']['lon'])
                window['-LAT-'].update(weatherdata['location']['lat'])
                window['-WINDDIR-'].update(weatherdata['current']['wind_dir'])
                window['-WINDSPEED-'].update(weatherdata['current']['wind_mph'])

            # Writes and reads new location to text file
            if event == "Go" and values['-LOCATION-'] != '':
                self._prevlocation = self._currlocation
                self._currlocation = values['-LOCATION-']

                print("Fetching weather data")
                response = requests.get(
                    f"api_uri_placeholder{self._currlocation}")
                jsondata = response.json()
                with open('weather.json', 'w') as weather:
                    json.dump(jsondata, weather, indent=2)

                # Load Json file
                print('Data collected')
                with open('weather.json', 'r') as weather:
                    weatherdata = json.load(weather)

                # Updates variables
                window['-CURLOCATION-'].update(weatherdata['location']['name'])
                window['-REGION-'].update(weatherdata['location']['region'])
                window['-TIME-'].update(weatherdata['location']['localtime'])
                window['-TEMP-'].update(weatherdata['current']['temp_f'])

                # Gets image
                imageget = requests.get("https:"+weatherdata['current']['condition']['icon'])
                window['-PICTURE-'].update(data=imageget.content)
                window['-DESCRIPTION-'].update(weatherdata['current']['condition']['text'])
                window['-LONG-'].update(weatherdata['location']['lon'])
                window['-LAT-'].update(weatherdata['location']['lat'])
                window['-WINDDIR-'].update(weatherdata['current']['wind_dir'])
                window['-WINDSPEED-'].update(weatherdata['current']['wind_mph'])

            if event == 'Save':
                # Sends the data to Microservice
                port = 55441
                IP = 'IP_placeholder' # IP Address of microservice - Current set to a place holder IP
                with socket(AF_INET, SOCK_STREAM) as message:
                    message.connect((IP, port))
                    letter = self._currlocation.encode()
                    message.send(letter)
                    print("data sent")

                    # receives the terminal message
                    terminal_msg = message.recv(1024).decode()
                    print(terminal_msg)

            # IMPLEMENT F/C
            if event == 'Temp Type':
                # Load Json file
                with open('weather.json', 'r') as weather:
                    weatherdata = json.load(weather)

                if self._cel == True:
                    self._cel = False
                    window['-TEMP-'].update(weatherdata['current']['temp_f'])
                    print("Switching Temp to F")
                else:
                    self._cel = True
                    window['-TEMP-'].update(weatherdata['current']['temp_c'])
                    print("Switching Temp to C")

            # IMPLEMENT HISTORY
            if event == "History":
                # Sends the request
                port = 55441
                IP = 'IP_Where_microservice_is_running'
                with socket(AF_INET, SOCK_STREAM) as message:
                    message.connect((IP, port))
                    letter = '-0-0-0'
                    message.sendall(letter.encode())
                    print("request sent")

                    # receives the terminal message
                    terminal_msg = message.recv(1024).decode()
                    print(terminal_msg)

                    # receives the data and writes it to
                    data = message.recv(1024).decode()

                    with open('history.txt', 'w') as historydata:
                        historydata.write(data)
                    print("history written to text file")

                # Opens a new history window with the text file displayed
                with open('history.txt', 'r') as historydata:
                    print(historydata.read())

            # UNDO FEATURE
            if event == "Undo":
                if self._currlocation:
                    print("Undoing last search")

                    self._currlocation, self._prevlocation = self._prevlocation, self._currlocation

                    response = requests.get(
                        f"API_URI_placeholder{self._currlocation}")
                    jsondata = response.json()
                    with open('weather.json', 'w') as weather:
                        json.dump(jsondata, weather, indent=2)
                    print('Data collected')

                    # Load Json file
                    with open('weather.json', 'r') as weather:
                        weatherdata = json.load(weather)

                    # Updates variables
                    window['-CURLOCATION-'].update(weatherdata['location']['name'])
                    window['-REGION-'].update(weatherdata['location']['region'])
                    window['-TIME-'].update(weatherdata['location']['localtime'])
                    window['-TEMP-'].update(weatherdata['current']['temp_f'])
                    imageget = requests.get("https:" + weatherdata['current']['condition']['icon'])      # Gets image
                    window['-PICTURE-'].update(data=imageget.content)
                    window['-DESCRIPTION-'].update(weatherdata['current']['condition']['text'])
                    window['-LONG-'].update(weatherdata['location']['lon'])
                    window['-LAT-'].update(weatherdata['location']['lat'])
                    window['-WINDDIR-'].update(weatherdata['current']['wind_dir'])
                    window['-WINDSPEED-'].update(weatherdata['current']['wind_mph'])

            # 7-day-forecast page
            if event == "7-day-forecast":
                window.close()
                self.create_7_day()

            # hourly weather page
            if event == "Hourly weather summary":
                window.close()
                self.create_hourly()

        print("catch you on the flip-side")
        window.close()

    def create_7_day(self):
        """
        Creates the 7-day weather forecast window
        """
        sevenheader = [
            [py.Text("SEVEN DAY WEATHER FORECAST", font=("Helvetica", 20))]
        ]

        rightcolumn2 = [
            [py.Button("Current Weather")],
            [py.Button("Hourly weather summary")],
        ]

        # second layout
        layout2 = [
            [py.Column(sevenheader, vertical_alignment='center', justification='center')],
            [py.HSeparator()],
            [py.Text("PLACE HOLDER"), py.VerticalSeparator(pad=(50, 50)), py.Column(rightcolumn2)],
        ]

        window = py.Window("Totally Awesome Weather App", layout2, margins=(50, 50))
        while True:
            event, values = window.read()

            # when the window is closed -- what happens
            if event == py.WIN_CLOSED:
                break

            # Current weather page
            if event == "Current Weather":
                window.close()
                self.create_main()

            if event == "Hourly weather summary":
                window.close()
                self.create_hourly()

        print("catch you on the flip-side")
        window.close()

    def create_hourly(self):
        """
        Creates the hourly weather forecast window
        """
        dailyheader = [
            [py.Text("HOURLY WEATHER SUMMARY", font=("Helvetica", 20))]
        ]

        rightcolumn3 = [
            [py.Button("Current Weather")],
            [py.Button("7-day-forecast")],
        ]

        # Third layout
        layout3 = [
            [py.Column(dailyheader, vertical_alignment='center', justification='center')],
            [py.HSeparator()],
            [py.Text("PLACE HOLDER"), py.VerticalSeparator(pad=(50, 50)), py.Column(rightcolumn3)],
        ]

        window = py.Window("Totally Awesome Weather App", layout3, margins=(50, 50))
        while True:
            event, values = window.read()

            # when the window is closed -- what happens
            if event == py.WIN_CLOSED:
                break

            # Current weather page
            if event == "Current Weather":
                window.close()
                self.create_main()

            if event == "7-day-forecast":
                window.close()
                self.create_7_day()

        print("catch you on the flip-side")
        window.close()



if __name__ == '__main__':
    print("Beep-Beep Boop-Boop")
    print("program starting.....")
    app = WeatherApp()
    app.create_main()
