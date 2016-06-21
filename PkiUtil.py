#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

class PkiUtil:
  fqcn = "PkiUtil"
  
  @staticmethod
  def encryptPKI(dataToEncrypt):
    dataFile = open("publickey.txt", "r").read()
    jsonData = json.loads(dataFile)
    pubKey = jsonData["keyAsPemString"]
    rsakey = RSA.importKey(pubKey)
    cipher = PKCS1_v1_5.new(rsakey)
    data = cipher.encrypt(dataToEncrypt)
    hex_string = data.encode('hex')
    return hex_string