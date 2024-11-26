import pybullet as p

# Connect to PyBullet GUI
physicsClient = p.connect(p.GUI)

# Disconnect from PyBullet
p.disconnect()
