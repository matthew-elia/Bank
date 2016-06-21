#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp    #importing loginapp, to get a coBrand and User Session response and used
import http       #importing http, its the key for all the apps, and to post and get the json response
import json        #library package for the json response access
import yaml        #converts unicode to byte code
import requests    #requests, for requesting the response from json

#<summary>
#The HoldingAssetClassificationApp class provides Asset classifications for the holdings for a member account. 
    
    #Steps to Use this App: 
      #i) doCoBrandLogin(coBrandUserName, coBrandPassword)
      #ii) doMemberLogin(userName, userPassword)
     
      #Browse all Accounts for member profile: 
        #getHoldings() 

class HoldingAssetClassificationApp:
  fqcn = "HoldingAssetClassificationApp"
  global userSession
  global cobSession

  @staticmethod
  def getAssetClassificationHoldings():
    global userSession
    global cobSession
    
    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
 
    mn = "getAssetClassificationHoldings()"
    print((HoldingAssetClassificationApp.fqcn + " :: " + mn))
    holdingURL = loginapp.LoginApp.localURLVer1 + "v1/holdings?include=assetClassification"
    jsonResponse = http.HTTP.doGet(holdingURL, hdr)  
    parsed_json = json.loads(jsonResponse)
    node = parsed_json.get("holding",{})
    print('-----------------------------------------------------------------------------------------------------------------')
    print("holdingId - accountId - holdingType - value - classificationType - classificationValue - allocation") #description
    print('-----------------------------------------------------------------------------------------------------------------')
    for i in node:
      if ('value' in i):
        print((i['id'],"  - ",i['accountId'],"  - ",i['holdingType'],"  - ",i['value']['amount'])) #,i['description']
      else:
        print((i['id'],"  - ",i['accountId'],"  - ",i['holdingType'],"  - ","  - ")) #,i['description']
      if ('assetClassification' in i):
        classificationNode = i.get("assetClassification",{})
        for j in classificationNode:
            print(("     - ","  - ","     - ","  - ","     - ","  - ","     - ","  - ",j['classificationType'],"    -      ",j['classificationValue'],"     -    ",j['allocation']))
    print('--------------------------------------------------------------------------------------------------------------')
