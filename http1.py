#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import http.client, urllib.request, urllib.parse, urllib.error  #imports all the libraries in http and url  
import json             #library package for the json response access
import yaml             #converts unicode to byte code
import requests         #requests, for requesting the response from json

#debugging python step by step
# import pdb
# pdb.set_trace()
# that's it

class http:
  global headers
  # fqcn = "http"

#<summary>
    #cobrand login
    #<param name="url"></param>
    #<param name="requestBody"></param> cobrand user name and password
    #<returns></returns>
  
  @staticmethod
  def doPost(url, requestBody):
    mn = "docobrandlogin(POST : " + url + ", " + requestBody+" )"
    #print(HTTP.fqcn + " :: " + mn)  
    resp = requests.post(url=url, data=requestBody)
    data = json.loads(resp.text)
    list_dump = json.dumps(data)
    yaml.safe_load(list_dump)
    return list_dump

# <summary>
#     User login
#     <param name="url"></param> 
#     <param name="sessionTokens(data)"></param> Authorization header (cobrand session id)
#     <param name="requestBody"></param>user name and password
#     <returns></returns>
    
  @staticmethod
  def doPostUser(url,hdr, requestBody):
    mn = "douserlogin(POST : " + url + ", " + requestBody +" )"
    #print(HTTP.fqcn + " :: " + mn)
    #hdr = {'Authorization':'{cobSession='+cobSession+'}'}
    resp= requests.post(url, data=requestBody, headers=hdr)
    result = json.loads(resp.text)
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    return list_dump

#<summary>
  #Get Response
  #<param name="url"></param>
  #<param name="headers(data)"></param> Cobrand and user logins session id
  #<returns></returns>
  
  @staticmethod
  def doGet(url, hdr):
    mn = "doIO(GET :" + url+ ", headers =  " + str(hdr) +" )";
    #print(HTTP.fqcn + " :: " + mn)
    resp= requests.get(url, headers=hdr)
    result = json.loads(resp.text)
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    return list_dump

  @staticmethod
  def doPut(url, loginForm, hdr):
    mn = "doIO(PUT :" + url + ", headers =  " + str(hdr) +" )"
    #print(HTTP.fqcn + " :: " + mn)
    resp= requests.put(url, data=loginForm, headers=hdr)
    result = json.loads(resp.text)
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    return list_dump

  @staticmethod
  def doPutAddAcc(url, loginForm, hdr):
     mn = "doIO(PUT :" + url + ", headers = " + str(hdr) + " )"
     # print(HTTP.fqcn + " :: " + mn)
     resp = requests.put(url, params=loginForm, headers=hdr)
     result = json.loads(resp.text)
     list_dump = json.dumps(result)
     yaml.safe_load(list_dump)
     return list_dump

  @staticmethod
  def doPutProviderAcc(url, requestBody,hdr):
    mn = "doIO(PUT :" + url + ", headers =  " + str(hdr) +" )"
    #print(HTTP.fqcn + " :: " + mn)
    resp= requests.put(url, data=requestBody, headers=hdr)
    result = json.loads(resp.text)
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    return list_dump

  @staticmethod
  def doPostAddAcc(url, loginForm, hdr):
    mn = "doIO(POST :" + url + ", headers =  " + str(hdr) +" )"
    #print(HTTP.fqcn + " :: " + mn)
    resp= requests.post(url, data=loginForm, headers=hdr)
    result = json.loads(resp.text)
    list_dump = json.dumps(result)
    yaml.safe_load(list_dump)
    return list_dump
