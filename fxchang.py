import requests
import json
import os


EX_API_KEY = os.environ.get('EX_API_KEY')
#abc = 'KWD'

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

def xcur(abc):
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/'+EX_API_KEY+'/pair/'+abc+'/INR'
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
