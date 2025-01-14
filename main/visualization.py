import numpy as np
import matplotlib.pyplot as plt

def create_grid():
    # Create a 9x6 grid
    grid = np.ones((9, 6))
    
    # Adding green cells
    green_cells = [
        (0, 2), (0, 3),
        (3, 4), (4, 3), (4, 4),
        (6, 1)
    ]
    
    # Adding red cells
    red_cells = [
        (3, 2), (3, 3),
        (6, 2), (6, 3),
        (8, 1)
    ]
    
    # Set the costs in the grid
    for i, j in green_cells:
        grid[i, j] = 2
    for i, j in red_cells:
        grid[i, j] = 10
        
    return grid

def visualize_grid(grid):
    fig, ax = plt.subplots(figsize=(8, 12))
    
    # Create color map
    cmap = plt.cm.colors.ListedColormap(['white', 'green', 'red'])
    bounds = [0.5, 1.5, 2.5, 10.5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
    # Plot the grid
    ax.imshow(grid, cmap=cmap, norm=norm)
    
    # Add grid lines
    ax.grid(True, which='major', color='black', linewidth=2)
    
    # Add cost labels to each cell
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            cost = grid[i, j]
            if cost == 1:
                label = 'x1'
            elif cost == 2:
                label = 'x2'
            else:
                label = 'x10'
            # Position text in top right corner with small offset
            ax.text(j + 0.3, i - 0.3, label, ha='center', va='center', fontsize=6, color='black')
    
    # Add Start and Goal text with bold weight
    ax.text(1, 0, 'Start', ha='center', va='center', weight='bold')
    ax.text(4, 7, 'Goal', ha='center', va='center', weight='bold')
    
    # Set ticks
    ax.set_xticks(np.arange(-0.5, 6, 1))
    ax.set_yticks(np.arange(-0.5, 9, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    #plt.show()

def visualize_path_with_cost(grid, path, total_cost):
    fig, ax = plt.subplots(figsize=(8, 12))
    
    # Create color map
    cmap = plt.cm.colors.ListedColormap(['white', 'green', 'red'])
    bounds = [0.5, 1.5, 2.5, 10.5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
    # Plot the grid
    ax.imshow(grid, cmap=cmap, norm=norm)
    
    # Adding grid lines
    ax.grid(True, which='major', color='black', linewidth=2)
    
    # Adding cost labels to each cell
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            cost = grid[i, j]
            if cost == 1:
                label = 'x1'
            elif cost == 2:
                label = 'x2'
            else:
                label = 'x10'
            ax.text(j + 0.3, i - 0.3, label, ha='center', va='center', fontsize=6, color='black')
    
    # Adding Start and Goal text
    ax.text(1, 0, 'Start', ha='center', va='center', weight='bold')
    ax.text(4, 7, 'Goal', ha='center', va='center', weight='bold')
    
    # Plot the path
    if path:
        path = np.array(path)
        ax.plot(path[:, 1], path[:, 0], 'c-', linewidth=2, label=f'Path (Cost: {int(total_cost)})')
        ax.plot(path[:, 1], path[:, 0], 'co', markersize=8)
    
    # Legend with total cost
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
    
    # Set ticks
    ax.set_xticks(np.arange(-0.5, 6, 1))
    ax.set_yticks(np.arange(-0.5, 9, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    plt.show()

#grid = create_grid()
#visualize_grid(grid)
