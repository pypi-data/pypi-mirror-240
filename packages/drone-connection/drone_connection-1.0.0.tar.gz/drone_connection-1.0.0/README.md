Drone Connector 

## Usage

```python
    from drone_connection import DroneConnector

    # Create a drone connection
    drone = DroneConnector(address='127.0.0.1', port=14550)


    # Connect to the drone
    drone.connect()


    # Send command to the drone
    drone.sendCommand('takeoff')


    # Disconnect from the drone
    drone.disconnect()