import tkinter
from consentiumthings import consentiumthings
import time
from tkinter import ttk
import sv_ttk

def handle_input():
    api_key = api_key_field.get()
    board_key = board_key_field.get()
    sensor_values = [sensor1_field.get(), sensor2_field.get(), sensor3_field.get(),
                     sensor4_field.get(), sensor5_field.get(), sensor6_field.get(), sensor7_field.get()]

    print(f"Input values: API Key - {api_key}, Board Key - {board_key}")

    # Create an instance of ConsentiumThings with the API key and board key
    ct = consentiumthings(api_key, board_key)

    # Your remaining code for handling sensor values and sending data
    info_buff = ["a", "b", "c", "d", "e", "f", "g"]
    r = ct.begin_send("send_key")
    ct.send_data(sensor_values, info_buff)
    received_data = ct.receive_data()
    print(received_data)

    # For demonstration purposes, sleep for 5 seconds (adjust as needed)
    time.sleep(5)

# Create the main tkinter window
root = tkinter.Tk()
root.title("CONSENTIUM CLOUD DASHBOARD")

# Entry for API key
api_key_label = ttk.Label(root, text="Enter the API Key:")
api_key_label.pack()
api_key_field = ttk.Entry(root)
api_key_field.pack()

# Entry for Board key
board_key_label = ttk.Label(root, text="Enter the Board Key:")
board_key_label.pack()
board_key_field = ttk.Entry(root)
board_key_field.pack()

# Entries for sensor values
sensor_labels = ["Sensor value 1", "Sensor value 2", "Sensor value 3",
                  "Sensor value 4", "Sensor value 5", "Sensor value 6", "Sensor value 7"]

for label_text in sensor_labels:
    sensor_label = ttk.Label(root, text=f"Enter the {label_text}:")
    sensor_label.pack()
    sensor_entry = ttk.Entry(root)
    sensor_entry.pack()

# Button to submit data
submit_button = ttk.Button(root, text="Submit", command=handle_input)
submit_button.pack()

def toggle_theme():
    # Toggle between dark and light themes
    if sv_ttk.get_theme() == "dark":
        print("Setting theme to light")
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == "light":
        print("Setting theme to dark")
        sv_ttk.use_dark_theme()
    else:
        print("Not Sun Valley theme")

# Button to toggle theme
theme_button = ttk.Button(root, text="Toggle theme", command=toggle_theme)
theme_button.pack()

# Run the tkinter main loop
root.mainloop()
