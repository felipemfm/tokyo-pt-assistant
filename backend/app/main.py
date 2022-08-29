# uvicorn app.main:app --reload

from fastapi import FastAPI

from app.api import api

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/railway")
def read_railway_data():
    return api.read_railway_data()


@app.get("/railway/{line_or_station}")
def read_railway_data_by(line_or_station):
    return api.read_railway_data_by(line_or_station)

@app.get("/railway/stationTimeTable/{operator}/{station}/{line}/{direction}")
def get_station_time_table(operator, line, station, direction):
    return api.get_station_time_table(operator, line, station, direction)