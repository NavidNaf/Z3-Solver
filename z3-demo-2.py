# This program uses the Z3 solver to define integer variables `x` and `y` and applies the `simplify()` function to various expressions. It first simplifies the arithmetic expression `x + y + 2*x + 3`, reducing it to a simpler form. Next, it simplifies the logical comparison `x < y + x + 2`. Finally, it simplifies a compound logical expression involving an inequality and a sum of squares, combining and reducing the terms within the `And` condition. The `simplify()` function helps reduce complex expressions into their most straightforward form in each case.

from z3 import *

x = Int('x')
y = Int('y')
print (simplify(x + y + 2*x + 3))
print (simplify(x < y + x + 2))
print (simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))
