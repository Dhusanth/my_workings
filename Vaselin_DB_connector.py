import mysql.connector
import pandas as pd
import numpy as np
import json

# DB connector
mydb = mysql.connector.connect(
  host= "192.168.2.36",
  user= "dhushanth",
  passwd= "aTVH@6283vH",
  database= "vaselin"
)

mycursor = mydb.cursor()

# To check tables in DB
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)

# Select Specific table, 'log' table has been selected
mycursor.execute("select * from logs")

# extract data from the table
myresult = mycursor.fetchall()

# for x in myresult:
#  print(x)

# Define column names and make dataframes
df = pd.DataFrame(data=myresult, columns=['id','datetime','mobile','message','reply','status'])


# create json format

mobile_numbers = df['mobile']

api_push_data = []

for r in mobile_numbers:
    data ={"mobile_number":r, "src":"vaselin", "brand_name":"Vaseline", "parent_compaany":"Uniliver"}
    api_push_data.append(data)

# api_push_data
    
# write to json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
path = './'
fileName = 'vaseline'
data = api_push_data

writeToJSONFile(path, fileName, data)
   
df1 = pd.DataFrame(data=api_push_data)  
    
    
    
    