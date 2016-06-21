#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import http
import http.client, urllib.request, urllib.parse, urllib.error    #imports all the libraries in http and url
import json               #library package for the json response access
import yaml               #converts unicode to byte code
import requests           #requests, for requesting the response from json
from requests import *    #imports all the libraries in the requests
import configparser


class LoginApp:
  global cobSession
  global userSession
  global cobrandLogin
  global cobrandPassword
  global locale
  global userName
  global userPassword
  global userLocale
  
  fqcn = "LoginApp"
  config=configparser.RawConfigParser()
  _SECTION = 'BaseURLSection'
  config.readfp(open('Config.cfg.txt'))
  #self._app_name = config.get(_SECTION, 'baseURL')
  localURLVer1 = config.get(_SECTION, "baseURL")
  print(localURLVer1)
  cobrandLogin = config.get(_SECTION, "cobrandLogin")
  cobrandPassword = config.get(_SECTION, "cobrandPassword")
  locale = config.get(_SECTION, "locale")
  userName = config.get(_SECTION, "loginName")
  userPassword = config.get(_SECTION, "password")
  userLocale = config.get(_SECTION, "userLocale")
    
  @staticmethod
  def doCoBrandLogin(coBrandUserName, coBrandPassword, locale):#doCoBrandLogin gives the CoBrandLogin session response#
    
    global cobSession
    mn = "doCoBrandLogin(coBrandUserName=" + coBrandUserName + ",coBrandPassword=" +coBrandPassword+ ",locale=" + locale + " )"
    print((LoginApp.fqcn + "::" + mn))
    
    coBrandLoginURL = LoginApp.localURLVer1 + "v1/cobrand/login"
    requestBody = json.dumps("{"+'"'+"cobrand"+'":{'+'"'+"cobrandLogin"+'"'+":"+'"'+coBrandUserName+'",'+'"'+"cobrandPassword"+'"'+":"+'"'+coBrandPassword+'",'+'"'+"locale"+'":"'+locale+'"'+"}}")
    requestBody = json.loads(requestBody)
    
    jsonResponse = requests.post(coBrandLoginURL, requestBody)
    
    response = jsonResponse.json()
    result = response.get("session",{response['session']['cobSession']})
    cobSession = result['cobSession']
    print(("Cobrand Session Token:- " + cobSession))
	
  @staticmethod
  def doUserLogin(userName, userPassword, userLocale):
    
    global userSession
    mn = "doUserLogin(loginName="+userName+",password="+userPassword+",coBrandSessionCredential="+cobSession+")"
    print((LoginApp.fqcn + "::" + mn))
    
    requestBody = json.dumps("{"+'"'+"user"+'":{'+'"'+"loginName"+'"'+":"+'"'+userName+'",'+'"'+"password"+'"'+":"+'"'+userPassword+'",'+'"'+"locale"+'":"'+userLocale+'"'+"}}")
    requestBody = json.loads(requestBody)
    hdr = {'Authorization':'{cobSession='+cobSession+'}'}
    userLoginURL = LoginApp.localURLVer1 + "v1/user/login"
    
    resp= requests.post(userLoginURL, data=requestBody, headers=hdr)
    
    result = json.loads(resp.text)
    userSession = result["user"]["session"]["userSession"]
    print(("User Session Token:- " + userSession))
    
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    print(list_dump)

#Authenticate
LoginApp.doCoBrandLogin(cobrandLogin,cobrandPassword,locale)
LoginApp.doUserLogin(userName, userPassword, userLocale)