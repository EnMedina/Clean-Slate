import requests
import urllib3
import logging
import time
import urllib.error
from datetime import datetime

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
logFile = open("/home/ec2-user/Clean-Slate/datascraper/boundaries.txt", "a+")
workFile = open("/home/ec2-user/Clean-Slate/datascraper/workfile.txt", "a+")
for courtNumber in range(21,30):
    boundary = 30000
    courtString = format(courtNumber, "02d")
    foundBound = False
    while not foundBound and boundary > 300:
        for i in range(2):
             logFile.flush()
             workFile.flush()
             crString = format(boundary - i, "07d")
             workFile.write(str(datetime.now()) + ' Attempt No.' +str(numAttempt) + f': Trying for CP-{courtString}-CR-{crString}-2018' + '\n')
             numAttempt += 1
             time.sleep(1)
             webpage = http.request('GET', f'https://services.pacourts.us/public/v1/cases/CP-{courtString}-CR-{crString}-2018')
             if webpage.status == 200 :
                 logFile.write(f'CP {courtString}  was found at {crString}' + '\n')
                 print("CR",courtString, " was found at " + crString)
                 foundBound = True;
                 break
             elif webpage.status == 429:
                 workFile.write('Reached request limit, sleeping for an hour' + '\n')
                 workFile.flush()
                 time.sleep(3610)
             elif webpage.status != 404:
                 workFile.write('Unexpected error with status' + str(webpage.status))

        if foundBound:
             break
        boundary =  int(boundary//1.1)


