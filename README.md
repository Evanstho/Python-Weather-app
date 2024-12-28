## Python Weather App

## Created By:
Thomas Evans. Copyright © 2023. All Rights Reserved.

## Description
Developed a weather application using Agile methodology, leveraging Python, Flask, and PySimpleGUI. The application features a user-friendly graphical interface, real time weather data and a separate microservice is implemented to collect weather data based on latitude and longitude coordinates.

## How to run
Start weatherApp.py and enter the name of the city in the search bar to retrieve weather information.

## How to save History
microservice.py must be running and weatherApp.py must be able to establish a TCP/IP connection.

## How to programmatically REQUEST data from windspeed.py
Windspeed.py can be run locally or hosted on another machine. To ensure that the microservice correctly receives the REQUEST the requesting program must establish a TCP/IP connection to the IP address where Windspeed.py is running. Next, the requesting program must send an encoded message containing the latitude and longitude. The Latitude and Longitude must be in the following format 'lat, long'.

Example call: Program requesting data establishes a TCP connection and sends an encoded message formatted as 'lat,long'.

## How to programmatically RECEIVE data from windspeed.py
In order to RECEIVE data from windspeed.py, the requesting program must establish and maintain the TCP/IP connection. The requesting program must LISTEN for a response from windspeed.py. The message containing the windspeed and wind direction will be immediately sent after the REQUEST is made as an encoded message in the following format, 'windspeed, direction'.

![CS361 - Assignment 9 UML](https://github.com/Evanstho/CS361/assets/102569958/1f76e6c8-50a4-42c9-bbe4-8edb8a714007)
