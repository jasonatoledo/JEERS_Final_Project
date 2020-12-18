# Run the line below in the directory folder of Flask_Frontend to create a virtual environment and install all dependencies.
# You may or may not have to perform this step depending on your system and the dependencies you might have already installed.
# conda env create -f environment.yml
# To run the file, follow the steps below:
# Step 1: Launch the virtaul environment with, conda activate FrontendEnv in your terminal.
# Step 2: Run the app.py file by runnning, python3 app.py or python app.py
# Step 3: A local host link should be printed into your terminal, copy and paste it into your browser window.
# If the app content is displayed in your browser, congratulations.

from flask import Flask
#from config import config
import pyodbc
import sqlalchemy as sa
from sqlalchemy import create_engine
import pandas as pd

# Database connection code.
engine = sa.create_engine('postgresql+pyodbc://postgres:JEERS123!@http://database-jeers.czgvqrcdettr.us-east-2.rds.amazonaws.com/JEERS_UFC')
conn = engine.connect()
print(engine.table_names())

result = engine.execute("select * from fighters")
for row in result:
    print(row)

result.close()

# conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello it works.</h1>"

if __name__ == '__main__':
    app.run()