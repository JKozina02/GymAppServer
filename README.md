# GymAppServer
Server with api for GymApp 

## Creating virtual envirement
 - `python -m venv .venv`
## Lunching virtual envirement
 - `.\.venv\Scripts\activate`
## Instaling dependencies inside venv
 - `pip install -r requirements.txt`

# Starting server

`docker-compose up --build`

## Usefull commands

Logging into database: 
1. `docker exec -it gymappdb mysql -u root -ppassword`
2. `USE gymapp;`