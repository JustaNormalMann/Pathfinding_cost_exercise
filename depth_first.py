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

def depth_first_search(grid, start=(0, 1), goal=(7, 4)):
    stack = [(start, [start], 0)]  # (current_pos, path, total_cost)
    visited = set()
    
    while stack:
        current_pos, path, cost = stack.pop()
        
        if current_pos == goal:
            return path, cost
        
        if current_pos not in visited:
            visited.add(current_pos)
            
            for neighbor in get_neighbors(current_pos, grid):
                if neighbor not in visited:
                    new_cost = cost + grid[neighbor]
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path, new_cost))
    
    return None, None  # No path found