# Kylie Tate
# 9-6-25

class DotProduct:
    def __init__(self):
        self.vec_a = input('\nType in vector a in this format (no fractions): "x,y,z"\nVector A: ')
        self.vec_b = input('Type in vector b in this format (no fractions): "x,y,z"\nVector B: ')
        self.vec_a_str = self.vec_a.split(",")
        self.vec_b_str = self.vec_b.split(",")
        self.eqs = []

    
    def multiplies(self):
        """
            multiplies each pair and adds them together
            this follows the definition of the Dot product:
            a*b = a_1*b_1 + a_2*b_2 + a_3*b_3
        """
        product = 0
        for i in range(len(self.vec_a_str)):
            product_part = float(self.vec_a_str[i]) * float(self.vec_b_str[i])
            product += product_part
            self.eqs.append(f"{float(self.vec_a_str[i])} * {float(self.vec_b_str[i])}")

        return product