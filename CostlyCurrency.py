from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
c = CurrencyRates()

s = CurrencyCodes()
a = c.get_rate('KWD','INR')
print('Top 1 : {0} {1}'.format((a),s.get_symbol('INR')))
f = c.get_rate('BHD','INR')
print('Top 2 : {0} {1}'.format((f),s.get_symbol('INR')))
fsa = c.get_rate('OMR','INR')
print('Top 3 : {0} {1}'.format((fsa),s.get_symbol('INR')))
