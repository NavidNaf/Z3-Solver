# Z3 Demonstration Programs

For a comprehensive guide and additional examples on using the Z3 theorem prover, please refer to the [Z3py Tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm).

This repository contains several demonstration programs that showcase the capabilities of the Z3 theorem prover and solver. Each program illustrates different functionalities of Z3, including constraint creation, expression simplification, and solving inequalities.

## File Descriptions

### `z3-demo-1.py`
This program uses the Z3 theorem prover to create and analyze a logical expression. It defines two integer variables, `x` and `y`, and forms a constraint `x + y >= 3`. The program inspects the structure of this constraint, printing details such as the number of arguments in the expression, its child sub-expressions, and the operator used (the relational operator `>=`). Finally, it retrieves and displays the operator's name, providing insights into how Z3 represents and processes this logical formula.

### `z3-demo-2.py`
This program uses the Z3 solver to define integer variables `x` and `y` and applies the `simplify()` function to various expressions. It first simplifies the arithmetic expression `x + y + 2*x + 3`, reducing it to a simpler form. Next, it simplifies the logical comparison `x < y + x + 2`. Finally, it simplifies a compound logical expression involving an inequality and a sum of squares, combining and reducing the terms within the `And` condition. The `simplify()` function helps reduce complex expressions into their most straightforward form in each case.

### `z3-demo-3.py`
This program demonstrates the use of the Z3 solver to handle constraints involving integer variables `x` and `y`. It initializes a solver instance `s` and adds two constraints: `x > 10` and `y == x + 2`. The program checks the satisfiability of these constraints and prints the result. It creates a new scope using `s.push()` to add another constraint, `y < 11`, and checks the updated set of constraints. After restoring the previous state of the solver with `s.pop()`, it checks the satisfiability of the restored constraints again, showcasing the ability to manage and manipulate constraints in Z3 effectively.

### `z3-demo-4.py`
This program utilizes the Z3 solver to define two real variables, `x` and `y`, and then solves a set of inequalities. Specifically, it checks for solutions that satisfy the conditions \(x^2 + y^2 > 3\) and \(x^3 + y < 5\). The `solve()` function evaluates these inequalities and attempts to find values for `x` and `y` that meet both conditions simultaneously, demonstrating how Z3 can be used to analyze and solve nonlinear mathematical problems.

## Requirements

To run these programs, you need to have Python and the Z3 library installed. You can install Z3 via pip:

```bash
pip install z3-solver
