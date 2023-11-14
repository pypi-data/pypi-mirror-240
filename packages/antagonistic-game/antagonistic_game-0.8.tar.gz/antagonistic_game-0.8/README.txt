This package is intended to be used for zero-sum (=antagonistic) matrix game solving and visualization of the solutions.

What to include?
from antagonistic_game.package import nash_equilibrium
from antagonistic_game.package import visualize

How it works?
- "nash_equilibrium" function takes a numpy matrix representing the game and returns the game solution: game value, first player's optimal strategies and the second player's optimal strategies
- "visualize" function takes two parameters: the game matrix and a tuple fo 2 elements: a numpy array of the first player's strategies and a numpy array of the second player's strategies.

Enjoy using <3

