from dot_product import DotProduct
from math import sqrt

class Abs_a(DotProduct):
    """|a| is used to find the projections"""
    def __init__(self):
        DotProduct.__init__(self)
        self.vector_float = []
        for i in range(len(self.vec_a_str)):
            self.vector_float.append(float(self.vec_a_str[i]))
        self.inside_sqrt = 0

    def calculate(self):
        added = 0
        for i in range(len(self.vec_a_str)):
            added += (self.vector_float[i])**2
        self.inside_sqrt = added
        return f"√{added}"
    