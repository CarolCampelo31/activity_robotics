import time

from niryosim import NiryoSim

nyrio_robot = NiryoSim('127.0.0.1')

# Init Axes
nyrio_robot.init6Axes()

# Move to Default Position
nyrio_robot.moveToHome()

nyrio_robot.closeGripper()

# input("Press ENTER to start Pick n Place Test...")

nyrio_robot.openGripper() # open gripper
time.sleep(4)

# Start Movement

nyrio_robot.moveJoints(0, 0, -30, 90, 0, 0)  # move joint_4 in 90 degrees
time.sleep(5)

nyrio_robot.moveJoints(0, 90, 0, 0, 0, 0)  # move joint_2 in 90 degrees
time.sleep(5)

nyrio_robot.moveJoints(90, 0, 0, 0, 0, 0)  # move joint_1 in 90 degrees
time.sleep(5)

nyrio_robot.closeGripper()  # close gripper
time.sleep(30)


nyrio_robot.openGripper()
time.sleep(2)

# Move to Default Position
nyrio_robot.moveToHome()
time.sleep(4)

