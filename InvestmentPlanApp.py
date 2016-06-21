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

class InvestmentPlanApp:
  fqcn = "InvestmentPlanApp"
  global userSession
  global cobSession

  @staticmethod
  def getInvestmentOptions():
    global userSession
    global cobSession
    
    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
 
    mn = "getInvestmentOptions()"
    print((InvestmentPlanApp.fqcn + " :: " + mn))
    portfolioURL = loginapp.LoginApp.localURLVer1 + "v1/accounts/investmentPlan/investmentOptions?include=assetClassification"
    jsonResponse = http.HTTP.doGet(portfolioURL, hdr)  
    parsed_json = json.loads(jsonResponse)
    node = parsed_json.get("account",{})
    print('IP --> InvestmentPlan')
    print('IO --> InvestmentOption')
    print('-------------------------------------------------------------------------------------------------------')
    print("AccountId - IP.planName - IP.providerName - IO.cusipNumber - IO.description - IO.holdingType - IO.price")
    print('-------------------------------------------------------------------------------------------------------')
    for i in node:
     # print i
      if ('investmentPlan' in i):
          #print i
          print((i['id'],"  - ",i['investmentPlan']['planName'],"  - ",i['investmentPlan']['providerName']))
          io = i.get("investmentoption",{})
          #print io
          for j in io:
            if ('price' in j):
              print(("  - ","  - ","  - ","  - ","  - ","  - ",j['cusipNumber'],"  - ",j['description'],"  - ",j['holdingType'],"  - ",j['price']['amount']))
            else:
              print(("  - ","  - ","  - ","  - ","  - ","  - ",j['cusipNumber'],"  - ",j['description'],"  - ",j['holdingType'],"  - ","  - "))
    print('--------------------------------------------------------------------------------------------------------------')
