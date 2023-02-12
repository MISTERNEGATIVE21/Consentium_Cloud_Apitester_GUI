import tkinter 
from ConsentiumThingsPy import ThingsUpdate
import time

from tkinter import ttk

import sv_ttk


  
def handle_input():
    api_key= api_key_field.get()
    sensor1= sensor1_field.get()
    sensor2= sensor2_field.get()
    sensor3= sensor3_field.get()
    sensor4= sensor4_field.get()
    sensor5= sensor5_field.get()
    sensor6= sensor6_field.get()
    sensor7= sensor7_field.get()
    print(f"Input value: {api_key}")
    board = ThingsUpdate(key=api_key)

    sensor_val = [sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7]
    info_buff = ["a", "b", "c", "d", "e", "f", "g"]
    r = board.sendREST(sensor_val=sensor_val, info_buff=info_buff)
    print(r)
    time.sleep(5)

root = tkinter.Tk()
root.title("CONSENTIUM CLOUD DASHBOARD")
api_key_label = ttk.Label(root, text="Enter the API Key:")
api_key_label.pack()
api_key_field = ttk.Entry(root)
api_key_field.pack()

sensor1_label = ttk.Label(root, text="Enter the Sensor value 1:")
sensor1_label.pack()
sensor1_field = ttk.Entry(root)
sensor1_field.pack()
sensor2_label = ttk.Label(root, text="Enter the Sensor value 2:")
sensor2_label.pack()
sensor2_field = ttk.Entry(root)
sensor2_field.pack()
sensor3_label = ttk.Label(root, text="Enter the Sensor value 3:")
sensor3_label.pack()
sensor3_field = ttk.Entry(root)
sensor3_field.pack()
sensor4_label = ttk.Label(root, text="Enter the Sensor value 4:")
sensor4_label.pack()
sensor4_field = ttk.Entry(root)
sensor4_field.pack()
sensor5_label = ttk.Label(root, text="Enter the Sensor value 5:")
sensor5_label.pack()
sensor5_field = ttk.Entry(root)
sensor5_field.pack()
sensor6_label = ttk.Label(root, text="Enter the Sensor value 6:")
sensor6_label.pack()
sensor6_field = ttk.Entry(root)
sensor6_field.pack()
sensor7_label = ttk.Label(root, text="Enter the Sensor value 7:")
sensor7_label.pack()
sensor7_field = ttk.Entry(root)
sensor7_field.pack()
sensor7_button = ttk.Button(root, text="Submit", command=handle_input)
sensor7_button.pack()

def toggle_theme():
    if sv_ttk.get_theme() == "dark":
        print("Setting theme to light")
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == "light":
        print("Setting theme to dark")
        sv_ttk.use_dark_theme()
    else:
        print("Not Sun Valley theme")

button = ttk.Button(root, text="Toggle theme", command=toggle_theme)
button.pack()

root.mainloop()
end()