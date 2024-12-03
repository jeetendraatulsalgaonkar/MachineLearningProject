from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
from typing import Optional
from uvicorn import run as app_run

from com.demo.visa.entity.Visa_model import VisaModel

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
        self.visaModel: Optional[VisaModel] = None

    async def get(self):
        form = await self.request.form()
        self.vehicle_data = form.get("vehicle_data")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("usvisa.html", {"request": request, "context": "Rendering"})


@app.post("/")
async def predictRouteClient(request: Request):
    try:
        form = DataForm(request)
        await form.get_usvisa_data()

        usvisa_data = VisaModel(
            continent=form.continent,
            education_of_employee=form.education_of_employee,
            has_job_experience=form.has_job_experience,
            requires_job_training=form.requires_job_training,
            no_of_employees=form.no_of_employees,
            company_age=form.company_age,
            region_of_employment=form.region_of_employment,
            prevailing_wage=form.prevailing_wage,
            unit_of_wage=form.unit_of_wage,
            full_time_position=form.full_time_position,
        )

        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        model_predictor = USvisaClassifier()

        value = model_predictor.predict(dataframe=usvisa_df)[0]

        status = None
        if value == 1:
            status = "Visa-approved"
        else:
            status = "Visa Not-Approved"

        return templates.TemplateResponse(
            "usvisa.html",
            {"request": request, "context": status},
        )

    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host="localhost", port=8292)