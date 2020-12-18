# Import Dependencies
from flask import Flask
# Import sqlalchemy and create engine connection
import sqlalchemy as sa
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# Database connection code.
engine = create_engine('postgresql+psycopg2://postgres:JEERS123!@database-jeers.czgvqrcdettr.us-east-2.rds.amazonaws.com')
conn = engine.connect()
print(engine.table_names())

"""
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
"""