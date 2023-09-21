"""
The program below reads a set of movement instructions from a file. Gets the robot to execute
those movement commands as defined in the functions below 
"""

from gpiozero import CamJamKitRobot

from gpiozero import DistanceSensor
from time import sleep


robot = CamJamKitRobot()


# Either moves forward or backwards or stops
def linear(speed, duration, direction):
    if direction == "Forwards":
        robot.value = (speed, speed)  # left and right speed of robot wheel
    elif direction == "Backwards":
        robot.value = (-speed, -speed)  # left and right speed of robot wheel
    elif direction == "Stop":
        robot.value = (0, 0)  # left and right speed of robot wheel
    sleep(duration)
    print(f"{direction} {speed} {speed} {duration}s")


# Either moves right or left
def turn(speed, duration, direction):
    if direction == "Left":
        robot.value = (0, speed)  # left and right speed of robot wheel
    elif direction == "Right":
        robot.value = (speed, 0)  # left and right speed of robot wheel
    sleep(duration)
    print(f"{direction} {speed} {speed} {duration}s")


# Either rotates clockwise or anti clockwise
def rotate(speed, duration, direction):
    if direction == "cw":
        robot.value = (speed, -speed)  # left and right speed of robot wheel
    elif direction == "ccw":
        robot.value = (-speed, speed)  # left and right speed of robot wheel
    sleep(duration)
    print(f"{direction} {speed} {speed} {duration}s")


# Reads the set of movement commands from the file, and get the robot to execute those movements.
with open("instructions.txt", "r") as file:
    for lines in file:
        lines = lines.rstrip()
        lines = lines.split(",")
        print(lines)
        if lines[0].strip('"') == "linear":
            linear(float(lines[1]), float(lines[2]), lines[3].strip('"'))
        elif lines[0].strip('"') == "turn":
            turn(float(lines[1]), float(lines[2]), lines[3].strip('"'))
        else:
            rotate(float(lines[1]), float(lines[2]), lines[3].strip('"'))
