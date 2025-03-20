from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Base de datos simulada (lista en memoria)
users_db = []

# Modelo de usuario
class User(BaseModel):
    name: str
    age: int
    email: str

# Endpoint POST para guardar usuario
@app.post("/user")
def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuario guardado", "user": user}

# Endpoint GET para obtener usuario guardado
@app.get("/user")
def get_users():
    return {"users": users_db}
