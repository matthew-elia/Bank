#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.
 
import loginapp      #importing loginapp, to get a coBrand and User Session response and used
import SiteApp       #importing SiteApp, its site id output is taken and assigned it as variable provider
import http         #importing http, its the key for all the apps, and to post and get the json response
import json          #library package for the json response access
import yaml          #converts unicode to bytecode
#from PkiUtil import PkiUtil

 #  The AddSiteAccount class provides aggregation methods. 
 #  Aggregation means, adding a bank, insurance/investment etcc.. account to Yodlee. 
   
 #   Steps to Use this App: 
 #   i) SiteApp.searchSite(searchString); First Fetch the Website you want to add the Account from. 
 #   ii) SiteApp.getSiteLoginForm(site); Get the Login Form for that Website. 
    
 #   Then user the methods of this calls:
     
 #   i) addSiteAccount(loginFrom)
    
 #   The SiteId is fetched from the previous response. 
 #   ii) getRefreshStatus(siteAccountId)

class AddSiteAccount:
  fqcn = "AddSiteAccount"
  providerAccountId=''

  # loginform is a ValueOject obtained from provider,which is assigned from the siteapp api(siteId)output.  
    #param loginForm

    #@return
  
  @staticmethod
  def addSiteAccount(loginForm):
    mn = "addSiteAccount( " + loginForm + " )"
    #print(AddSiteAccount.fqcn + " :: " + mn)
    loginForm1 = json.loads(loginForm)
    loginFormId = loginForm1['provider'][0]['id']
    
    global userSession
    global cobSession
    global uSession
    global cSession
    global hdr
    global siteAccountId
    global jsonRequest
    print(loginForm)
    uSession = loginapp.userSession
    cSession = loginapp.cobSession
    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    addSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/" + str(loginFormId)
    jsonResponse = http.HTTP.doPostAddAcc(addSiteURL, loginForm, hdr)
    print(jsonResponse)
    parsed_json = json.loads(jsonResponse)
    print('--------------------------------------------------')
    print("Add Account Response:")
    print('--------------------------------------------------')
    AddSiteAccount.providerAccountId = parsed_json['providerAccountId']
    print(("Provider Account ID: ", AddSiteAccount.providerAccountId))
    print(("Refresh Status: ", parsed_json['refreshInfo']['refreshStatus']))
    print('--------------------------------------------------')
    
    

