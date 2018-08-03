# easy and simple pipeline with self define class
from sklearn.pipeline import Pipeline


class Mul(object):
    def __init__(self, x):
        self.x = x
    
    def fit(self, x, y=None):
        return self
    
    def transform(self, x):
        return x * x

class Add(object):
    def __init__(self, x):
        self.x = x
    
    def fit(self, x, y=None):
        print(x+5)
        return x+5


mul_ = Mul(3)
add_ = Add(3)


mul_add = Pipeline([('multiply', mul_), ('add', add_)])
                     
print(mul_add.fit(10))
#105
