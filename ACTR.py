import time
import Dynamixel
import os

def __init__():
    DXL_IDs = [1,2]
    BAUDRATE = 57600
    DEVICENAME = "/dev/ttyUSB0"
    dxl = Dynamixel.Dynamixel(DEVICENAME, BAUDRATE)
    dxl.setRecommendedValue(DXL_IDs)
    #testReadWriteCurrent(dxl,DXL_IDs)
    testReadWritePosition(dxl,DXL_IDs)

def testReadWritePosition(dyn, DXL_IDs):
    dyn.writeTorqueEnable(DXL_IDs, [0, 0])
    dyn.writeOperatingMode(DXL_IDs, [3, 3])
    dyn.writeTorqueEnable(DXL_IDs, [1, 1])

    start = time.time()
    dyn.writeGoalPosition(DXL_IDs, [0,0])
    elapsed_time = time.time() - start
    print ("elapsed_time(write):{0}".format(elapsed_time*1000) + "[msec]")
    time.sleep(1.0)
    start = time.time()
    pos = dyn.readPresentPosition(DXL_IDs)
    elapsed_time = time.time() - start
    print(pos)
    print ("elapsed_time(read):{0}".format(elapsed_time*1000) + "[msec]")
    dyn.writeGoalPosition(DXL_IDs, [2000,1000])
    time.sleep(1.0)
    start = time.time()
    pos = dyn.readPresentPosition(DXL_IDs)
    elapsed_time = time.time() - start
    print(pos)
    print ("elapsed_time(read):{0}".format(elapsed_time*1000) + "[msec]")
    dyn.writeTorqueEnable(DXL_IDs, [0, 0])
    # ret, elapsed_time = timeMesurement(dyn.writeGoalPosition, 2, DXL_IDs, [0,0])
    # print("Spent time = %.3f(msec)" % (elapsed_time*1000))

def testReadWriteCurrent(dxl: Dynamixel.Dynamixel, DXL_IDs):

    # Torque off
    dxl.writeTorqueEnable(DXL_IDs, [0] * 2)
    # Set operating mode velocity
    dxl.writeOperatingMode(DXL_IDs, [0] * 2)
    # Torque on
    dxl.writeTorqueEnable(DXL_IDs, [1] * 2)

    # start = time.time()
    # Set velocity

    #dxl.writeGoalVelocity(DXL_IDs, [200] * len(DXL_IDs))
    #time.sleep(100)
    #dxl.writeGoalCurrent(DXL_IDs, [50] * len(DXL_IDs))
    #print(dxl.readPresentCurrent(DXL_IDs))
    #time.sleep(10)

    # dxl.writeGoalVelocity(DXL_IDs, [4] * len(DXL_IDs))
    dxl.writeGoalCurrent(DXL_IDs, [200,200])
    time.sleep(0.05)
    #os.system('clear')
    #print(dxl.readPresentCurrent([1]), dxl.readPresentCurrent([2]))
    time.sleep(5)
    
    # dyn.writeGoalVelocity(DXL_IDs, [0] * len(DXL_IDs))
    # time.sleep(1)
    # Torque off
    dxl.writeTorqueEnable(DXL_IDs, [0]*2)


if __name__ == "__main__":
    __init__()
