from tello import *

start()
takeoff()

distance_feet = 2

# Convert feet to centimeters
distance_cm = int(distance_feet * 30.48)

# Move forward
left(distance_cm)

up(distance_cm)

right(distance_cm)

down(distance_cm)

land()
