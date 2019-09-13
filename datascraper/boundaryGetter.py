from urllib.request import urlopen,Request
import logging
import time
import urllib.error

boundaries = [50000, 40000,35000,30000,27500, 25000, 22500, 20000, 18000, 16000, 15000, 13000, 11500, 10000, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500, 4000, 3500, 3250, 3000, 2750,2500, 2250, 2000, 1750, 1500, 1250, 1000, 750, 600, 500, 400, 300, 200, 100, 50, 25]
logFile = open("boundaries.txt", "a")
for courtNumber in range(2,68):
    courtString = format(courtNumber, "02d")
    foundBound = False 
    for num in boundaries:
        for i in range(3):
            crString = format(num - i, "07d")
            print(f' Trying for CP-{courtString}-CR-{crString}-2018')
            time.sleep(5)
            try:    
                file = f'https://services.pacourts.us/public/v1/cases/CP-{courtString}-CR-{crString}-2018'
                req = Request(file,headers={'User-Agent': 'Mozilla/5.0'})
                result = urlopen(req)
                if result.getcode() == 200:
                        logFile.write(f'CP {courtString}  was found at {crString}' + '\n')
                        print("CR",courtString, " was found at " + crString)
                        foundBound = True;
                        break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    continue
                elif e.code == 429:
                    time.sleep(3600)
                    continue
                else:
                    raise
        if foundBound:
            break

