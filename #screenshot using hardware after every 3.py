'''import pyautogui
import os
import time

# Path to the directory to save screenshots
path = "C:/Screenshot/"

# Create the directory if it doesn't exist
os.makedirs(path, exist_ok=True)

# Loop to capture screenshots every 3 seconds
for i in range(5):
    time.sleep(3)  # Adjusted sleep time to 3 seconds
    # Generate filename based on current time
    filename = f"screenshot_{i+1}.png"
    # Join path and filename
    filepath = os.path.join(path, filename)
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        # Save screenshot
        screenshot.save(filepath)
        print(f"9Screenshot {i+1} captured successfully!")
    except Exception as e:
        print(f"Error capturing screenshot {i+1}: {e}")

print("Screenshots captured successfully!")
import pyautogui
import os
import time

# Path to the directory to save screenshots
path = "2"

# Create the directory if it doesn't exist
try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")
except OSError as e:
    print(f"Error creating directory: {e}")
    exit()

# Loop to capture screenshots every 3 seconds
for i in range(5):
    time.sleep(3)  # Adjusted sleep time to 3 seconds
    # Generate filename based on current time
    filename = f"screenshot_{i+1}.png"
    # Join path and filename
    filepath = os.path.join(path, filename)
    try:
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        print("Screenshot taken successfully.")
        # Save screenshot
        screenshot.save(filepath)
        print(f"Screenshot {i+1} saved successfully to '{filepath}'.")
    except Exception as e:
        print(f"Error capturing or saving screenshot {i+1}: {e}")

print("Screenshots captured successfully!")'''
import pyautogui
import os
import time
from datetime import datetime

# Path to the directory to save screenshots
path = "C:\\mera folder"

# Create the directory if it doesn't exist
try:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")
except OSError as e:
    print(f"Error creating directory: {e}")
    exit(1)

# Loop to capture screenshots every 3 seconds
for i in range(5):
    try:
        time.sleep(3)  # Adjusted sleep time to 3 seconds
        # Generate filename based on current date and time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        # Join path and filename
        filepath = os.path.join(path, filename)
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        print(f"Screenshot taken successfully.")
        # Save screenshot
        screenshot.save(filepath)
        print(f"Screenshot saved successfully to '{filepath}'.")
    except pyautogui.FailSafeException as e:
        print(f"PyAutoGUI fail-safe triggered: {e}")
    except OSError as e:
        print(f"OS error: {e}")
    except Exception as e:
        print(f"Unexpected error capturing or saving screenshot: {e}")

print("Screenshots captured successfully!")