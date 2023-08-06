# return bytes(bytearray([int(data)]))
import serial
import time
import signal
import threading
from WizData import Common
from WizDefaultSensor import WizSensorData


class WizSerial:
    ser = None

    def __init__(self, port, sensorDataManager=WizSensorData(), baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
        self.ser = serial.Serial()

        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.bytesize = bytesize
        self.ser.parity = parity
        self.ser.stopbits = stopbits
        self.ser.timeout = timeout
        self.ser.xonxoff = xonxoff
        self.ser.rtscts = rtscts
        self.ser.dsrdtr = dsrdtr

        # self.reset()
        self.ser.open()

        self.exitThread = False  # 쓰레드 종료용 변수
        self.ackData = []
        self.sensorRawBuf = []
        self.processedData = None
        self.wizSensorData = sensorDataManager
        self.sensorData = self.wizSensorData.sensorData
        self.isAck = threading.Event()
        signal.signal(signal.SIGINT, self.readThreadHandler)
        self.thread_read = threading.Thread(target=self.readThread)  # args=(self.ser,)
        self.thread_read.start()

    def reset(self):
        self.ser.dtr=False
        self.ser.rts=True
        self.ser.dtr=False
        self.ser.rts=False

    def write(self, data):  # 일단 리스트( ex: [1,2,...] )형태만 가정함
        self.ser.write(bytes(bytearray(data)))
        self.isAck.clear()  # 이벤트 플래그 false
        self.isAck.wait()  # timeout을 주고 is_set()을 물어봐서 타임아웃에러를 Raise할수도 있음

    def getData(self):  # writeAndWaitAck 이후에 바로 사용함
        tmp = self.processedData
        self.processedData = None
        return tmp

    def getSensorDataManager(self) -> WizSensorData:
        return self.wizSensorData

    def _write(self, data):  # 일단 리스트( ex: [1,2,...] )형태만 가정함
        self.ser.write(bytes(bytearray(data)))
        # time.sleep(0.05)

    def processAckData(self):
        if self.ackData[1] == 1:  # sendInt()
            r = self.ackData[3] * 127 + self.ackData[4]
            if self.ackData[2] == 1:
                r *= -1
            self.processedData = r
        elif self.ackData[1] == 3:  # sendFloat()
            _sign = self.ackData[2] & 0x80
            firstData = self.ackData[2] & 0x7f
            data = firstData << 8 | self.ackData[3]
            if _sign == 1:
                data *= -1
            data /= 10
            self.processedData = data
        elif self.ackData[1] == 4:  # sendToString()
            msgLength = self.ackData[0] - 2
            msg = ""
            for i in range(msgLength):
                asc = self.ackData[i + 2]
                if asc != 13:  # carriage_return : 13
                    msg += chr(asc)
            self.processedData = msg
        elif self.ackData[1] == 5:  # sendBool()
            self.processedData = False if self.ackData[2] == 0 else True
        elif self.ackData[1] == 6:  # runOK()
            self.processedData = "runOk"
        elif self.ackData[1] == 7:  # sendInt2() - uint
            r = self.ackData[2] << 8 | self.ackData[3]
            self.processedData = r
        else:
            raise RuntimeError("Unknown Data Received")
        self.ackData.clear()  # 처리 후 지움
        self.isAck.set()  # 이벤트 플래그 true

    def processSensorData(self):
        if self.sensorRawBuf[1] == 10:  # 코드위즈 기본 센서 1
            self.saveCodewizBoardSensorValue1()
        elif self.sensorRawBuf[1] == 11:  # 코드위즈 기본 센서 2
            self.saveCodewizBoardSensorValue2()

        self.sensorRawBuf.clear()  # 처리 후 지움

    def readThreadHandler(self, signum=None, frame=None):
        self.exitThread = True

    def readThread(self):
        _state = 1
        _receiveLength = 0
        _receiveSensorLength = 0
        # 쓰레드 종료될때까지 계속 돌림
        while not self.exitThread:
            # 데이터가 있있다면
            for c in self.ser.read():
                if _state == 1:
                    if c == 255:
                        _state = 2
                elif _state == 2:
                    if c == 254:
                        _state = 3
                    elif c == 253:
                        _state = 13

                elif _state == 3:
                    _state = 4
                    _receiveLength = c - 1
                    self.ackData.append(c)
                elif _state == 4:
                    if _receiveLength > 1:
                        self.ackData.append(c)
                        _receiveLength -= 1
                    elif _receiveLength == 1:
                        self.ackData.append(c)
                        _receiveLength = 0
                        _state = 1
                        self.processAckData()

                elif _state == 13:
                    _state = 14
                    _receiveSensorLength = c - 1
                    self.sensorRawBuf.append(c)
                elif _state == 14:
                    if _receiveSensorLength > 1:
                        self.sensorRawBuf.append(c)
                        _receiveSensorLength -= 1
                    elif _receiveSensorLength == 1:
                        self.sensorRawBuf.append(c)
                        _receiveSensorLength = 0
                        _state = 1
                        self.processSensorData()

    def saveCodewizBoardSensorValue1(self):
        keys = ["mic", "light", "hallSensor"]
        for i in range(len(keys)):
            _value = (self.sensorRawBuf[2 + 2 * i] << 8) | self.sensorRawBuf[3 + 2 * i]
            if keys[i] == "hallSensor":
                _value -= 300
            self.sensorData[keys[i]] = _value

    def saveCodewizBoardSensorValue2(self):
        keys = [
            "distance",
            "touchPin_1", "touchPin_2", "touchPin_3",
            "touchPin_4", "touchPin_5", "touchPin_6",
            "button_right", "button_left",
            "gyroX", "gyroY", "gyroZ",
            "tempSensor",
        ]

        # distance
        _value = (self.sensorRawBuf[2] << 8) | self.sensorRawBuf[3]
        if _value < 3000:
            self.sensorData[keys[0]] = _value

        # enables
        for i in range(1, 1 + 8):
            _value = (self.sensorRawBuf[4] >> (i - 1)) & 1
            self.sensorData[keys[i]] = False if _value == 0 else True
            # if _value==0:
            #     self.sensorData[keys[i]] = False
            # else:
            #     self.sensorData[keys[i]] = True

        # gyro
        for i in range(9, 9 + 3):
            _value = self.sensorRawBuf[i - 4]
            if _value <= 180:
                self.sensorData[keys[i]] = _value - 90

        # tempSensor
        _value = (self.sensorRawBuf[8] << 8) | self.sensorRawBuf[9]
        _value -= 400
        _value /= 10
        if _value < 81:
            self.sensorData[keys[12]] = _value

    def end(self):
        self._write(Common.resetMessage())
        time.sleep(0.33)
        self.readThreadHandler()
        self.ser.close()

    def runDefaultSensor(self):
        self.write(Common.sensorStart())

