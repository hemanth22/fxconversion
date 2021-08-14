from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
c = CurrencyRates()

s = CurrencyCodes()
a = c.get_rate('SGD','INR')
print('singapure fx rate with indian currency: {0} {1}'.format((a),s.get_symbol('INR')))


f = c.get_rate('EUR','INR')
print('European fx rate with indian currency: {0} {1}'.format((f),s.get_symbol('INR')))

fsa = c.get_rate('USD','INR')
print('American fx rate with indian currency: {0} {1}'.format((fsa),s.get_symbol('INR')))