#  The following api provides refresh status of an account which was aggregated from the previous api call - AddSiteAccount.addSiteAccount(Provider loginForm)
    # @param siteAccountId
    # @return
    
  @staticmethod
  def getRefreshStatus(providerAccountId, isPkiRequired):
    global hdr
    mn = "getRefreshStatus( " + str(AddSiteAccount.providerAccountId) + " )"
    #print(Refresh SiteAccount.fqcn + " :: " + str(mn))
    getRefreshStatusURL = loginapp.LoginApp.localURLVer1 + "v1/refresh/" + str(AddSiteAccount.providerAccountId)
    jsonResponse = http.HTTP.doGet(getRefreshStatusURL, hdr)
    parsed_json = json.loads(jsonResponse)
    #print jsonResponse
    print('--------------------------------------------------')
    print("Account Refresh Response:")
    print('--------------------------------------------------')
    print(("Provider Account ID: ", AddSiteAccount.providerAccountId))
    refreshStatus = parsed_json['refreshInfo']['refreshStatus']
    statusCode = parsed_json['refreshInfo']['statusCode']
    print(("Refresh Status: ", parsed_json['refreshInfo']['refreshStatus']))
    if refreshStatus == 'LOGIN_FAILURE' or refreshStatus == 'REFRESH_TIMED_OUT' or refreshStatus == 'REFRESH_CANCELLED' or refreshStatus == 'REFRESH_COMPLETED_WITH_UNCERTAIN_ACCOUNT'	or refreshStatus == 'SITE_CANNOT_BE_REFRESHED' or refreshStatus == 'REFRESHED_TOO_RECENTLY' or refreshStatus == 'REFRESH_COMPLETED_ACCOUNTS_ALREADY_AGGREGATED':
        print('Please try again')
    else:
        #print parsed_json
        while refreshStatus != 'REFRESH_COMPLETED':
          if refreshStatus == 'LOGIN_FAILURE' or refreshStatus == 'REFRESH_TIMED_OUT' or refreshStatus == 'REFRESH_CANCELLED' or refreshStatus == 'REFRESH_COMPLETED_WITH_UNCERTAIN_ACCOUNT' or refreshStatus == 'SITE_CANNOT_BE_REFRESHED' or refreshStatus == 'REFRESHED_TOO_RECENTLY' or refreshStatus == 'REFRESH_COMPLETED_ACCOUNTS_ALREADY_AGGREGATED':
            break
          try:
            loginForm = parsed_json['loginForm']
            print('Got login Form')
            jsonRequest = json.dumps(parsed_json)
            break
          except:
            jsonResponse = http.HTTP.doGet(getRefreshStatusURL, hdr)
            #print jsonResponse
            parsed_json = json.loads(jsonResponse)
            #print parsed_json
            refreshStatus = parsed_json['refreshInfo']['refreshStatus']
            print(("Refresh Status: ", parsed_json['refreshInfo']['refreshStatus']))
        if (refreshStatus != 'LOGIN_FAILURE' or refreshStatus != 'REFRESH_TIMED_OUT' or refreshStatus != 'REFRESH_CANCELLED' or refreshStatus != 'REFRESH_COMPLETED_WITH_UNCERTAIN_ACCOUNT' or refreshStatus != 'SITE_CANNOT_BE_REFRESHED' or refreshStatus != 'REFRESHED_TOO_RECENTLY' or refreshStatus != 'REFRESH_COMPLETED_ACCOUNTS_ALREADY_AGGREGATED') and refreshStatus != 'REFRESH_COMPLETED':
            AddSiteAccount.updateSiteAccount(AddSiteAccount.providerAccountId, jsonRequest, isPkiRequired)
    print('--------------------------------------------------')


  @staticmethod
  def updateSiteAccount(providerAccountId, jsonRequest, isPkiRequired):
    global userSession
    global cobSession
    global uSession
    global cSession
    global hdr
    global siteAccountId

    uSession = loginapp.userSession
    cSession = loginapp.cobSession
    hdr = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}

    #print 'checking----'jsonRequest

    if 'token' in jsonRequest:
      parsed_json = json.loads(jsonRequest)
      token = "123456"
      parsed_json['loginForm']['row'][0]['field'][0]['value'] = token
      print('Token verification in-progress...')

      jsonVal = json.dumps(parsed_json)
      requestBody="MFAChallenge="+jsonVal
      print(('request Body ==> ',requestBody))
      updateSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/" + str(providerAccountId)
      jsonResponse = http.HTTP.doPutAddAcc(updateSiteURL, requestBody, hdr)
      #print 'Update Site Response: '+jsonResponse
      parsed_json = json.loads(jsonResponse)
      print(parsed_json)
      jsonResult = parsed_json['MFAChallenge']
      if jsonResult == 'Success':
        print('Token verification process successfull!!!!')
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
      else:
        print('Please try again')
    elif 'questionAndAnswer' in jsonRequest:
      parsed_json = json.loads(jsonRequest)
      question1 = "Texas"
      question2 = "w3schools"
      if isPkiRequired == 1:
        parsed_json['loginForm']['row'][0]['field'][0]['value'] = PkiUtil.encryptPKI(question1)
        parsed_json['loginForm']['row'][1]['field'][0]['value'] = PkiUtil.encryptPKI(question2)
      else:
        parsed_json['loginForm']['row'][0]['field'][0]['value'] = question1
        parsed_json['loginForm']['row'][1]['field'][0]['value'] = question2
      print('QA verification in-progress...')

      jsonVal = json.dumps(parsed_json)
      requestBody="MFAChallenge="+jsonVal
      #print 'request Body ==> ',requestBody
      updateSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers/" + str(providerAccountId)
      jsonResponse = http.HTTP.doPutAddAcc(updateSiteURL, requestBody, hdr)
      #print 'Update Site Response: '+jsonResponse
      parsed_json = json.loads(jsonResponse)
      #print parsed_json
      jsonResult = parsed_json['MFAChallenge']
      if jsonResult == 'Success':
        print('QA verification process successfull!!!!')
        AddSiteAccount.getRefreshStatus(AddSiteAccount.providerAccountId, isPkiRequired)
      else:
        print('Please try again')
