from fastapi import FastAPI, Path, Annotated, HTTPException
from starlette import status

app = FastAPI()

users: dict[str, {"1": "Имя: Example, возраст: 18"}]


@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  next_id = str(max(int(k) for k in users.keys()) + 1)
  users[next_id] = f"Имя: {username}, возраст: {age}"
  return f"User {next_id} is registered"

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    next_id = str(max(int(k) for k in users.keys()) + 1)  # Находим следующий ID
    users[next_id] = f"Имя: {username}, возраст: {age}"
    return f"User {next_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
