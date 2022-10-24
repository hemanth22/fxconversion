import requests
import os
import json

cuabc1="USD"
cuabc2="EUR"
cuabc3="GBP"
cuabc4="JPY"
cuabc5="AUD"
cuabc6="NZD"
cuabc7="CAD"
cuabc8="CHF"
cuabc9="NOK"
cuabc0="SEK"

EX_API_KEY = os.environ.get('EX_API_KEY')

def xcur(abc):
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/'+EX_API_KEY+'/pair/'+abc+'/USD'
    # Making our request
    response = requests.get(url)
    
    data = response.json()

    x= json.dumps(data)
    y = json.loads(x)
    #print(response)
    b = y['base_code']
    s = y['target_code']
    rate = y['conversion_rate']
    print('1 {0} = {2} {1}'.format(b, s, rate))

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
