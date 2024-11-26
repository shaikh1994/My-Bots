import pyrosim.pyrosim as pyrosim

# Start creating the SDF file
pyrosim.Start_SDF("box.sdf")

# Add a cube to the world
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

# End the SDF creation
pyrosim.End()
