#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp     #importing loginapp, to get a coBrand and User Session response and used
import http        #importing http, its the key for all the apps, and to post and get the json response
import json         #library package for the json response access
import yaml         #converts unicode to byte code
import requests     #requests, for requesting the response from json

#<summary>
#The TransactionApp class provides Transaction details. 

  #Steps to Use this App: 
      #i) doCoBrandLogin(coBrandUserName, coBrandPassword)
      #ii) doMemberLogin(userName, userPassword)
     
     #Browse all Accounts for member profile: 
       #getTransactions() 

class TransactionApp:
  fqcn = "TransactionApp"
  global userSession
  global cobSession

  @staticmethod
  def getTransactions():
    global userSession
    global cobSession
  
    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    
    mn = "getTransactions()"
    print((TransactionApp.fqcn + " :: " + mn))
    transactionsURL = loginapp.LoginApp.localURLVer1 + "v1/transactions/"
    jsonResponse = requests.get(transactionsURL,headers=hdr)
    response = jsonResponse.text
    parsed_json = json.loads(response)
    print(parsed_json)
    node = parsed_json.get("transaction",{})

    print('--------------------------------------------------')
    print("Container  - Amount  - BaseType")
    print('--------------------------------------------------')
    for i in node:
      if('amount' in i):
        print((i['CONTAINER'],"  - ",i['amount']['amount'],"  - ",i['baseType']))
      elif(not('amount' in i)):
        print((i['CONTAINER'],"  - ",'0',"  - ",i['baseType']))
    print('--------------------------------------------------')
