from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API de Autos y Reservas")

# --- MODELOS ---
class Auto(BaseModel):
    id: int
    marca: str
    modelo: str

class Reserva(BaseModel):
    id: int
    auto_id: int
    cliente: str

# --- BASE DE DATOS VOLÁTIL (Simulada) ---
db_autos = []
db_reservas = []

# --- CRUD AUTOS ---
@app.get("/autos", response_model=List[Auto])
def obtener_autos():
    return db_autos

@app.post("/autos")
def crear_auto(auto: Auto):
    db_autos.append(auto)
    return {"msg": "Auto registrado"}

# --- CRUD RESERVAS ---
@app.get("/reservas", response_model=List[Reserva])
def obtener_reservas():
    return db_reservas

@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    # Validar si el auto existe
    if not any(a.id == reserva.auto_id for a in db_autos):
        raise HTTPException(status_code=404, detail="El auto no existe")
    db_reservas.append(reserva)
    return {"msg": "Reserva creada"}