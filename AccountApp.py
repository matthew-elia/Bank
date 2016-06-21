#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp   #importing loginapp, to get a coBrand and User Session response and used
import http      #importing http, its the key for all the apps, and to post and get the json response
import http.client, urllib.request, urllib.parse, urllib.error    #imports all the libraries in http and url
import json       #library package for the json response access
import requests   #requests, for requesting the response from json

#<summary>
#The AccountApp class provides authentication and authorization services. 

#Steps to Use this App: 
#i) doCoBrandLogin(coBrandUserName, coBrandPassword)
#ii) doMemberLogin(userName, userPassword)

    #Browse all Accounts for member profile: 
      # getAccounts() 

class AccountApp:
  fqcn = "AccountApp"
  global userSession
  global cobSession
  
  @staticmethod
  def getAccounts():
    global userSession
    global cobSession

    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    mn = "getAccounts()"
    print((AccountApp.fqcn + " :: " + mn))
    accountSummaryURL = loginapp.LoginApp.localURLVer1 + "v1/accounts"
    jsonResponse = requests.get(accountSummaryURL,headers=hdr)
    response = jsonResponse.text
    parsed_json = json.loads(response)
    print(parsed_json)
    node = parsed_json.get("account",{})
    print('--------------------------------------------------------------------------')
    print("Account Id	-	Account Name	-	Account Status")
    print('--------------------------------------------------------------------------')
    for i in node:
      if ('accountName' in i):
        print((i['id'],"	-	",i['accountName'],"	-	",i['accountStatus']))
      elif (not ('accountName' in i)):
        print((i['id'], "	-	","    -   ", "	-	", i['accountStatus']))
    print('--------------------------------------------------------------------------')
