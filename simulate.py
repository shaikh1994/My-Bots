import pybullet as p
import time
import pybullet_data



# Connect to the PyBullet GUI
p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Optionally disable the sidebars to speed up simulation
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("block_grid.sdf")


# Load the world with multiple links
# p.loadSDF("world.sdf")

# Loop to step through the simulation
for i in range(1000):
    p.stepSimulation()  # Step the physics simulation
    time.sleep(1 / 60)  # Slow down the simulation by 1/60th of a second
    print(i)  # Print the loop variable

# Disconnect from the simulation
p.disconnect()
