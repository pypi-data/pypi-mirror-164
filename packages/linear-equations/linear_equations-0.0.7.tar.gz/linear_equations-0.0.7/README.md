# linear_equations

This is a simple Mathematical Module which is simple to use.  The module provides classes through which linear equations in 2 variables can be solved, and visualized.

## Classes and Functions provided

- class Symbol
    > symbols to use in Linear Equations \
    > example: Symbol("x") -> x, Symbol("y") -> y
- class LinearEquation1D
    > objects of type ax + b = 0 \
    > each such object has one unique solution
- class LinearEquation2D
    > objects of type ax + by + c = 0 \
    > when standalone, each such object has infinitely many solutions \
    > when solved with another such object, the final result may be infinitely many solutions, no solution or a unique solution
- function solve1D(eqn)
    > solves one LinearEquation1D \
    > used to retrieve the solution to a 1D equation as a float
- function solve2D(eqn1, eqn2)
    > solves two LinearEquation2D \
    > used to retrieve solution to two 2D equations as a tuple of floats
- function consistency(eqn1, eqn2)
    > checks and returns if the given LinearEquation2D objects are consistent or not
- function satisfies(eqn, x, y)
    > returns True if the given pair of numbers satisfy a particular LinearEquation2D and False in all other cases

Each function contains help text that can be accessed through help() in python to know more about it.

## Update (0.0.5)
You can now graph and visualize 2-dimensional equations! \
Added function graph(eqn1, eqn2) which graphs the given LinearEquation2D objects on a 2D mathematical plot along with their solution (if any)

## Update (0.0.6)
Minor bug fixes:
- Fixed issues with plotting linear equations
- Improved legend on graphs

Added function graph_many(eqn1, eqn2, ..., eqnn, show_legend=True) which graphs more than two LinearEquation2D objects on the same plot along with each of their solutions (if any)

## Updates (0.0.7)
Minor bug fixes

## Reach out to me
If you face issues, contact me through my e-mail: knightt1821@gmail.com