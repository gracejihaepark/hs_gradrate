import requests
import pandas as pd
import json
import config
from sodapy import Socrata
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats

# create connection
cnx = mysql.connector.connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = 'nyc_public_high_schools_grad_rate',
    use_pure=True
    )

cursor = cnx.cursor()


# load dataframes
regents = pd.read_csv('regents.csv')
grad = pd.read_csv('grad.csv')
att = pd.read_csv('attendance.csv')
teach_qual = pd.read_csv('teacher_qualifications.csv')
