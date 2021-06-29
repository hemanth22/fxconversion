from forex_python.converter import CurrencyRates
c = CurrencyRates()
a = c.get_rate('INR','SGD')
print('singapure currency: {0} {1}'.format(a*1362000,c.get_symbol('SGD')))
d = c.get_rate('INR','EUR')
print('European Currency: {0} {1}'.format(d*1362000,c.get_symbol('EUR')))
print('European Currency: {0} {1}'.format(d*853000,c.get_symbol('EUR')))
