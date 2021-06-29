from forex_python.converter import CurrencyRates
c = CurrencyRates()
a = c.get_rate('INR','SGD')
print('singapure currency {0}'.format(a*1362000))
d = c.get_rate('INR','EUR')
print('European Currency {0}'.format(d*1362000))
print('European Currency {0}'.format(d*853000))
