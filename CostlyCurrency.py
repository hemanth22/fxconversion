import requests
import os

cuabc1="KWD"
cuabc2="BHD"
cuabc3="OMR"
cuabc4="JOD"
cuabc5="GIP"
cuabc6="GBP"
cuabc7="KYD"
cuabc8="EUR"
cuabc9="CHF"
cuabc0="USD"

EX_API_KEY = os.environ.get('EX_API_KEY')

def xcur(abc):
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/'+EX_API_KEY+'/pair/'+abc+'/INR'
    # Making our request
    response = requests.get(url)
    #print(response)
    data = response.json()
    print("======================================================")
    #print(data)
    for i,z in data.items():
        print(str(i),':',str(z))

xcur(cuabc1)
xcur(cuabc2)
xcur(cuabc3)
xcur(cuabc4)
xcur(cuabc5)
xcur(cuabc6)
xcur(cuabc7)
xcur(cuabc8)
xcur(cuabc9)
xcur(cuabc0)
