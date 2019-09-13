import urllib.request, urllib.error
try:
    file = f'https://services.pacourts.us/public/v1/cases/CP-01-CR-0001399-2018'
    req = urllib.request.Request(file,headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req)
    print(webpage.getcode())
    if webpage.getcode() == 200 :
        print("That address does exist")
except urllib.error.HTTPError as e:
        print( e.code )
