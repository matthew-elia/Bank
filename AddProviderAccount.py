#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.
 
import loginapp      #importing loginapp, to get a coBrand and User Session response and used
import SiteApp       #importing SiteApp, its site id output is taken and assigned it as variable provider
import http         #importing http, its the key for all the apps, and to post and get the json response
import json          #library package for the json response access
import yaml          #converts unicode to bytecode
#from PkiUtil import PkiUtil

 #  The AddProviderAccount class provides aggregation methods. 
 #  Aggregation means, adding a bank, insurance/investment etcc.. account to Yodlee. 
   
 #   Steps to Use this App: 
 #   i) SiteApp.searchSite(searchString); First Fetch the Website you want to add the Account from. 
 #   ii) SiteApp.getSiteLoginForm(site); Get the Login Form for that Website. 
    
 #   Then user the methods of this calls:
     
 #   i) addProviderAccount(loginFrom)
    
 #   The SiteId is fetched from the previous response. 
 #   ii) getProviderAccountDetails(providerAccountId)

class AddProviderAccount:
  fqcn = "AddProviderAccount"
  providerAccountId=''

  # loginform is a ValueOject obtained from provider,which is assigned from the siteapp api(siteId)output.  
    #param loginForm

    #@return
  
  @staticmethod
  def addProviderAccount(loginForm):
    mn = "addProviderAccount( " + loginForm + " )"
    #print(AddProviderAccount.fqcn + " :: " + mn)
    loginForm1 = json.loads(loginForm)
    loginFormId = loginForm1['provider'][0]['id']
    print('*****************')
    print(loginForm1)
    loginForm1 ="{"+'"'+"loginForm"+'":'+str(loginForm1['provider'][0]['loginForm']).replace("True","true").replace("False","false").replace("u'",'"').replace("'",'"')+"}"
    print(loginForm1)
    print(loginFormId)
	
    global userSession
    global cobSession
    global uSession
    global cSession
    global hdr
    global siteAccountId
    global jsonRequest

    uSession = loginapp.userSession
    cSession = loginapp.cobSession
    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    addSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/providerAccounts?providerId=" + str(loginFormId)
    print(addSiteURL)
    jsonResponse = http.HTTP.doPostAddAcc(addSiteURL, loginForm1, hdr)
    print(jsonResponse)
    parsed_json = json.loads(jsonResponse)
    print('--------------------------------------------------')
    print("Add Account Response:")
    print('--------------------------------------------------')
    AddProviderAccount.providerAccountId = parsed_json['providerAccount']['id']
    print(("Provider Account ID: ", AddProviderAccount.providerAccountId))
    print(("Refresh Status: ", parsed_json['providerAccount']['refreshInfo']['status']))
    print('--------------------------------------------------')
    
    

