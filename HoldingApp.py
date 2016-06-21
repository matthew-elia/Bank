#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp    #importing loginapp, to get a coBrand and User Session response and used
import http       #importing http, its the key for all the apps, and to post and get the json response
import json        #library package for the json response access
import yaml        #converts unicode to byte code
import requests    #requests, for requesting the response from json

#<summary>
#The HoldingApp class provides holdings for a member account. 
    #Holdings are Investment accounts which a member has aggregated using Aggregation Apps.
    
    #Steps to Use this App: 
      #i) doCoBrandLogin(coBrandUserName, coBrandPassword)
      #ii) doMemberLogin(userName, userPassword)
     
      #Browse all Accounts for member profile: 
        #getHoldings() 

class HoldingApp:
  fqcn = "HoldingApp"
  global userSession
  global cobSession

  @staticmethod
  def getHoldings():
    global userSession
    global cobSession
    
    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
 
    mn = "getHoldings()"
    print((HoldingApp.fqcn + " :: " + mn))
    holdingURL = loginapp.LoginApp.localURLVer1 + "v1/holdings/"
    jsonResponse = http.HTTP.doGet(holdingURL, hdr)  
    parsed_json = json.loads(jsonResponse)
    node = parsed_json.get("holding",{})
    print('--------------------------------------------------')
    print("holdingType - price.amount - price.currency - quantity")
    print('--------------------------------------------------')
    for i in node:
      #print i
      if ('price' in i and 'quantity' in i):
        print((i['holdingType'],"  - ",i['price']['amount'],"  - ",i['price']['currency'],"  - ",i['quantity']))
      elif (('price' in i) and not ('quantity' in i)):
        print((i['holdingType'],"  - ",i['price']['amount'],"  - ",i['price']['currency'],"  - "))
      elif (not ('price' in i) and ('quantity' in i)):
        print((i['holdingType'],"  - ","  - ","  - ","  - ","  - ",i['quantity']))
    print('--------------------------------------------------')
