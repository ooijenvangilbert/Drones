from robomaster import robot

drone = robot.Drone()

drone.initialize()
drone_version = drone.get_sdk_version()
print("Drone sdk version : {0}".format(drone_version))

drone.close()