#  The following api provides refresh status of an account which was aggregated from the previous api call - AddSiteAccount.addSiteAccount(Provider loginForm)
    # @param siteAccountId
    # @return
    
  @staticmethod
  def getProviderAccountDetails(providerAccountId, isPkiRequired):
    global hdr
    mn = "getProviderAccountDetails( " + str(AddProviderAccount.providerAccountId) + " )"
    getStatusURL = loginapp.LoginApp.localURLVer1 + "v1/providers/providerAccounts/" +str(AddProviderAccount.providerAccountId)
    jsonResponse = http.HTTP.doGet(getStatusURL, hdr)
    parsed_json = json.loads(jsonResponse)
    print(parsed_json)
    #print jsonResponse
    print('--------------------------------------------------')
    print("Account Refresh Response:")
    print('--------------------------------------------------')
    print(("Provider Account ID: ", AddProviderAccount.providerAccountId))
    refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
    #statusCode = parsed_json['providerAccount']['refreshInfo']['statusCode']
    print(("Refresh Status: ", parsed_json['providerAccount']['refreshInfo']['status']))
    if refreshStatus == 'FAILED':
        print('Please try again')
    else:
        #print parsed_json
        while refreshStatus != 'SUCCESS':
          if refreshStatus == 'FAILED':
            break
          try:
            loginForm = parsed_json['providerAccount']['loginForm']
            #print 'Got login Form', parsed_json
            jsonRequest = json.dumps(parsed_json)
            break
          except:
            jsonResponse = http.HTTP.doGet(getStatusURL, hdr)
            #print jsonResponse
            parsed_json = json.loads(jsonResponse)
            #print parsed_json
            refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
            print(("Refresh Status: ", parsed_json['providerAccount']['refreshInfo']['status']))
        if refreshStatus != 'FAILED':
            jsonRequest = json.dumps(parsed_json)
            AddProviderAccount.updateProviderAccount(AddProviderAccount.providerAccountId, jsonRequest, isPkiRequired)
    print('--------------------------------------------------')


  @staticmethod
  def updateProviderAccount(providerAccountId, jsonRequest, isPkiRequired):
    global userSession
    global cobSession
    global uSession
    global cSession
    global hdr
    global siteAccountId
    global refreshStatus
    getStatusURL = loginapp.LoginApp.localURLVer1 + "v1/providers/providerAccounts/" +str(AddProviderAccount.providerAccountId)

    uSession = loginapp.userSession
    cSession = loginapp.cobSession
    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}

    #print 'checking----'jsonRequest
     
    if 'token' in jsonRequest:
      parsed_json = json.loads(jsonRequest)
      token = "123456"
      question1 = "Texas"
      question2 = "w3schools"
      parsed_json['providerAccount']['loginForm']['row'][0]['field'][0]['value'] = token
      print('Token verification in-progress...')
      print(parsed_json)
      jsonVal ="{"+'"'+"loginForm"+'":'+str(parsed_json['providerAccount']['loginForm']).replace("True","true").replace("False","false").replace("u'",'"').replace("'",'"')+"}"
      print(jsonVal)
      updateSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/providerAccounts?providerAccountIds=" + str(providerAccountId)
      jsonResponse = http.HTTP.doPutProviderAcc(updateSiteURL, jsonVal, hdr)
      parsed_json = json.loads(jsonResponse)
      refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
      print(("Refresh Status::::::::::::: ", parsed_json['providerAccount']['refreshInfo']['status']))
      if refreshStatus == 'FAILED':
        print('Please try again')
      while refreshStatus != 'SUCCESS':
        if refreshStatus == 'FAILED':
            break
        try:
            parsed_json['providerAccount']['loginForm']['row'][0]['field'][0]['value'] = question1
            parsed_json['providerAccount']['loginForm']['row'][1]['field'][0]['value'] =question2
            loginForm = "{"+'"'+"loginForm"+'":'+str(parsed_json['providerAccount']['loginForm']).replace("True","true").replace("False","false").replace("u'",'"').replace("'",'"')+"}"
            jsonRequest = json.dumps(parsed_json)
            break
        except:
            jsonResponse = http.HTTP.doGet(getStatusURL, hdr)
            parsed_json = json.loads(jsonResponse)
            refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
            print(("Refresh Status: ", parsed_json['providerAccount']['refreshInfo']['status']))
      jsonVal = loginForm
      print('QA verification in-progress...')
      updateSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/providerAccounts?providerAccountIds=" + str(providerAccountId)
      jsonResponse = http.HTTP.doPutProviderAcc(updateSiteURL, jsonVal, hdr)
      parsed_json = json.loads(jsonResponse)
      refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
      if refreshStatus == 'Success':
        print('QA verification process successfull!!!!')
      else:
        print(("Refresh Status:", parsed_json['providerAccount']['refreshInfo']['status']))
        if refreshStatus == 'FAILED':
          print('Please try again')
        while refreshStatus != 'SUCCESS':
          if refreshStatus == 'FAILED':
            break
          try:
            loginForm = parsed_json['providerAccount']['loginForm']
            #print 'Got login Form', parsed_json
            jsonRequest = json.dumps(parsed_json)
            break
          except:
            jsonResponse = http.HTTP.doGet(getStatusURL, hdr)
            #print jsonResponse
            parsed_json = json.loads(jsonResponse)
            #print parsed_json
            refreshStatus = parsed_json['providerAccount']['refreshInfo']['status']
            print(("Refresh Status: ", parsed_json['providerAccount']['refreshInfo']['status']))
        if refreshStatus != 'FAILED':
            jsonRequest = json.dumps(parsed_json)
            AddProviderAccount.updateProviderAccount(AddProviderAccount.providerAccountId, jsonRequest, isPkiRequired)           
