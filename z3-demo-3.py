# This program demonstrates the use of the Z3 solver to handle constraints involving integer variables `x` and `y`. It initializes a solver instance `s` and adds two constraints: `x > 10` and `y == x + 2`. The program checks the satisfiability of these constraints and prints the result. It creates a new scope using `s.push()` to add another constraint, `y < 11`, and checks the updated set of constraints. After restoring the previous state of the solver with `s.pop()`, it checks the satisfiability of the restored constraints again, showcasing the ability to manage and manipulate constraints in Z3 effectively.

from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
print (s)

s.add(x > 10, y == x + 2)
print (s)
print ("Solving constraints in the solver s ...")
print (s.check())

print ("Create a new scope...")
s.push()
s.add(y < 11)
print (s)
print ("Solving updated set of constraints...")
print (s.check())

print ("Restoring state...")
s.pop()
print (s)
print ("Solving restored set of constraints...")
print (s.check())