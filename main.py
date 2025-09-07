from dot_product import DotProduct
from abs_a import Abs_a
from vector_proj import Vector
from scalar_proj import Scalar

def repeat():
    """in case there are more than one problems to solve"""
    response = input("\nAnother? (type y or n)\n")
    if response == 'y':
        main()
    else: return

def main():
    """allows you to choose and use which solving type"""
    which_method = input("\nCalculate [1]Dot Product, [2]Scalar Projection, [3]Vector Projection\n")

    if which_method == "1":
        dotprod = DotProduct()
        multi = dotprod.multiplies()
        for i in range(len(dotprod.eqs)):
            print(f"{dotprod.eqs[i]}")
        print(multi)
        repeat()
    elif which_method == "2":
        scalar = Scalar()
        scalar.answer()
        repeat()
    elif which_method == "3":
        vector = Vector()
        vector.answer()
        repeat()
    else:
        print("Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()