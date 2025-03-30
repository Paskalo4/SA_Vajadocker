#!/bin/bash

# Preverite, ali obstajajo mape Client_side in Server_side
if [ ! -d "./Client_side" ]; then
    echo "Napaka: mapa Client_side ni najdena!"
    exit 1
fi

if [ ! -d "./Server_side" ]; then
    echo "Napaka: mapa Server_side ni najdena!"
    exit 1
fi

# Ustvarimo Docker omrežje
docker network create my_network

# Zgradimo Docker slike za odjemalca in strežnik
docker build -t flask-client ./Client_side
docker build -t flask-server ./Server_side

# Zaženemo Docker vsebnike v omrežju
docker run -d --name server --network my_network flask-server
docker run -d --name client --network my_network -p 8080:8080 flask-client

# Izpišemo IP naslov odjemalca
CLIENT_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client)
echo "IP naslov odjemalca: $CLIENT_IP"

# Izpišemo vse aktivne vsebnike
docker ps
