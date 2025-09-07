from dot_product import DotProduct
from abs_a import Abs_a

class Vector(Abs_a):
    def __init__(self):
        Abs_a.__init__(self)
        self.numerators = []
        for i in range(len(self.vec_a_str)):
            self.numerators.append(self.multiplies() * float(self.vec_a_str[i]))

    def answer(self):
        self.calculate()
        print(f"<{self.numerators[0]}/{self.inside_sqrt}, {self.numerators[1]}/{self.inside_sqrt}, {self.numerators[2]}/{self.inside_sqrt}>")
