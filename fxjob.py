from forex_python.converter import CurrencyRates
import json
c = CurrencyRates()
abc = c.get_rates('INR')
dxg = json.dumps(abc,sort_keys=True, indent=4)
#print(abc)
for i,z in abc.items():
    print(i,':',z)
