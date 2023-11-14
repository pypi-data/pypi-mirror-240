## Usage

*. **Import packages:**

    ```python

    from drone_connection import DroneConnection

    # Create a drone connection instance
    drone = DroneConnection(address='127.0.0.1', port=14550)

    # Connect to the drone
    drone.connect()

    # Send a command to the drone
    drone.send_command('takeoff')

    # Receive data from the drone
    drone.receive_data()

    # Disconnect from the drone
    drone.disconnect()