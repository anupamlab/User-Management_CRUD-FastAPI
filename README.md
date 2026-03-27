# 🚀 User Management API (FastAPI + MySQL)

A lightweight and efficient **User Management REST API** built using FastAPI and MySQL.  
This project demonstrates core backend development skills including API design, database integration, validation, and structured error handling.

---

## 📌 Overview

This API enables basic user operations such as registration, authentication, and full CRUD functionality.  
It is designed with simplicity and clarity, making it ideal for understanding backend fundamentals and REST API development.

---

## ✨ Key Features

- User Registration (Signup)
- User Authentication (Login validation)
- Retrieve all users
- Retrieve user by ID
- Update user details
- Delete user
- Validation & Error handling: Input validation, Structured error handling with HTTP status codes

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Database:** MySQL  
- **Validation:** Pydantic  
- **Database Access:** MySQL Connector (Raw SQL)

---

## 📂 Project Structure

```
.
├── main.py        # API routes and business logic
├── database.py    # MySQL connection setup
├── models.py      # Pydantic schema for user input request validation (JSON)
└── .env           # Environment configuration
```

---

## ⚙️ Setup & Installation


### Install Dependencies

```
pip install -r requirements.txt
```

---

### Database Setup

Create database:

```
CREATE DATABASE testdb;
```

Create table:

```
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    age INT
);
```

---

### 4. Environment Configuration

Create `.env` file:

```
HOST=localhost
USER=root
PASSWORD=yourpassword
DATABASE=testdb
```

---

### 5. Run Application

```
pip install unicorn

python -m uvicorn main:app --reload
```

---

## 🌐 API Documentation

FastAPI provides interactive API documentation:

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 📡 API Endpoints

| Method | Endpoint       | Description            |
|--------|----------------|------------------------|
| POST   | /signup        | Register new user      |
| POST   | /login         | Authenticate user      |
| GET    | /users         | Get all users          |
| GET    | /users/{id}    | Get user by ID         |
| PUT    | /users/{id}    | Update user            |
| DELETE | /users/{id}    | Delete user            |

---

## 📥 Sample Request

```
POST /signup

{
  "username": "john",
  "password": "1234",
  "age": 25
}
```

---

## 📤 Sample Response

```
{
  "message": "User created successfully"
}
```

---

## ⚠️ Important Notes

- Uses raw SQL queries (no ORM)
- Passwords are stored in plain text (no encryption)
- Designed for learning and demonstration purposes

---

## 🚀 Learning Outcomes

- REST API design using FastAPI  
- Database integration with MySQL  
- Handling HTTP requests and responses  
- Input validation with Pydantic  
- Error handling using HTTPException  

---

## This project was developed as part of my learning journey in Python. As a learning assistant to understand concepts and structure the code took help of GPT Models. The final implementation, testing, and project setup were completed by "infoanupampal@gmail.com"


<div align="center">

Built with ❤️ by **anupamLab**

</div>

