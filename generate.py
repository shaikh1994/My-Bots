import pyrosim.pyrosim as pyrosim

# Start creating the SDF file
pyrosim.Start_SDF("block_grid.sdf")

# Parameters for the grid
rows = 5  # Number of rows in the grid
columns = 5  # Number of columns in the grid
tower_height = 5  # Number of blocks in each tower
initial_size = [1, 1, 1]  # Initial size of each block
scaling_factor = 0.9  # Scaling factor for the size of blocks in each tower

# Nested loops to create a grid of towers
for row in range(rows):
    for col in range(columns):
        # Base x, y position for the tower
        x_position = row * 2  # Spacing between rows
        y_position = col * 2  # Spacing between columns
        
        # Create a tower at the current grid position
        for height in range(tower_height):
            # Calculate z-coordinate and size for the current block
            z_position = 0.5 + sum(initial_size[2] * (scaling_factor**h) for h in range(height))
            size = [dimension * (scaling_factor**height) for dimension in initial_size]

            # Add the block to the world
            pyrosim.Send_Cube(name=f"Block_{row}_{col}_{height}", pos=[x_position, y_position, z_position], size=size)

# End the SDF creation
pyrosim.End()
