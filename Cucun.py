from forex_python.converter import CurrencyRates
c = CurrencyRates()
a = c.get_rate('INR','SGD')
print('singapure currency ',a*1362000)
d = c.get_rate('INR','EUR')
print('European Currency ',d*1362000)
print('European Currency ',d*853000)
