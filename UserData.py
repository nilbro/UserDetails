from urllib import response
import requests
import json
import sqlite3

def authoriseData():
#this function performs basic authentication with Client Id and Client Secret obtained from the application website and username and password as header parameters
#It returns access token and refresh token 
 

    url = "https://coyotraining.coyocloud.com/api/oauth/token?grant_type=password&username=RL&password=demo"

    payload={}
    files={}
    headers = {
    'Authorization': 'Basic VGVzdGluZ2luMTIzOjkwYWEwYzA4LTVjNmQtNDQ1Ni04Y2MzLWM5ODJkZDJiZWFkZA==',
    'Cookie': 'COYOSESSION=NTlhZTFmNjEtNDZjMy00Y2ZjLTkxMzktMWI5YmM4ZWVjYWU1'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)




def accessData():
#this function access user resources from the endpoint URL by passing access token as the Authorization header
   url = "https://coyotraining.coyocloud.com/api/users/admin/export"

   payload={}
   headers = {
     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiY295byJdLCJleHRlcm5hbCI6ZmFsc2UsInVzZXJfbmFtZSI6ImYwNTQ1MGMxLWM1MjYtNDExNC05NDZkLTdkNzA4YTU3YWVhNiIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE2NDU2NDY4MjMsImF1dGhvcml0aWVzIjpbIk1BTkFHRV9VU0VSX0RJUkVDVE9SSUVTIiwiU1dJVENIX0hPTUVQQUdFX0tJVCIsIk1BTkFHRV9USEVNRVMiLCJERUxFVEVfV09SS1NQQUNFIiwiREVMRVRFX0NPTU1FTlQiLCJNQU5BR0VfTEFOR1VBR0VTIiwiTUFOQUdFX0xJQ0VOU0UiLCJNQU5BR0VfRkVBVFVSRVMiLCJDUkVBVEVfV09SS1NQQUNFIiwiTUFOQUdFX1RFUk1TIiwiTUFOQUdFX1NUQVRJU1RJQ1MiLCJNQU5BR0VfVVNFUiIsIk1BTkFHRV9VU0VSU19HUk9VUFNfUk9MRVMiLCJQRVJTT05BTF9MQVVOQ0hQQUQiLCJBQ0NFU1NfT1dOX1VTRVJfUFJPRklMRSIsIkRFTEVURV9QQUdFIiwiTUFOQUdFX0dBTUlGSUNBVElPTiIsIkNSRUFURV9TSEFSRSIsIkFVVE9fU1VCU0NSSUJFX1BBR0UiLCJDUkVBVEVfRVZFTlQiLCJNQU5BR0VfSk9CUyIsIlBFUk1JVF9HUk9VUF9JTlZJVEVTIiwiTUFOQUdFX1NFVFRJTkdTIiwiRU5HQUdFX1RJTUVMSU5FX0VOQUJMRUQiLCJVU0VfSEFTSFRBR1MiLCJTRUFSQ0giLCJBQ0NFU1NfQ09MTEVBR1VFX0xJU1QiLCJBQ1RfQVNfU0VOREVSIiwiTUFOQUdFX0ZJTEVTIiwiTUFOQUdFX0FQUFNfUEFHRSIsIlNFTkRfUFVTSF9OT1RJRklDQVRJT05TIiwiQUNDRVNTX0dfU1VJVEVfSU5URUdSQVRJT04iLCJNQU5BR0VfQVVUSEVOVElDQVRJT05fUFJPVklERVJfQ09ORklHUyIsIlBFUk1JVF9XT1JLU1BBQ0VfSU5WSVRFUyIsIk1BTkFHRV9QVUJMSUNfTElOS1MiLCJMSUtFIiwiTUFOQUdFX01BSU5URU5BTkNFIiwiQ1JFQVRFX1BVQkxJQ19QQUdFIiwiTUFOQUdFX0xBTkRJTkdfUEFHRVMiLCJQRVJNSVRfUEFHRV9JTlZJVEVTIiwiQUNUX0FTX1NFTkRFUl9MT0NBTExZIiwiTUFOQUdFX0dMT0JBTF9XSURHRVRTIiwiUk9MRV9JTlRFUk5BTF9VU0VSIiwiQUNDRVNTX05FV1MiLCJNQU5BR0VfTk9USUZJQ0FUSU9OX1NFVFRJTkdTIiwiTUFOQUdFX0FQUFNfV09SS1NQQUNFIiwiQ1JFQVRFX1JFUE9SVFMiLCJNQU5BR0VfUEFHRSIsIlBFUk1JVF9XT1JLU1BBQ0VfRVhURVJOQUxfSU5WSVRFUyIsIkNPWU9fVVNFUiIsIkNSRUFURV9TVElDS1lfVElNRUxJTkVfSVRFTSIsIkFDQ0VTU19BTkFMWVRJQ1MiLCJDUkVBVEVfUkVTVFJJQ1RFRF9USU1FTElORV9JVEVNIiwiTUFOQUdFX1BST0ZJTEVfRklFTERTIiwiVVNFX01FU1NBR0lORyIsIk1BTkFHRV9BUElfQ0xJRU5UUyIsIk1BTkFHRV9SRVBPUlRTIiwiRU5BQkxFX01PREVSQVRPUl9NT0RFIiwiRk9MTE9XX1VTRVIiLCJNQU5BR0VfUEFHRV9DQVRFR09SSUVTIiwiTUFOQUdFX1BMVUdJTlMiLCJBQ0NFU1NfTk9USUZJQ0FUSU9OUyIsIkNSRUFURV9QQUdFIiwiQUNDRVNTX0ZJTEVTIiwiTUFOQUdFX1dPUktTUEFDRSIsIk1BTkFHRV9BQ0NPVU5UX1NFVFRJTkdTIiwiQUNDRVNTX1BBR0VTIiwiRk9MTE9XX1BBR0UiLCJBQ0NFU1NfTEFVTkNIUEFEIiwiQUNDRVNTX09USEVSX1VTRVJfUFJPRklMRSIsIkFDQ0VTU19MQU5ESU5HX1BBR0VTIiwiREVMRVRFX1RJTUVMSU5FX0lURU0iLCJFRElUX0lOX01TT0ZGSUNFIiwiQUNDRVNTX0VWRU5UUyIsIkVOR0FHRV9IT01FUEFHRVNfRU5BQkxFRCIsIkFDQ0VTU19PRkZJQ0VfMzY1X0lOVEVHUkFUSU9OIiwiTUFOQUdFX0VWRU5UIiwiTUFOQUdFX0xBVU5DSFBBRCIsIk1BTkFHRV9TRUNVUklUWSIsIk1BTkFHRV9UT1BJQ1MiLCJNQU5BR0VfV09SS1NQQUNFX0NBVEVHT1JJRVMiLCJBQ0NFU1NfUEVSU09OQUxfVElNRUxJTkUiLCJBQ0NFU1NfV09SS1NQQUNFUyIsIkNSRUFURV9USU1FTElORV9JVEVNIiwiQ1JFQVRFX0NPTU1FTlQiXSwianRpIjoidEVvWFMzRmt4cnJfRjYxa3FtR2dwYUFVZFMwIiwidGVuYW50IjoiZWNlN2Q2YzItOThiOC00NDQyLWE4ZGEtZjZlOWNiN2Q2MGU3IiwiY2xpZW50X2lkIjoiVGVzdGluZ2luMTIzIiwibW9kZXJhdG9yX21vZGUiOmZhbHNlfQ.7vTLazcRltBJdtkioktLrllBxAKL2Z6TQAXodpbK61c',
     'Cookie': 'COYOSESSION=NmE4YWIyMjAtMzFjNy00ZTRlLWE3YTYtNjkxMjYzYjg5MWFj'
   }

   response = requests.request("GET", url, headers=headers, data=payload)
   
   return response.text


def createConnection():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    return con,cur

def createTable():
    con,cur=createConnection()
    cur.execute('''CREATE TABLE Userdetails
               (username text, email text, lastlogin real)''')

def insertIntoDB(responseReceived):

    #response recieved from server is converted to json
    con,cur=createConnection()
    y=json.loads(responseReceived)
    x=y["content"]
    for i in range(len(x)):
        displayname=x[i]["displayName"]
        email=x[i]["email"]
        try:
            lastlogin=x[i]["lastLogin"]
        except KeyError:
            lastlogin=0

        cur.execute("insert into Userdetails (username, email, lastlogin) values (?, ?, ?)",
                (displayname, email, lastlogin))

    con.commit()
    con.close()
 


def printResults():
#this prints the contents of the database 
    cur,con = createConnection()
    for row in cur.execute('SELECT * FROM  Userdetails'):
        print(row)
    con.commit()
    con.close()
 



authoriseData()
responseReceived = accessData()
createTable()
insertIntoDB(responseReceived)
printResults()