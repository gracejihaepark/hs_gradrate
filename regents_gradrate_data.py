import requests
import pandas as pd
import json
import config
from sodapy import Socrata
import mysql.connector

# create connection
cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = 'nyc_public_high_schools_grad_rate',
    use_pure=True
    )

cursor = cnx.cursor()


# make API call for hs regents data
client = Socrata("data.cityofnewyork.us", 'hs_key')
client = Socrata('data.cityofnewyork.us',
                  config.hsregent_token,
                  username=config.od_user,
                  password=config.od_pw)
results = client.get("csps-2ne9", limit=215000)
regents = pd.DataFrame.from_records(results)
regents


# make API call for hs graduation rate data
client = Socrata("data.cityofnewyork.us", 'hs_key')
client = Socrata('data.cityofnewyork.us',
                  config.hsgrad_token,
                  username=config.od_user,
                  password=config.od_pw)
results = client.get("nb39-jx2v", limit=256000)
gradrate = pd.DataFrame.from_records(results)
gradrate


cursor.execute("""SELECT * FROM attendance""")
attendance = cursor.fetchall()

attendance
