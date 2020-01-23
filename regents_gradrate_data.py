import requests
import pandas as pd
import json
import config
from sodapy import Socrata
import mysql.connector
import numpy as np

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


# make API call for hs graduation rate data
client = Socrata("data.cityofnewyork.us", 'hs_key')
client = Socrata('data.cityofnewyork.us',
                  config.hsgrad_token,
                  username=config.od_user,
                  password=config.od_pw)
results = client.get("nb39-jx2v", limit=256000)
gradrate = pd.DataFrame.from_records(results)





# drop unwanted rows in dataframes; save as csv files
regents = regents[~regents['school_level'].isin(['K-8', 'Elementary'])]
regents.to_csv('regents.csv')

gradrate = gradrate[gradrate['cohort_year'].isin(['2013'])]
gradrate.to_csv('gradrate.csv')


# select only rows where the year is 2017
regents2017 = regents[regents['year'].isin(['2017'])]
# take out rows with inappropriate school level
regents2017 = regents2017[~regents2017.school_level.str.contains('Junior High-Intermediate-Middle')]
# regentsdf = pd.DataFrame(regents2017.loc[:, ['school_name', 'regents_exam', 'demographic_variable', 'total_tested', 'mean_score', 'number_scoring_below_65', 'percent_scoring_below_65', 'number_scoring_65_or_above', 'percent_scoring_65_or_above', 'number_scoring_80_or_above', 'percent_scoring_80_or_above', 'number_scoring_cr', 'percent_scoring_cr']])
# regents_tuples = list(regentsdf.itertuples(index=False, name=None))





# load tuples
import pickle
with open('tup.pkl', 'rb') as f:
    x = pickle.load(f)

with open('tup1.pkl', 'rb') as g:
    y = pickle.load(g)

# change list of tuples to dataframe to change nans
ydf = pd.DataFrame(y)
# change nans to null in dataframe
ydf = ydf.where((pd.notnull(ydf)), None)
ydf
# change back dataframe now updated with nones back to list of tuples
y = list(ydf.itertuples(index=False, name=None))





# split list into smaller lists
n = 10000
regents_chunks = [x[i:i+n] for i in range(0,len(x),n)]

# insert regents data into database
for chunk in regents_chunks:
    insert_regents = ("""INSERT INTO regents(
                         school_name, regents_exam, demographic, total_tested, mean_score,
                         number_scoring_below_65, percent_scoring_below_65,
                         number_scoring_65_or_above, percent_scoring_65_or_above,
                         number_scoring_80_or_above, percent_scoring_80_or_above,
                         number_scoring_cr, percent_scoring_cr)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")
    cursor.executemany(insert_regents, chunk)
    cnx.commit()


# split list into smaller lists
n = 10000
grad_chunks = [y[i:i+n] for i in range(0,len(y),n)]

# insert grad rate data into database
for chunk in grad_chunks:
    insert_gradrate = ("""INSERT INTO gradrate(
                         school_name, demographic, cohort, total_cohort,
                         total_grads, total_grads_of_cohort)
                         VALUES (%s, %s, %s, %s, %s, %s);""")
    cursor.executemany(insert_gradrate, chunk)
    cnx.commit()




# create tuples long way
def make_num (stuff):
    try:
        y=float(stuff)
    except:
        y=None
    return y

i=0
regents_tuple_nums=[]
for thing in range(len(list(regents2017['school_name']))):
    new_tuple = (list(regents2017['school_name'])[i],
                list(regents2017['regents_exam'])[i],
                list(regents2017['demographic_variable'])[i],
                list(regents2017['total_tested'])[i],
                make_num (list(regents2017['mean_score'])[i]),
                make_num (list(regents2017['number_scoring_below_65'])[i]),
                make_num (list(regents2017['percent_scoring_below_65'])[i]),
                make_num (list(regents2017['number_scoring_65_or_above'])[i]),
                make_num (list(regents2017['percent_scoring_65_or_above'])[i]),
                make_num (list(regents2017['number_scoring_80_or_above'])[i]),
                make_num (list(regents2017['percent_scoring_80_or_above'])[i]),
                make_num (list(regents2017['number_scoring_cr'])[i]),
                make_num (list(regents2017['percent_scoring_cr'])[i]))
    print (new_tuple)
    regents_tuple_nums.append(new_tuple)
    i+=1

# split list into smaller lists
n = 10000
regents_chunks = [regents_tuple_nums[i:i+n] for i in range(0,len(regents_tuple_nums),n)]

# insert regents data into database
for chunk in regents_chunks:
    insert_regents = ("""INSERT INTO regents(
                         school_name, regents_exam, demographic, total_tested, mean_score,
                         number_scoring_below_65, percent_scoring_below_65,
                         number_scoring_65_or_above, percent_scoring_65_or_above,
                         number_scoring_80_or_above, percent_scoring_80_or_above,
                         number_scoring_cr, percent_scoring_cr)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")
    cursor.executemany(insert_regents, chunk)
    cnx.commit()





# regents dataframe
cursor.execute("""SELECT * FROM regents;""")
regents = pd.DataFrame(cursor.fetchall())
regents.columns = [x[0] for x in cursor.description]
regents.to_csv('regents.csv')
# finalize regents dataframe
regents = regents[regents['demographic'].isin(['All Students'])]
# regents = regents.dropna()
regents = regents.drop(columns=['Unnamed: 0', 'demographic', 'total_tested', 'mean_score', 'number_scoring_below_65','percent_scoring_below_65', 'number_scoring_65_or_above', 'number_scoring_80_or_above', 'percent_scoring_80_or_above', 'number_scoring_cr','percent_scoring_cr'])
regents.to_csv('regentsfinal.csv')


# graduation rate dataframe
cursor.execute("""SELECT * FROM gradrate;""")
grad = pd.DataFrame(cursor.fetchall())
grad.columns = [x[0] for x in cursor.description]
grad.to_csv('grad.csv')
# finalize graduation rate dataframe
grad = pd.read_csv('grad.csv')
grad = grad[(grad['cohort'].isin(['4 year June'])) & (grad['demographic'].isin(['All Students']))]
grad = grad.drop(columns=['Unnamed: 0', 'demographic', 'cohort'])
grad = grad.sort_values(by=['school_name']).reset_index()
grad.to_csv('gradfinal.csv')


# attendance dataframe
cursor.execute("""SELECT * FROM attendance""")
att = pd.DataFrame(cursor.fetchall())
att.columns = [x[0] for x in cursor.description]
att.to_csv('attendance.csv')
# finalize attendance dataframe
att = pd.read_csv('attendance.csv')
att = att.drop(columns=['Unnamed: 0'])
att = att.sort_values(by=['school_name']).reset_index()
att = att.drop([1])
att.to_csv('attendancefinal.csv')


# teacher qualifications dataframe
cursor.execute("""SELECT * FROM teacher_qualifications""")
teach_qual = pd.DataFrame(cursor.fetchall())
teach_qual.columns = [x[0] for x in cursor.description]
teach_qual.to_csv('teacher_qualifications.csv')
