from consentiumthings import consentiumthings

# Take user input for board key, send key, and receive key
board_key = input("Enter board key: ")
send_key = input("Enter send key: ")
receive_key = input("Enter receive key: ")

# Take user input for 4 sensor names and values
sensor_data = {}
for i in range(1, 5):
    sensor_name = input(f"Enter sensor name for sensor {i}: ")
    sensor_value = input(f"Enter value for {sensor_name}: ")
    sensor_data[sensor_name] = sensor_value

# Initialize ConsentiumThings
ct = consentiumthings(board_key)

# Send data
ct.begin_send(send_key)
ct.send_data(list(sensor_data.values()), list(sensor_data.keys()))

# Receive data
ct.begin_receive(receive_key, recent=False)
print(ct.receive_data())
