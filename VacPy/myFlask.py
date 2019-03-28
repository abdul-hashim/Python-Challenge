import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
# session = scoped_session(sessionmaker(bind=engine))
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def HomePage():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all Measurement names"""
    # Query all precipitations
    latest_date = session.query(Measurement.date).\
        order_by(Measurement.date.desc()).\
        first()
    tempT = latest_date[0]
    myDate = dt.date(year=int(tempT[0:4]), month=int(tempT[5:7]), day=int(tempT[8:10]))
    query_date = myDate - dt.timedelta(days=365)

    # Perform a query to retrieve the date and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
          filter(Measurement.date >= query_date).all()
     
    all_Measurements = []
    for date, prcp in results:
        Measurement_dict = {}
        Measurement_dict["date"] = date
        Measurement_dict["prcp"] = prcp
        all_Measurements.append(Measurement_dict)


    return jsonify(all_Measurements)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of Measurement data including the name, age, and sex of each Measurement"""
    # Query all Stations
    results = session.query(Station.station).all()

    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    station_tmp = session.query(Measurement.station).all()

    latest_date = session.query(Measurement.date).\
        order_by(Measurement.date.desc()).\
        first()
    tempT = latest_date[0]

    myDate = dt.date(year=int(tempT[0:4]), month=int(tempT[5:7]), day=int(tempT[8:10]))
    query_date = myDate - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.tobs).\
          filter(Measurement.date >= query_date).all()

    all_tobs = []
    for tobs in results:
        all_tobs.append(tobs)
        
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()

    myData = []

    for temps in results:
        myData.append(temps)

    return jsonify(myData)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    myData = []

    for temps in results:
        myData.append(temps)

    return jsonify(myData)


if __name__ == '__main__':
    app.run(debug=True)