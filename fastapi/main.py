from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()
class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas : List[Tea] = []

@app.get("/")
def read_root():
    return {"message":"Hello from the root, whatup"}

@app.get("/allteas")
def allteas():
    return teas

@app.post("/teas")
def get_teas(tea:Tea):
    teas.append(tea)
    return teas

@app.put("/tea/{tea_id}")
def edit_tea(tea_id:int, updated_tea:Tea):
     for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
     return {"error":"No tea available"}

@app.delete("/tea/{tea_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return {"message" :f"Deleted tea : {deleted.name}"}
    return {"error":"Could not delete the specified"}