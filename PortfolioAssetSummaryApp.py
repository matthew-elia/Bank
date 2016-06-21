#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp    #importing loginapp, to get a coBrand and User Session response and used
import http       #importing http, its the key for all the apps, and to post and get the json response
import json        #library package for the json response access
import yaml        #converts unicode to byte code
import requests    #requests, for requesting the response from json

#<summary>
#The PortfolioAssetSummaryApp class provides summary of Asset Classifications with value. 
    
    #Steps to Use this App: 
      #i) doCoBrandLogin(coBrandUserName, coBrandPassword)
      #ii) doMemberLogin(userName, userPassword)
     
      #Browse all Accounts for member profile: 
        #getAssetSummary() 

class PortfolioAssetSummaryApp:
  fqcn = "DerivedHoldingSummaryApp"
  global userSession
  global cobSession

  @staticmethod
  def getAssetSummary():
    global userSession
    global cobSession
    
    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
 
    mn = "getAssetSummary()"
    print((PortfolioAssetSummaryApp.fqcn + " :: " + mn))
    portfolioURL = loginapp.LoginApp.localURLVer1 + "v1/derived/holdingSummary?include=details"
    jsonResponse = http.HTTP.doGet(portfolioURL, hdr)  
    parsed_json = json.loads(jsonResponse)
    node = parsed_json.get("holdingSummary",{})
    print('------------------------------------------------------------------------------------------------')
    print("classificationType - classificationValue - amount - holdingId - accountId - value")
    print('------------------------------------------------------------------------------------------------')
    for i in node:
        print((i['classificationType'],"  - ",i['classificationValue'],"  - ",i['value']['amount']))
        holding = i.get("holding",{})
        for j in holding:
          if ('value' in j):
            print(("  - ","  - ","  - ","  - ","  - ","  - ",j['id'],"  - ",j['accountId'],"  - ",j['value']['amount']))
          else:
            print(("  - ","  - ","  - ","  - ","  - ","  - ",j['id'],"  - ",j['accountId'],"  - ","  - "))
    print('-------------------------------------------------------------------------------------------------')
