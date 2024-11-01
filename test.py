import time

from Dynamixel import Dynamixel, Test_Dynamixel


def __init__():
    DXL_IDs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] # 動かしたいサーボのIDを指定
    BAUDRATE = 57600            # 基本変更しなくてよし
    DEVICENAME = "/dev/ttyUSB0" # 接続されているポート指定
    dxl = Dynamixel(DEVICENAME, BAUDRATE)   # Dynamixelクラスイニシャライズ
    dxl.setRecommendedValue(DXL_IDs)        # 動かすサーボの初期化
    
    test_dynamixel = Test_Dynamixel()
    test_dynamixel.testReadWriteCurrent(dxl, DXL_IDs)     # テスト関数呼び出し
    test_dynamixel.testReadWritePosition(dxl, DXL_IDs)    # テスト関数呼び出し
    test_dynamixel.testReadWriteVelocity(dxl, DXL_IDs)    # テスト関数呼び出し
    
    #testwriteroop(dxl, DXL_IDs)     # 無限ループテストコード

def testwriteroop(dxl: Dynamixel, DXL_IDs):
    """_summary_
        無限ループテストコード

    Args:
        dxl (Dynamixel): Dynamixel class
        DXL_IDs (_type_): ID list
    """
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
    try:
        print("------- run test code -------")
        while True:
            # dxl.writeGoalVelocity(DXL_IDs, [4] * len(DXL_IDs))
            for i in range(0, 200,1):
                dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs)) # 基本どの関数も，IDのリスト，値のリストで動く
                time.sleep(0.1)
            for i in range(200, -200, -1):
                dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs))
                time.sleep(0.1)
            for i in range(-200, 0, 1):
                dxl.writeGoalVelocity(DXL_IDs, [i] * len(DXL_IDs))
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("------- end test code -------")
        #Torque off
        dxl.writeTorqueEnable(DXL_IDs, [0]* len(DXL_IDs))


if __name__ == "__main__":
    __init__()
