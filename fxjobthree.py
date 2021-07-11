from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import json
c = CurrencyRates()
s = CurrencyCodes()
abc = c.get_rates('INR')
dxg = json.dumps(abc,sort_keys=True, indent=4)
#print(abc)
for i,z in abc.items():
    print(i,':',z,s.get_symbol(i),'  ',s.get_currency_name(i))
