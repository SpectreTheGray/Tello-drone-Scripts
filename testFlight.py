from tello import *
import time
import cv2

# Start the Tello SDK mode and the video stream
start()
start_video()
takeoff()

# Pause for 5 seconds to ensure stable flight before moving
time.sleep(5)

# Define the distance in feet
distance_feet = 4

# Convert feet to centimeters
distance_cm = int(distance_feet * 30.48)

# Move forward
forward(distance_cm)

# Pause for a moment
time.sleep(2)

# Continuously display the video feed
while True:
    # Get the latest frame from the video stream
    frame = get_video_frame()

    # Display the frame
    cv2.imshow('Tello Video Feed', frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Print remaining distance
    print("Remaining Distance:", distance_cm, "cm")

    # Check if the drone has moved forward the specified distance
    if distance_cm <= 0:
        break

    # Decrement the remaining distance
    distance_cm -= 1

# Release the video stream
stop_video()

# Move backward for the same distance
backward(int(distance_feet * 30.48))

# Get the battery level
battery_level = get_battery()
print("Battery level:", battery_level, "%")

# Land the drone
land()
