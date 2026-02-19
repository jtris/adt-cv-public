import math

def hypotenuse(a: int, b: int) -> float:
    return math.sqrt(a**2 + b**2)

c = hypotenuse(3, 4)
print(c)
