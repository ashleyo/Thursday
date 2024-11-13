'''
Discussion - not very deep - of why we often prefer managed access to data in classes
and how to use properties to achieve this.
'''

class MultiplyBy:
    def __init__(self, value):
        self._value = value

    def __call__(self, other):
        return self._value * other

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError('Value must be non-negative')
        self._value = new_value
    


double = MultiplyBy(2)
print(double(7))

print(double.value)
double.value = -1

print(double(7))




