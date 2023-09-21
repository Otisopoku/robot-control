"""
In this program, a set of instructions are read from a file. The robot is made to carry out those set of instruction movements as long as the sensor 
of the robot does not detect any obstacle within a range of 100cm distance. If it does, it performs set of avoidance movements as described in the code
"""

from gpiozero import CamJamKitRobot
from gpiozero import LED, DistanceSensor
from time import sleep


robot = CamJamKitRobot()

sensor = DistanceSensor(echo=18, trigger=17, max_distance=1)


# Either moves the robot foward or backward or stops
def linear(speed, duration, direction):
    if direction == "Forwards":
        robot.value = (speed, speed)
    elif direction == "Backwards":
        robot.value = (-speed, -speed)
    elif direction == "Stop":
        robot.value = (0, 0)
    sleep(duration)


# Either moves the robot left or right
def turn(speed, duration, direction):
    if direction == "Left":
        robot.value = (0, speed)

    elif direction == "Right":
        robot.value = (speed, 0)

    sleep(duration)


# Either rotates the robot clockwise or anti clockwise
def rotate(speed, duration, direction):
    if direction == "cw":
        robot.value = (speed, -speed)

    elif direction == "ccw":
        robot.value = (-speed, speed)

    sleep(duration)


# Prints the distance between the sensor and a head on obstacle of the robot
def print_d():
    for i in range(0, 10):
        print(
            f"{direction} {speed} {speed} {duration}s Distance_of_obstacle{sensor.distance* 100 :.2f}"
        )
        sleep(0.1)


# Once the sensor of the robot detects that an object is less that 100cm from it, it performs the following operations to avoid the obstacle
def avoidance():
    # moves backwards and prints the distance of any head-on obstacle
    linear(0.75, 1, "Backwards")
    for i in range(0, 10):
        print(f"Backward 0.75 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # rotates anti clockwise and prints the distance of any head-on obstacle
    rotate(0.5, 1, "ccw")
    for i in range(0, 10):
        print(f"ccw 0.5 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # moves forward and prints the distance of any head-on obstacle
    linear(0.5, 1, "Forwards")
    for i in range(0, 10):
        print(f"Forwards 0.75 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # rotates clockwise and prints the distance of any head-one obstacle
    rotate(0.5, 1, "cw")
    for i in range(0, 10):
        print(f"cw 0.5 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # moves forwards and prints the distance of any head-on obstacle
    linear(0.5, 1, "Forwards")
    for i in range(0, 10):
        print(f"Forwards 0.5 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # rotates clockwis and prints the distance of any head on obstacle
    rotate(0.5, 1, "cw")
    for i in range(0, 10):
        print(f"cw 0.5 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # moves forward and prints the distance of any head-on obstacle
    linear(0.5, 1, "Forwards")
    for i in range(0, 10):
        print(f"Forwards 0.5 1s {sensor.distance * 100:.2f}cm")
        sleep(0.1)
    # rotates anti clockwise and prints the distance of any head-on obstacle
    rotate(0.5, 1, "ccw")
    for i in range(0, 10):
        print(f"ccw 0.5 1s {sensor.distance * 100:.2f}")
        sleep(0.1)


# Reads and stores the set of commands to be executed by the robot from the instructions.txt file
with open("instructions.txt", "r") as file:
    instructions = []
    for line in file:
        lines = line.rstrip().split(",")
        instructions.append(lines)

# Continuously moves the robot until the user terminates the program.
# As long as there is no obstacle detected by the robot sensor within a range of 10cm, the robot executes the commands read from the instructions.txt file
# Otherwise, the robot performs the obstacle avaidance technique described above.
while True:
    for instruction in instructions:
        if sensor.distance > 0.1:
            duration = float(instruction[2])
            speed = float(instruction[1])
            direction = instruction[3]

            if instruction[0] == "linear":
                linear(speed, duration, direction)
            elif instruction[0] == "turn":
                turn(speed, duration, direction)
            else:
                rotate(speed, duration, direction)
        else:
            avoidance()
