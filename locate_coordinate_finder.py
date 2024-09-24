import pyautogui
import time

# Function to get the screen coordinates
def get_coordinates():
    print("Move your mouse to the desired position and press Ctrl+C to capture the coordinates.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"X: {x}, Y: {y}", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nCoordinates captured.")

# Uncomment the following line to get the coordinates
get_coordinates()

# Coordinates for Viber icon, chat, and message input field
viber_icon_coords = (100, 200)  # Example coordinates, replace with actual
chat_coords =  (500, 600)      # Example coordinates, replace with actual
