# Run the line below in the directory folder of Flask_Frontend to create a virtual environment and install all dependencies.
# You may or may not have to perform this step depending on your system and the dependencies you might have already installed.
# conda env create -f environment.yml
# To run the file, follow the steps below:
# Step 1: Launch the virtaul environment with, conda activate FrontendEnv in your terminal.
# Step 2: Run the app.py file by runnning, python3 app.py or python app.py
# Step 3: A local host link should be printed into your terminal, copy and paste it into your browser window.
# If the app content is displayed in your browser, congratulations.

from flask import Flask, jsonify, render_template, request
from config import db_pwd
import pyodbc
import psycopg2
import datetime as dt
import numpy as np
import pandas as pd
# SQLalchemy
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Configure Flask App
app = Flask(__name__)

# Create App Routes
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

# DATABASE CONNECTION AND QUERIES BELOW THIS LINE
db_string1 = f"postgres://postgres:{db_pwd}@127.0.0.1:5432/database_name"
db_string2 = f"postgresql+psycopg2://postgres:{db_pwd}@database-jeers.czgvqrcdettr.us-east-2.rds.amazonaws.com"
db_string3 = f"postgresql+pyodbc://postgres:{db_pwd}@http://database-jeers.czgvqrcdettr.us-east-2.rds.amazonaws.com/JEERS_UFC"

# Database connection code.
engine = create_engine(db_string)
engine = sa.create_engine(db_string)
conn = engine.connect()

# Create cursor object.
cur = conn.cursor()

# Queries
cur.execute("""SELECT * FROM fighters""")
query_results = cur.fetchall()
print(query_results)
print(engine.table_names())

print(engine.table_names())

result = engine.execute("select * from fighters")
for row in result:
    print(row)

# Close the cursor and the connection
result.close()
cur.close()
conn.close()






'''
engine = create_engine("db_string")
Base = automap_base()

Base.prepare(engine, reflect=True)
app = Flask(__name__)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

@app.route('/api/v1.0/home')
def welcome():
    return(

    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    '''