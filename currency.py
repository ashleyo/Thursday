from typing import Any


BASE_CURRENCY = 'USD'

class Currency:
    _rate = 1.00
    _name = BASE_CURRENCY
    def __init__(self, name, rate):
        self._name = name
        self._rate = rate
    
    def convert_to_base(self, amount):
        return amount * self.rate
    def yield_from_base(self, amount):
        return amount / self.rate
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.convert_to_base(*args, **kwds)

    @property
    def rate(self):
        return self._rate
    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def name(self):
        return self._name

'''
Example usage:
'''

GBP = Currency('GBP', 1.25)
print(GBP.convert_to_base(100)) # 125.0 one hundred pounds is 125 dollars
print(GBP.yield_from_base(100)) # 80 pounds is 100 dollars

EURO = Currency('EUR', 1.10)
print(EURO.convert_to_base(100)) # 110.0 one hundred euros is 110 dollars
print(EURO.yield_from_base(100)) # 90.9090909090909 euros is 100 dollars


