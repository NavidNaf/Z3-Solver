# This program uses the Z3 theorem prover to create and analyze a logical expression. It defines two integer variables, `x` and `y`, and forms a constraint `x + y >= 3`. The program inspects the structure of this constraint, printing details such as the number of arguments in the expression, its child sub-expressions, and the operator used (the relational operator `>=`). Finally, it retrieves and displays the operator's name, providing insights into how Z3 represents and processes this logical formula.

from z3 import *

x = Int('x')
y = Int('y')
n = x + y >= 3
print ("num args: ", n.num_args())
print ("children: ", n.children())
print ("1st child:", n.arg(0))
print ("2nd child:", n.arg(1))
print ("operator: ", n.decl())
print ("op name:  ", n.decl().name())
