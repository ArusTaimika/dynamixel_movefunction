import time

from Dynamixel import Dynamixel


def __init__():
    DXL_IDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    BAUDRATE = 57600
    DEVICENAME = "/dev/ttyUSB0"
    dxl = Dynamixel(DEVICENAME, BAUDRATE)
    dxl.setRecommendedValue(DXL_IDs)
    testReadWriteVelocity(dxl, DXL_IDs)


def testReadWriteVelocity(dxl: Dynamixel, DXL_IDs):
    # Torque off
    dxl.writeTorqueEnable(DXL_IDs, [0] * len(DXL_IDs))

    # Set operating mode velocity
    dxl.writeOperatingMode(DXL_IDs, [1] * len(DXL_IDs))
    # Torque on
    dxl.writeTorqueEnable(DXL_IDs, [1] * len(DXL_IDs))

    # start = time.time()
    # Set velocity

    # dyn.writeGoalVelocity(DXL_IDs, [200] * len(DXL_IDs))
    # time.sleep(100)

    i = 0

    while True:
        # dxl.writeGoalVelocity(DXL_IDs, [4] * len(DXL_IDs))
        for i in range(0, 200,1):
            dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs))
            time.sleep(0.1)
        for i in range(200, -200, -1):
            dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs))
            time.sleep(0.1)
        for i in range(-200, 0, 1):
            dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs))
            time.sleep(0.1)

    # dyn.writeGoalVelocity(DXL_IDs, [0] * len(DXL_IDs))
    # time.sleep(1)
    # # Torque off
    # dyn.writeTorqueEnable(DXL_IDs, [0]* len(DXL_IDs))


if __name__ == "__main__":
    __init__()