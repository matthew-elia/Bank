#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import loginapp  #importing loginapp, to get a coBrand and User Session response and used
import http     #importing http, its the key for all the apps, and to post and get the json response
import json      #library package for the json response access
import yaml      #converts unicode to bytecode

#global parsed_json
#global siteResponse

class SiteApp:
  fqcn = "SiteApp"
  
  global userSession
  global cobSession
  global uSession
  global cSession
  global jsonResponse
  siteResponse=''

#<summary>
    #searchSite method  will search for the site name
    #<param name="searchString"></param> site name to be searched

  @staticmethod
  def searchSite(searchString):
    global userSession
    global cobSession
    global uSession
    global cSession
    
    uSession = loginapp.userSession
    cSession = loginapp.cobSession
    data = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    mn = "searchSite(searchString " + searchString + " )"
    #print(SiteApp.fqcn + " :: " + mn)
    searchSiteURL = loginapp.LoginApp.localURLVer1 + "v1/providers?name="+searchString
    jsonResponse = http.HTTP.doGet(searchSiteURL, data)
    #print jsonResponse
    print(jsonResponse)
    parsed_json = json.loads(jsonResponse)
    #import pdb
    #pdb.set_trace()
    #print parsed_json
    for provider_object in parsed_json['provider']:
        print((provider_object['id']," => ",provider_object['name']))
        #print provider_object['name']
      #print i['id'],"=>",i['name']

#<summary>
  #the getSiteLoginFrom method search for the site id
  @staticmethod
  def getSiteLoginForm(sitId):
    global uSession
    global cSession
    global jsonResponse

    uSession = loginapp.userSession
    cSession = loginapp.cobSession

    data = {'Authorization':'{userSession='+uSession+',cobSession='+cSession+'}'}
    mn = "searchSite(siteId " + sitId + " )"
    #print(SiteApp.fqcn + " :: " + mn)
    getSiteLoginFormURL = loginapp.LoginApp.localURLVer1 + "v1/providers/" + sitId
    jsonResponse = http.HTTP.doGet(getSiteLoginFormURL, data)
    #print jsonResponse
    SiteApp.siteResponse = jsonResponse
