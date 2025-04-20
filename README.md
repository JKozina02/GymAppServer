# GymAppServer
Server with api for GymApp 

- Creating virtual envirement
`python -m venv .venv`
- Lunching virtual envirement
`.\.venv\Scripts\activate`
- Instaling dependencies inside venv
`pip install -r requirements.txt`

## Starting server

`docker-compose up --build`

## Usefull commands

Logging into database: 
1. `docker exec -it gymappdb mysql -u root -ppassword`
2. `USE gymapp;`

# Api endpoints
Api adress: `http://localhost:8000`

### Create user in database
`POST` `/create-user/` 
body
{
    `username: str`
    `email: EmailStr`
    `password: str`
}
response
{
    "status_code":num, "message":str, "user":user
}

### Checks if email is in database
`GET` `/check-user/`
body
{
    `email: EmailStr`
}
response
{
    "status_code":num, "message":str, "userExists":bool
}

### Login user returns true if success
`POST` `/login-user/`
body
{
    `email: EmailStr`
    `password: str`
}
response
{
    "status_code":num, "message":str, "loggedIn": bool
}

### Gets list of exercises, can search by name if needed
`GET` `/get-exercises/?name=`
response
{
    "status_code":num, "exercises":exercises
}

### Creates new exercise in database
`POST` `/create-exercise/`
body
{
    `name: str`
    `time: bool`
    `reps: bool`
    `weight: bool`
}
response
{
    "status_code":num, "message":str, "exercise": exercise
}
