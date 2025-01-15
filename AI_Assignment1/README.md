# Explanation of the program
The code is divided into 4 different 
python files 
(main.py, visualization.py, depth_first.py and A_star.py).'

## [`main.py`](main.py)
The [`main.py`](main.py) contains the main code which
calls upon the different functions in the program.
These are functions such as [`create_grid()`](visualization.py#L4) and 
[`visualize_path_with_cost()`](visualization.py#L69) 
from visualization.py.<br> 
Ofcourse there are other functions which the [`main.py`](main.py)
calls upon which calculates the depth first path or
A* path.

## [`visualization.py`](visualization.py)
This python program creates the grid and visualizes 
the path which has been found either at [`depth_first.py`](depth_first.py)
or [`A_star.py`](A_star.py).
Additionally, it adds extra information such as what
each cell costs to enter and total cost of the path
which has been taken/calculated. This is done show
clarify the result for the user.


## [`depth_first.py`](depth_first.py)
In [`depth_first.py`](depth_first.py) we have two functions,[`get_neighbors(pos, grid)`](depth_first.py#L1)
and [`depth_first_search(grid, start=(0, 1), goal=(7, 4))`](depth_first.py#L13).
The first checks all moves which it can perform and then 
stores possible moves in "neighbors".<br>
The other (depth_first_search...) defines the start position and
the goal position. After that it finds a valid position which it can move
and moves until it reaches the goal (it cannot move outside the grid nor
onto a path which has already been driven). In addition, it calculates the 
total cost of the path it went.


## [`A_star.py`](A_star.py)
[`A_star.py`](A_star.py) containts 3 functions:
* [`heuristic(node, goal)`](A_star.py#L4)
* [`get_neighbors(pos, grid)`](A_star.py#L16)
* [`a_star_search(grid, start=(0, 1), goal=(7, 4))`](A_star.py#L28)

[`heuristic(node, goal)`](A_star.py#L4) estimates
the remaining distance to the goal and then returns it.


[`get_neighbors(pos, grid)`](A_star.py#L16) checks
for the directions which can be driven (to ensure 
we stay inside the grid and don't go over our 
previous path).


[`a_star_search(grid, start=(0, 1), goal=(7, 4))`](A_star.py#L28)
is a A* algorithm which in short can be explained by the 
following list: 
* Finds the shortest path 
* Explores more promising paths first
* Consider terrain cost in its planning on the next move
* At last ofcourse it's more efficient than depth first.


 

# How to run the program
A simple step by step by on how to run the code 
(considering the user already has python 3.12 or higher
with an IDE downloaded):
1. Ensure that the given packages which are used in this
   program is downloaded. <br>If not, then use "requirements.txt"
   to download them<br>
   (a) Open the terminal <br>
   (b) Navigate to the projects directory <br>
   (c) type: pip install -r requirements.txt <br>
2. Open [`main.py`](main.py)
3. Run [`main.py`](main.py)
