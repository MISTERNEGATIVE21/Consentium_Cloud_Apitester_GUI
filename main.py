import tkinter as tk
from consentiumthings import consentiumthings

def send_data():
    board_key = board_key_entry.get()
    send_key = send_key_entry.get()
    receive_key = receive_key_entry.get()

    sensor_data = {}
    for i in range(1, 5):
        sensor_name = sensor_name_entries[i-1].get()
        sensor_value = sensor_value_entries[i-1].get()
        sensor_data[sensor_name] = sensor_value

    ct = consentiumthings(board_key)

    # Send data
    ct.begin_send(send_key)
    ct.send_data(list(sensor_data.values()), list(sensor_data.keys()))

    # Receive data
    ct.begin_receive(receive_key, recent=False)
    result_label.config(text=ct.receive_data())

# Create the main window
root = tk.Tk()
root.title("ConsentiumThings GUI")

# Create and place labels and entries
tk.Label(root, text="Board Key:").grid(row=0, column=0, padx=5, pady=5)
board_key_entry = tk.Entry(root)
board_key_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Send Key:").grid(row=1, column=0, padx=5, pady=5)
send_key_entry = tk.Entry(root)
send_key_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Receive Key:").grid(row=2, column=0, padx=5, pady=5)
receive_key_entry = tk.Entry(root)
receive_key_entry.grid(row=2, column=1, padx=5, pady=5)

sensor_name_entries = []
sensor_value_entries = []

# Create fixed input boxes for sensor names and data
sensor_names = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"]
for i, sensor_name in enumerate(sensor_names):
    tk.Label(root, text=f"{sensor_name} Name:").grid(row=i+3, column=0, padx=5, pady=5)
    sensor_name_entry = tk.Entry(root)
    sensor_name_entry.grid(row=i+3, column=1, padx=5, pady=5)
    sensor_name_entry.insert(0, sensor_name)
    sensor_name_entries.append(sensor_name_entry)

    tk.Label(root, text=f"{sensor_name} Value:").grid(row=i+3, column=2, padx=5, pady=5)
    sensor_value_entry = tk.Entry(root)
    sensor_value_entry.grid(row=i+3, column=3, padx=5, pady=5)
    sensor_value_entries.append(sensor_value_entry)

# Create and place the send button
send_button = tk.Button(root, text="Send Data", command=send_data)
send_button.grid(row=8, column=0, columnspan=4, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=4, pady=10)

# Start the GUI
root.mainloop()
