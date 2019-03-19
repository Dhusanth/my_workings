import mysql.connector
import pandas as pd
import numpy as np
import json
import re

# DB connector - Table subscriber
mydb = mysql.connector.connect(
  host= "192.168.2.36",
  user= "dhushanth",
  passwd= "aTVH@6283vH",
  database= "ssp"
)

mycursor = mydb.cursor()

# To check tables in DB
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

mycursor.execute("select * from subscribers")

subscribers = mycursor.fetchall()

subscribers_data = pd.DataFrame(data=subscribers)
subscribers_data.head(5)

# Select 3 columns 'subscriber_id', 'subscriber_mobile', 'service_code'
subscribers1 = subscribers_data.loc[: , [0,1,3]]
subscribers1.head(5)

# Rename Column
subscribers_new_data = subscribers1.rename(columns={0:"subscriber_id", 1:"subscriber_mobile", 3:"service_code"})
subscribers_new_data.head()

# subscribers_new_data = pd.DataFrame(data=subscribers1, columns=['subscriber_id', 'subscriber_mobile', 'service_code'])

# DB connector - Table Service
mydb1 = mysql.connector.connect(
  host= "192.168.2.36",
  user= "dhushanth",
  passwd= "aTVH@6283vH",
  database= "ssp"
)

mycursor1 = mydb1.cursor()
mycursor1.execute("select * from services")

services = mycursor1.fetchall()
services_data = pd.DataFrame(data=services)

# Select 4 columns "service_code","service_name","mtr_comment","parent_code"
services1 = services_data.loc[: , [0,1,3,4]]

# Rename Column
services_new_data = services1.rename(columns={0:"service_code", 1:"service_name", 3:"mtr_comment", 4:"parent_code"})

finaldata = pd.merge(subscribers_new_data, services_new_data)
finaldata.head(5)

Export = finaldata.to_json (r'./vasabi.json')







