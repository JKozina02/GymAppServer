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


## Endpoints
Api adress: http://localhost:8000

### Create a New User
**POST** `/create-user/`

**Request Body (JSON):**
```json
{
  "username": "string",
  "email": "user@example.com",
  "password": "string"
}
```

**Response:**
```json
{
  "status_code": 200,
  "message": "User created successfully!",
  "user": {...}
}
```

---

### Check if User Email Exists
**GET** `/check-user/`

**Request Body (JSON):**
```json
{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "status_code": 200,
  "message": "Email valid!",
  "userExists": true
}
```

---

### User Login
**POST** `/login-user/`

**Request Body (JSON):**
```json
{
  "email": "user@example.com",
  "password": "string"
}
```

**Response:**
```json
{
  "status_code": 200,
  "message": "User logged In!",
  "loggedIn": true
}
```

---

### Get List of Exercises
**GET** `/get-exercises/`

**Query Parameters:**
- `name` (optional): Filter exercises by name.

**Example:**
```
GET /get-exercises/?name=Push-up
```

**Response:**
```json
{
  "status_code": 200,
  "exercises": [...]
}
```

---

### Create a New Exercise
**POST** `/create-exercise/`

**Request Body (JSON):**
```json
{
  "name": "string",
  "time": true,
  "reps": true,
  "weight": false
}
```

**Response:**
```json
{
  "status_code": 200,
  "message": "Exercise created successfully!",
  "exercise": {...}
}
```

---

### Update an Exercise
**PUT** `/update-exercise/{exercise_id}`

**Path Parameter:**
- `exercise_id` (integer): ID of the exercise to update.

**Request Body (JSON):**
```json
{
  "name": "new name",
  "time": true,
  "reps": false,
  "weight": true
}
```

**Response:**
```json
{
  "status_code": 200,
  "message": "Exercise updated successfully",
  "exercise": {...}
}
```

---

### Delete an Exercise
**DELETE** `/delete-exercise/{exercise_id}`

**Path Parameter:**
- `exercise_id` (integer): ID of the exercise to delete.

**Response:**
```json
{
  "status_code": 200,
  "message": "Exercise deleted successfully"
}
```

---

# Project Structure

```
app/
  ├── crud.py
  ├── database.py
  ├── schemas.py
  └── __init__.py
main.py
requirements.txt
docker-compose.yml
README.md
```

---

# Notes

- The project uses **FastAPI** for a high-performance, asynchronous REST API.
- **MySQL** database runs inside a Docker container.
- Database initialization happens automatically on server startup.
- Models, database sessions, and schemas are modularized under the `app/` directory.

---