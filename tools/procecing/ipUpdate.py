from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import time  
from faker import Faker 

# uvicorn filename:app --reload  app - это экзымпляр fast api reload - позволяет сделать так если изменим код в файле не нужно будет его перезапускать 

app = FastAPI()
faker = Faker()

app.get("/")
async def read_root(request: Request):
    return RedirectResponse(f"{request.url}docs")

app.get("/adress")
async def adress_fake_adress():
    return {"Name": faker.address(), "Timestamp": time()}

@app.get("/name")
async def get_fake_name():
    return {"Name": faker.name(), "Timestamp": time()}

@app.get("/email")
async def get_fake_email():
    return {"Email": faker.email(), "Timestamp": time()}

@app.get("/mac")
async def get_fake_mac():
    return {"Mac": faker.mac_address(), "Timestamp": time()}

@app.get("/all")
async def get_fake_all():
    return {"Name": faker.name(), 
            "Adrees": faker.address(), 
            "Email": faker.free_email(),
            "Mac": faker.mac_address(),
            "Timestamp": time()}