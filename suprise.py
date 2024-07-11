import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser
import platform
import time

def prank():
    # Open the default web browser with the specified link after delay
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Determine delay for message box based on system architecture
    if platform.architecture()[0] == "64bit":
        time.sleep(2)  # Delay for 2 seconds for 64-bit systems
    else:
        time.sleep(10)  # Delay for 10 seconds for 32-bit systems

    # Create a tkinter Toplevel window for the message box
    message_box = tk.Toplevel()
    message_box.title("Prank Alert")
    message_box.geometry("300x150")

    # Label with prank message
    label = tk.Label(message_box, text="You just got pranked!")
    label.pack(pady=10)

    # Function to close both windows (message box and main window)
    def close_windows():
        message_box.destroy()
        window.destroy()

    # OK button to close both windows
    ok_button = tk.Button(message_box, text="OK", command=close_windows)
    ok_button.pack(pady=10)

# Hide the command prompt window
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# Create a tkinter window
window = tk.Tk()
window.title("Cool")  # Set window title to "Cool"
window.geometry("300x100")  # Set window size

# Start the prank function (which opens the rickroll link and displays message box)
prank()

# Start the tkinter main loop
window.mainloop()
