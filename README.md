# CS361
Software engineering 1 - Weather Application

How to programmatically REQUEST data from the microservice (windspeed.py)

Windspeed.py can be run locally or hosted on another machine. To ensure that the microservice correctly receives the REQUEST ensure that the requesting program establishes a TCP connection to the IP address of where windspeed.py is running. Next, the requesting program must send an encoded message containing the latitude and longitude. The Latitude and Longitude must be in the following format "lat,long".

Example call: Program requesting data establishes a TCP connection and sends an encoded message formatted as 'lat,long'.

How to programmatically RECEIVE data from the microservice (windspeed.py)

In order to receive data from the windspeed.py microservice, the requesting program will need to maintain the TCP connection initally established when a request was sent. The requesting program must be listening for a response from the microservice. The message containing the windspeed and wind direction will be immediately sent after the request is made as an encoded message in the following format, "windspeed, direction".

![CS361 - Assignment 9 UML](https://github.com/Evanstho/CS361/assets/102569958/1f76e6c8-50a4-42c9-bbe4-8edb8a714007)
