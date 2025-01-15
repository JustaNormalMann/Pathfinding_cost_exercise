import numpy as np
from heapq import heappush, heappop

def heuristic(node, goal):
    # Get x, y coordinates
    x1, y1 = node
    x2, y2 = goal
    
    # Calculate base 2D distance
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Return Euclidean distance
    return np.sqrt(dx**2 + dy**2)

def get_neighbors(pos, grid):
    rows, cols = grid.shape
    row, col = pos
    neighbors = []
    
    # Check all possible moves (up, right, down, left)
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))
    return neighbors

def a_star_search(grid, start=(0, 1), goal=(7, 4)):
    # Priority queue to store (f_cost, g_cost, position, path)
    open_set = [(0, 0, start, [start])]
    # Keep track of visited nodes and their g_costs
    closed_set = {}
    
    while open_set:
        f, g_cost, current, path = heappop(open_set)
        
        # If we reached the goal, return the path and cost
        if current == goal:
            return path, g_cost
        
        # If we've seen this node before with a better g_cost, skip it
        if current in closed_set and closed_set[current] <= g_cost:
            continue
            
        closed_set[current] = g_cost
        
        # Check all neighbors
        for neighbor in get_neighbors(current, grid):
            # Calculate new g_cost (the cost from start)
            new_g_cost = g_cost + grid[neighbor]
            
            # If we've seen this neighbor before with a better g_cost, skip it
            if neighbor in closed_set and closed_set[neighbor] <= new_g_cost:
                continue
            
            # Calculate h_cost (heuristic estimated cost to goal)
            h_cost = heuristic(neighbor, goal)
            
            # Calculate f_cost (total estimated cost)
            f_cost = new_g_cost + h_cost
            
            # Adding to open set with new path
            new_path = path + [neighbor]
            heappush(open_set, (f_cost, new_g_cost, neighbor, new_path))
    
    return None, None  # No path found
