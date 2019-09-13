from urllib.request import urlopen,Request
import logging
import time

timeoutSeconds = 10
for crValue in range(10):
    time.sleep(timeoutSeconds)
    crString = format(crValue,"07d")
    print("Trying for prefix ", crString)
    try:
        file = f'https://services.pacourts.us/public/v1/cases/CP-02-CR-{crString}-2018'
        req = Request(file,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        file1 = open(f"CP-02-CR-{crString}-2018.json", "wb")  # append mode
        file1.write(webpage)
        file1.close()
    except Exception as e:
        logging.error('error is',)
        file2 = open("logs.csv", "a")
        log = f'{file},{e} \n'
        file2.write(log)


