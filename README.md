## Python Weather App

## Created By:
Thomas Evans

## Description
A weather application developed using Agile methodology, leveraging Python and PySimpleGUI.
The application features a user-friendly graphical interface, real time weather data.
A separate microservice is implemented to collect weather data based on receiving latitudinal and longitudinal coordinates.

## How to run
Start weatherApp.py and enter the name of the city in the search bar to retrieve weather information.

### How to save History
microservice.py must be running and weatherApp.py must be able to establish a TCP/IP connection with microservice.py.

## How to programmatically REQUEST data from windspeed.py
Windspeed.py can be run locally or hosted on another machine. To ensure that the microservice correctly receives the REQUEST, and the requesting program must establish and maintain a TCP/IP connection with Windspeed.py. Next, the requesting program must send an encoded message containing the latitude and longitude. The Latitude and Longitude must be in the following format 'lat, long'.

Example call: Program requesting data establishes a TCP connection and sends an encoded message formatted as 'lat,long'.

## How to programmatically RECEIVE data from windspeed.py
In order to RECEIVE data from windspeed.py, the requesting program must establish and maintain a TCP/IP connection and the requesting program must LISTEN for a response from windspeed.py. The message containing the windspeed and wind direction will be immediately sent after the REQUEST is made as an encoded message in the following format, 'windspeed, direction'.

![CS361 - Assignment 9 UML](https://github.com/Evanstho/CS361/assets/102569958/1f76e6c8-50a4-42c9-bbe4-8edb8a714007)

Copyright © 2023. All Rights Reserved.
