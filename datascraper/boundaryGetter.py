import requests
import urllib3
import logging
import time
import urllib.error
import datetime

#Configuration to avoid SSL errors in servers
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
   # no pyopenssl support used / needed / available
   pass




numAttempt = 1
http = urllib3.PoolManager()
logFile = open("boundaries.txt", "a+")
workFile = open("workfile.txt", "a+")
for courtNumber in range(2,68):
    boundary = 30000
    courtString = format(courtNumber, "02d")
    foundBound = False
    while not foundBound and boundary > 300:
        for i in range(2):
             crString = format(boundary - i, "07d")
             workFile.write(str(datetime.time.now()) + ' Attempt No.' +str(numAttempt) + f': Trying for CP-{courtString}-CR-{crString}-2018' + '\n')
             numAttempt += 1
             time.sleep(3)
             webpage = http.request('GET', f'https://services.pacourts.us/public/v1/cases/CP-{courtString}-CR-{crString}-2018')
             if webpage.status == 200 :
                 logFile.write(f'CP {courtString}  was found at {crString}' + '\n')
                 print("CR",courtString, " was found at " + crString)
                 foundBound = True;
                 break
             elif webpage.status == 429:
                 workFile.write('Reached request limit, sleeping for an hour' + '\n')
                 time.sleep(3610)

        if foundBound:
             break
        boundary =  int(boundary//1.1)

