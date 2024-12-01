from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
from typing import Optional
from uvicorn import run as app_run

from vehicle.domain.vehicle_data import VehicleData

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm:
    def __init__(self, request, Request):
        self.request: Request = request
        self.vehicle_data: Optional[VehicleData] = None

    async def get(self):
        form = await self.request.form()
        self.vehicle_data = form.get("vehicle_data")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("vehicleData.html", {"request": request, "context": "Rendering"})


if __name__ == "__main__":
    app_run(app, host="localhost", port=8292)