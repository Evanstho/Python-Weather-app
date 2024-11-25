# Microservice for mortar calculator
import requests
import json

from socket import *

# Establish connection
port = 55441
ip = '0.0.0.0'
print(f"Server running on: {ip}, {port})")
alpha = False
with (socket(AF_INET, SOCK_STREAM) as serv):
    serv.bind((ip, port))
    serv.listen(1)
    while True:
        connection, addr = serv.accept()

        print(f"Accepted connection from {addr[0]} on {addr[1]} ")
        rec = connection.recv(4096).decode()

        print(f"Received Data: {rec}")
        if rec:

            # API CALL
            print("Making api call...")
            response = requests.get(f"Api_uri_placeholder{rec}")
            data = response.json()

            # Saving information into json file
            with open('wind.json', 'w') as wind:
                winddirspeed = json.dump(data, wind, indent=2)

            # sending parsed information
            print(f"sending info...")
            pinfo = str(data['current']['wind_mph']) + ', ' + str(data['current']['wind_dir'])
            connection.send(pinfo.encode())
