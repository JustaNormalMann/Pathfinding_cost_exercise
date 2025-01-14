from visualization import create_grid, visualize_path_with_cost
from depth_first import depth_first_search
from A_star import a_star_search

# Create the grid
grid = create_grid()
    
# Find path using DFS
dfs_path, dfs_cost = depth_first_search(grid)
if dfs_path:
    #print(f"Depth First path found with total cost: {int(dfs_cost)}")
    #print(f"Depth First path: {dfs_path}")
    visualize_path_with_cost(grid, dfs_path, dfs_cost)
    
# Find path using A*
astar_path, astar_cost = a_star_search(grid)
if astar_path:
    #print(f"\nA* Path found with total cost: {int(astar_cost)}")
    #print(f"A* Path: {astar_path}")
    visualize_path_with_cost(grid, astar_path, astar_cost)
