from fastapi import FastAPI, HTTPException
from database import cursor, db
from models import User

app = FastAPI()

# -------------------------------
# Helper function: format DB data
# -------------------------------
def format_users(data):
    return [
        {
            "id": row[0],
            "username": row[1],
            "password": row[2],
            "age": row[3]
        }
        for row in data
    ]

# -------------------------------
# 1. SIGNUP API (Create user)
# -------------------------------
@app.post("/signup")
def signup(user: User):
    query = "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)"
    values = (user.username, user.password, user.age)

    cursor.execute(query, values)
    db.commit()

    return {"message": "User created successfully"}

# -------------------------------
# 2. LOGIN API (Check user)
# -------------------------------
@app.post("/login")
def login(user: User):
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    values = (user.username, user.password)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# -------------------------------
# 3. GET ALL USERS
# -------------------------------
@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return format_users(result)

# -------------------------------
# 4. GET USER BY ID
# -------------------------------
@app.get("/users/{id}")
def get_user(id: int):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": result[0],
        "username": result[1],
        "password": result[2],
        "age": result[3]
    }

# -------------------------------
# 5. UPDATE USER
# -------------------------------
@app.put("/users/{id}")
def update_user(id: int, user: User):
    query = "UPDATE users SET username=%s, password=%s, age=%s WHERE id=%s"
    values = (user.username, user.password, user.age, id)

    cursor.execute(query, values)
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}

# -------------------------------
# 6. DELETE USER
# -------------------------------
@app.delete("/users/{id}")
def delete_user(id: int):
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}