from dot_product import DotProduct
from abs_a import Abs_a

class Scalar(Abs_a):
    def __init__(self):
        Abs_a.__init__(self)

    def answer(self):
        print(f"{self.multiplies()} / {self.calculate()}")