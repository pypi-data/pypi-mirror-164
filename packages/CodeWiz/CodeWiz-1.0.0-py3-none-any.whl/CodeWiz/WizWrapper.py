
class Common:
    RUN_TYPE=0
    READ_TYPE=1

    @staticmethod
    def addHeader(data):
        return [254, 255, len(data)+1]+data

    @staticmethod
    def transWizAscii(data):
        if str(type(data))!= "<class 'str'>":
            data=str(data)
        tmp = [ord(c) for c in data]
        return [len(tmp)]+tmp

    @staticmethod
    def resetMessage():
        return [254, 255, 4, 1, 3, 1]

    @staticmethod
    def sensorStart():
        return [254, 255, 3, 1, 2]


class RgbData:
    @staticmethod
    # RgbData.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 3])

    @staticmethod
    # RgbData.setBrightness(60)
    def setBrightness(value: int):
        if 0<=value<=255:
            return Common.addHeader([Common.RUN_TYPE, 4]+Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: RgbData.setBrightness(value: int)")

    @staticmethod
    # RgbData.setColor(1, 255, 255, 255)
    def setColor(num: int, red: int, green: int, blue: int):
        if (0<=red<=255)and(0<=green<=255)and(0<=blue<=255):
            return Common.addHeader([Common.RUN_TYPE, 5]
                                    +Common.transWizAscii(num)
                                    +Common.transWizAscii(red)
                                    +Common.transWizAscii(green)
                                    +Common.transWizAscii(blue))
        else:
            raise RuntimeError("InvalidValue: RgbData.setColor(num: int, red: int, green: int, blue: int)")

    @staticmethod
    # RgbData.setColorAll(255, 255, 255)
    def setColorAll(red: int, green: int, blue: int):
        if (0<=red<=255)and(0<=green<=255)and(0<=blue<=255):
            return Common.addHeader([Common.RUN_TYPE, 41]
                                    +Common.transWizAscii(red)
                                    +Common.transWizAscii(green)
                                    +Common.transWizAscii(blue))
        else:
            raise RuntimeError("InvalidValue: RgbData.setColorAll(red: int, green: int, blue: int)")


class SpeakerData:
    value=['C', 'Cs', 'D', 'Eb', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'Bb', 'B']
    beatList=[2, 4, 8, 16, 32]

    @staticmethod
    # SpeakerData.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 12])

    @staticmethod
    # SpeakerData.play('B', 4, 4)
    def play(note: str, octave: int, beat: int):
        if note not in SpeakerData.value:
            raise RuntimeError("InvalidValue: SpeakerData.play(...) - note in ['C', 'Cs','D', 'Eb', 'E','F', 'Fs', 'G', 'Gs', 'A', 'Bb', 'B']")
        if octave not in range(1, 8):
            raise RuntimeError("InvalidValue: SpeakerData.play(...) - range(1, 8)")
        if beat not in SpeakerData.beatList:
            raise RuntimeError("InvalidValue: SpeakerData.play(...) - beat in [2, 4, 8, 16, 32]")
        return Common.addHeader([Common.RUN_TYPE, 13]
                                +Common.transWizAscii(SpeakerData.value.index(note))
                                +Common.transWizAscii(octave)+Common.transWizAscii(beat))

    @staticmethod
    # SpeakerData.off()
    def off():
        return Common.addHeader([Common.RUN_TYPE, 14])


class OledData:
    colorList=['Black', 'White']
    # dirList = ['left to right', 'right to left', 'right bottom to upper left', 'left bottom to upper right']
    dirList=['L2R', 'R2L', 'RB2LU', 'LB2RU']  # [왼쪽에서 오른쪽. 오른쪽에서 왼쪽, 오른쪽 아래에서 왼쪽 위, 왼쪽 아래에서 오른쪽 위]

    @staticmethod
    # OledData.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 8])

    @staticmethod
    # OledData.clear()
    def clear():
        return Common.addHeader([Common.RUN_TYPE, 11])

    @staticmethod
    # OledData.reverse(False)
    def reverse(value: bool):
        return Common.addHeader([Common.RUN_TYPE, 20]+Common.transWizAscii(1 if value else 0))

    @staticmethod
    # OledData.setFontSize(3)
    def setFontSize(value: int):
        if 1<=value<=9:
            return Common.addHeader([Common.RUN_TYPE, 15] + Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: setFontSize(value: int) - 1<=value<=9")

    @staticmethod
    # OledData.setCursor((0,0))
    def setCursor(point: tuple):
        if len(point)!=2:
            raise RuntimeError("InvalidValue: OledData.setCursor(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 10]
                                +Common.transWizAscii(point[0])+Common.transWizAscii(point[1]))

    @staticmethod
    # OledData.print("Hello")
    def print(msg: str):
        return Common.addHeader([Common.RUN_TYPE, 9] +Common.transWizAscii(msg))

    @staticmethod
    # OledData.overlap(False)
    def overlap(isOverlap: bool):
        return Common.addHeader([Common.RUN_TYPE, 16]+Common.transWizAscii(1 if isOverlap else 0))

    @staticmethod
    # OledData.scroll("RB2LU",0,0)
    def scroll(_dir: str, startLine: int, endLine: int):
        # dirList=['L2R', 'R2L', 'RB2LU', 'LB2RU']  # [왼쪽에서 오른쪽. 오른쪽에서 왼쪽, 오른쪽 아래에서 왼쪽 위, 왼쪽 아래에서 오른쪽 위]
        if _dir not in OledData.dirList:
            raise RuntimeError("InvalidValue: OledData.scroll(...) - _dir in ['L2R', 'R2L', 'RB2LU', 'LB2RU']")
        _range8=range(8)  # 0~7
        if (startLine not in _range8) or (endLine not in _range8):
            raise RuntimeError("InvalidValue: OledData.scroll(...) - line in range(8)")
        return Common.addHeader([Common.RUN_TYPE, 19]
                                +Common.transWizAscii(OledData.dirList.index(_dir))
                                +Common.transWizAscii(startLine)+Common.transWizAscii(endLine))

    @staticmethod
    # OledData.stopScroll()
    def stopScroll():
        return Common.addHeader([Common.RUN_TYPE, 25])

    @staticmethod
    # OledData.drawDot((0,0), "White")
    def drawDot(point: tuple, color: str):
        if color not in OledData.colorList:
            raise RuntimeError("InvalidValue: OledData.drawDot(...) - color in ['Black', 'White']")
        if len(point)!=2:
            raise RuntimeError("InvalidValue: OledData.drawDot(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 17]
                                +Common.transWizAscii(point[0])+Common.transWizAscii(point[1])
                                +Common.transWizAscii(OledData.colorList.index(color)))

    @staticmethod
    # OledData.drawLine((0, 0), (10, 10), "White")
    def drawLine(startPoint: tuple, endPoint: tuple, color: str):
        if color not in OledData.colorList:
            raise RuntimeError("InvalidValue: OledData.drawLine(...) - color in ['Black', 'White']")
        if (len(startPoint)!=2)or(len(endPoint)!=2):
            raise RuntimeError("InvalidValue: OledData.drawLine(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 18]
                                +Common.transWizAscii(startPoint[0])+Common.transWizAscii(startPoint[1])
                                +Common.transWizAscii(endPoint[0])+Common.transWizAscii(endPoint[1])
                                +Common.transWizAscii(OledData.colorList.index(color)))

    @staticmethod
    # OledData.drawRect((0,0), 2, 4, False, "White")
    def drawRect(point: tuple, width: int, height: int, fill: bool, color: str):
        if color not in OledData.colorList:
            raise RuntimeError("InvalidValue: OledData.drawRect(...) - color in ['Black', 'White']")
        if len(point)!=2:
            raise RuntimeError("InvalidValue: OledData.drawRect(...) - len(o) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 21]
                                +Common.transWizAscii(point[0])+Common.transWizAscii(point[1])
                                +Common.transWizAscii(width)+Common.transWizAscii(height)
                                +Common.transWizAscii(1 if fill else 0)+Common.transWizAscii(OledData.colorList.index(color)))

    @staticmethod
    # OledData.drawCircle((0,0), 1, False, "White")
    def drawCircle(o: tuple, rad: int, fill: bool, color: str):
        if color not in OledData.colorList:
            raise RuntimeError("InvalidValue: OledData.drawCircle(...) - color in ['Black', 'White']")
        if len(o)!=2:
            raise RuntimeError("InvalidValue: OledData.drawCircle(...) - len(o) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 22]
                                + Common.transWizAscii(o[0]) + Common.transWizAscii(o[1]) + Common.transWizAscii(rad)
                                + Common.transWizAscii(1 if fill else 0) + Common.transWizAscii(OledData.colorList.index(color)))

    @staticmethod
    # OledData.drawTriangle((0,0), (0,0), (0,0), False, "White")
    def drawTriangle(p1: tuple, p2: tuple, p3: tuple, fill: bool, color: str):
        if color not in OledData.colorList:
            raise RuntimeError("InvalidValue: OledData.drawTriangle(...) - color in ['Black', 'White']")
        if (len(p1)!=2)or(len(p2)!=2)or(len(p3)!=2):
            raise RuntimeError("InvalidValue: OledData.drawTriangle(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 23]
                                + Common.transWizAscii(p1[0]) + Common.transWizAscii(p1[1])
                                + Common.transWizAscii(p2[0]) + Common.transWizAscii(p2[1])
                                + Common.transWizAscii(p3[0]) + Common.transWizAscii(p3[1])
                                + Common.transWizAscii(1 if fill else 0) + Common.transWizAscii(OledData.colorList.index(color)))


class RadioMeshData:
    @staticmethod
    def init(groupName: str):
        # 254, 255, 13, 0, 104, 9, 71, 114, 111, 117, 112, 78, 97, 109, 101 : RadioMesh "GroupName" 생성/참여
        # RadioMeshData.init("GroupName")
        return Common.addHeader([Common.RUN_TYPE, 104] + Common.transWizAscii(groupName))

    @staticmethod
    def send(msg: str):
        # 254, 255, 11, 0, 105, 7, 77, 101, 115, 115, 97, 103, 101 : RadioMesh "Message" 보내기
        # RadioMeshData.send("Message")
        return Common.addHeader([Common.RUN_TYPE, 105]+ Common.transWizAscii(msg))

    @staticmethod
    # RadioMeshData.getReceivedMsg() -- writeAndWaitAck(...)와 사용할 것
    def getReceivedMsg():
        return Common.addHeader([Common.READ_TYPE, 102])

    @staticmethod
    # RadioMeshData.clearMsg()
    def clearMsg():
        return Common.addHeader([Common.RUN_TYPE, 106])


class ServoData:
    pinNumber = {15: 2, 27: 3, 18: 6, 19: 7}

    @staticmethod
    # ServoData.init("SCON"); ServoData.init("MCON", 18)
    def init(mode: str, pin=18):
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 100])
        elif mode == "MCON":
            if pin in ServoData.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 97] + Common.transWizAscii(ServoData.pinNumber[pin]))
            else:
                raise RuntimeError("InvalidValue: ServoData.init(...) - pin in [15, 27, 18, 19]")
        else:
            raise RuntimeError("InvalidValue: ServoData.init(...) - mode in ['SCON', 'MCON']")

    @staticmethod
    # ServoData.setAngle("SCON", 0); ServoData.setAngle("MCON", 0, 18)
    def setAngle(mode: str, value: int, pin=18):
        if (value<0)or(value>180):
            raise RuntimeError("InvalidValue: ServoData.setAngle(...) - 0<=value<=180")
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 99]+ Common.transWizAscii(value))
        elif mode == "MCON":
            if pin in ServoData.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 96] + Common.transWizAscii(ServoData.pinNumber[pin])+ Common.transWizAscii(value))
            else:
                raise RuntimeError("InvalidValue: ServoData.setAngle(...) - pin in [15, 27, 18, 19]")
        else:
            raise RuntimeError("InvalidValue: ServoData.setAngle(...) - mode in ['SCON', 'MCON']")

    @staticmethod
    # ServoData.setVelocity("SCON",100); ServoData.setVelocity("MCON", -100,18)
    def setVelocity(mode: str, value: int, pin=18):
        if (value<-100)or(value>100):
            raise RuntimeError("InvalidValue: ServoData.setVelocity(...) - -100<=value<=100")
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 92]+ Common.transWizAscii(value))
        elif mode == "MCON":
            if pin in ServoData.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 93] + Common.transWizAscii(ServoData.pinNumber[pin])+ Common.transWizAscii(value))
            else:
                raise RuntimeError("InvalidValue: ServoData.run(...) - pin in [15, 27, 18, 19]")
        else:
            raise RuntimeError("InvalidValue: ServoData.run(...) - mode in ['SCON', 'MCON']")


class WaterPumpData:
    motorNum = ["MOTOR_L", "MOTOR_R"]

    @staticmethod
    # WaterPumpData.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 89])

    @staticmethod
    # WaterPumpData.run("MOTOR_L", 1023)
    def run(motor: str, value: int):
        if (value<0)or(value>1023):
            raise RuntimeError("InvalidValue: WaterPumpData.run(...) - -0<=value<=1023")
        if motor in WaterPumpData.motorNum:
            motor=WaterPumpData.motorNum.index(motor)
            return Common.addHeader([Common.RUN_TYPE, 52] + Common.transWizAscii(motor)+ Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: WaterPumpData.run(motor: str, value: int) - motor in ['MOTOR_L', 'MOTOR_R']")


class PropellerData:
    pinNumber = [27, 18, 19]

    @staticmethod
    # PropellerData.init(18)
    def init(pin: int):
        if pin in PropellerData.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 53]+ Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: PropellerData.init(pin: int) - pin in [27, 18, 19]")

    @staticmethod
    # PropellerData.run(18, 1023)
    def run(pin: int, value: int):
        if (value<0)or(value>1023):
            raise RuntimeError("InvalidValue: PropellerData.run(...) - -0<=value<=1023")
        if pin in PropellerData.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 54]+ Common.transWizAscii(pin)+ Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: PropellerData.run(pin: int, value: int) - pin in [27, 18, 19]")


class VibratorData:
    pinNumber = [13, 14, 15, 27, 18, 19]

    @staticmethod
    # VibratorData.init(18)
    def init(pin: int):
        if pin in VibratorData.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 50]+ Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: VibratorData.init(pin: int) - pin in [13, 14, 15, 27, 18, 19]")

    @staticmethod
    # VibratorData.run(True) - True면 1보냈고 그 외에는 전부 0보냄
    def run(value: bool):
        return Common.addHeader([Common.RUN_TYPE, 51] + Common.transWizAscii(1 if value else 0))


class DcMotorData:
    motorNum = ["MOTOR_L", "MOTOR_R"]

    @staticmethod
    # DcMotorData.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 89])

    @staticmethod
    # DcMotorData.run("MOTOR_L", False, 1023) # 2번인자 True면 시계방향 아니면 반시계방향
    def run(motor: str, _dir: bool, value: int):
        if motor in DcMotorData.motorNum:
            return Common.addHeader([Common.RUN_TYPE, 52]
                                    +Common.transWizAscii(DcMotorData.motorNum.index(motor))
                                    +Common.transWizAscii(0 if _dir else 1)
                                    +Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: DcMotorData.run(...) - motor in ['MOTOR_L', 'MOTOR_R']")


class DotMatrixData:
    pinNumber = [15, 27, 18, 19]
    isRow = ["COL", "ROW"]

    @staticmethod
    # DotMatrixData.init(1, 18, 19, 15)
    def init(count: int, din: int, cs: int, clk: int):
        def _isCorrectInputData() -> bool:
            tmp = set()
            tmp.add(din)
            tmp.add(cs)
            tmp.add(clk)
            if (1<=count<= 8) \
                    and (len(tmp)==3) \
                    and (din in DotMatrixData.pinNumber) \
                    and (cs in DotMatrixData.pinNumber) \
                    and (clk in DotMatrixData.pinNumber):
                return True
            else:
                return False
        if _isCorrectInputData():
            return Common.addHeader([Common.RUN_TYPE, 56]
                                    +Common.transWizAscii(count)
                                    +Common.transWizAscii(din)
                                    +Common.transWizAscii(cs)
                                    +Common.transWizAscii(clk))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.init(count: int, din: int, cs: int, clk: int)")

    @staticmethod
    # DotMatrixData.printStr(1, "Hello")
    def printStr(num: int, msg: str):
        if 1<=num<=8:
            return Common.addHeader([Common.RUN_TYPE, 57]
                                    +Common.transWizAscii(num-1)
                                    +Common.transWizAscii(msg))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.printStr(num: int, msg: str)")

    @staticmethod
    # DotMatrixData.clearMatrix(1)
    def clearMatrix(num: int):
        if 1<=num<=8:
            return Common.addHeader([Common.RUN_TYPE, 58] +Common.transWizAscii(num-1))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.clearMatrix(num: int)")

    @staticmethod
    # DotMatrixData.clearMatrixAll()
    def clearMatrixAll():
        return Common.addHeader([Common.RUN_TYPE, 59])

    @staticmethod
    # DotMatrixData.setLine(1, "COL", 2, "11111111")
    def setLine(num: int, isRow: str, lineNum: int, data: str):
        if (1<=num<=8)and(1<=lineNum<=8) and(isRow in DotMatrixData.isRow):
            if (len(data)==8)and(data.count('1')+data.count('0')==8):
                return Common.addHeader([Common.RUN_TYPE, 60]
                                        +Common.transWizAscii(num-1)
                                        +Common.transWizAscii(DotMatrixData.isRow.index(isRow))
                                        +Common.transWizAscii(lineNum-1)
                                        +Common.transWizAscii(data))
            else:
                raise RuntimeError("InvalidValue: DotMatrixData.setLine(...) - (len(data)==8)and(data.count('1')+data.count('0')==8)")
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.setLine(...) - (1<=num<=8)and(1<=lineNum<=8)and(isRow in ['COL', 'ROW'])")

    @staticmethod
    # DotMatrixData.setDot(1, 2, 2, True)
    def setDot(num: int, row: int, col: int, isHigh: bool):
        if (1<=num<=8)and(1<=row<=8)and(1<=col<=8):
            return Common.addHeader([Common.RUN_TYPE, 61]
                                    +Common.transWizAscii(num-1)
                                    +Common.transWizAscii(row-1)
                                    +Common.transWizAscii(col-1)
                                    +Common.transWizAscii(1 if isHigh else 0))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.setDot(num: int, row: int, col: int, isHigh: bool)")

    @staticmethod
    # DotMatrixData.setBrightness(1, 8)
    def setBrightness(num: int, brightness: int):
        if (1<=num<=8)and(1<=brightness<=15):
            return Common.addHeader([Common.RUN_TYPE, 62]
                                    +Common.transWizAscii(num-1)
                                    +Common.transWizAscii(brightness))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.setBrightness(num: int, brightness: int)")

    @staticmethod
    # DotMatrixData.setLimit(1, 8)
    def setLimit(num: int, limit: int):
        if (1<=num<=8)and(1<=limit<=8):
            return Common.addHeader([Common.RUN_TYPE, 63]
                                    +Common.transWizAscii(num-1)
                                    +Common.transWizAscii(limit-1))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.setLimit(num: int, limit: int)")

    @staticmethod
    # DotMatrixData.setShutdown(1, False)
    def setShutdown(num: int, isShutdown: bool):
        if 1<=num<=8:
            return Common.addHeader([Common.RUN_TYPE, 64]
                                    +Common.transWizAscii(num-1)
                                    +Common.transWizAscii(1 if isShutdown else 0))
        else:
            raise RuntimeError("InvalidValue: DotMatrixData.setShutdown(num: int, isActive: bool)")


class NeoPixelData:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # NeoPixelData.init(18, 16)
    def init(pin: int, count: int):
        if pin in NeoPixelData.pinList:
            return Common.addHeader([Common.RUN_TYPE, 42]
                                    +Common.transWizAscii(pin)
                                    +Common.transWizAscii(count))
        else:
            raise RuntimeError("InvalidValue: NeoPixelData.init(pin: int, count: int)")

    @staticmethod
    # NeoPixelData.setBrightness(255)
    def setBrightness(value: int):
        if 0<=value<=255:
            return Common.addHeader([Common.RUN_TYPE, 43] +Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: NeoPixelData.setBrightness(value: int)")

    @staticmethod
    # NeoPixelData.setColor(1, 255, 255, 255)
    def setColor(num: int, red: int, green: int, blue: int):
        if (0<=red<=255)and(0<=green<=255)and(0<=blue<=255):
            return Common.addHeader([Common.RUN_TYPE, 44]
                                    +Common.transWizAscii(num)
                                    +Common.transWizAscii(red)
                                    +Common.transWizAscii(green)
                                    +Common.transWizAscii(blue))
        else:
            raise RuntimeError("InvalidValue: NeoPixelData.setColor(num: int, red: int, green: int, blue: int)")

    @staticmethod
    # NeoPixelData.setColorAll(255, 255, 255)
    def setColorAll(red: int, green: int, blue: int):
        if (0<=red<=255)and(0<=green<=255)and(0<=blue<=255):
            return Common.addHeader([Common.RUN_TYPE, 46]
                                    +Common.transWizAscii(red)
                                    +Common.transWizAscii(green)
                                    +Common.transWizAscii(blue))
        else:
            raise RuntimeError("InvalidValue: NeoPixelData.setColorAll(red: int, green: int, blue: int)")


class LaserData:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # LaserData.init(18)
    def init(pin: int):
        if pin in LaserData.pinList:
            return Common.addHeader([Common.RUN_TYPE, 48]
                                    +Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: LaserData.init(pin: int)")

    @staticmethod
    # LaserData.run(True)
    def run(isOn: bool):
        return Common.addHeader([Common.RUN_TYPE, 49]
                                +Common.transWizAscii(1 if isOn else 0))


class MeshData:
    @staticmethod
    # MeshData.init("GroupName")
    def init(groupName: str):
        return Common.addHeader([Common.RUN_TYPE, 101] + Common.transWizAscii(groupName))

    @staticmethod
    # MeshData.send("Message")
    def send(Message: str):
        return Common.addHeader([Common.RUN_TYPE, 102] + Common.transWizAscii(Message))

    @staticmethod
    # MeshData.isReceived("Message") -- writeAndWaitAck(...)와 사용할 것
    def isReceived(Message: str):
        return Common.addHeader([Common.READ_TYPE, 97] +Common.transWizAscii(Message))

    @staticmethod
    # MeshData.getReceivedMsg() -- writeAndWaitAck(...)와 사용할 것
    def getReceivedMsg():
        return Common.addHeader([Common.READ_TYPE, 95])

    @staticmethod
    # MeshData.isConnected() -- writeAndWaitAck(...)와 사용할 것
    def isConnected():
        return Common.addHeader([Common.READ_TYPE, 99])

    @staticmethod
    # MeshData.clearMsg()
    def clearMsg():
        return Common.addHeader([Common.RUN_TYPE, 103])


class InfraredThermometerData:
    _type=["SCON", "MCON"]
    _unit=["C", "F"]

    @staticmethod
    # InfraredThermometerData.read("SCON", "C") -- writeAndWaitAck(...)와 사용할 것
    def read(_type: str, unit: str):
        if (_type in InfraredThermometerData._type)and(unit in InfraredThermometerData._unit):
            return Common.addHeader([Common.READ_TYPE, 100+InfraredThermometerData._type.index(_type)]
                                    +Common.transWizAscii(InfraredThermometerData._unit.index(unit)))
        else:
            raise RuntimeError("InvalidValue: InfraredThermometerData.read(_type: str, unit: str)")


class DHT:  # Digital Humidity Temperature
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]
    _unit=['C', 'F']

    @staticmethod
    # DHT.init(18)
    def init(pin: int):
        if pin in DHT.pinList:
            return Common.addHeader([Common.RUN_TYPE, 83]
                                    +Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: DHT.init(pin: int)")

    @staticmethod
    # DHT.isConnected() -- writeAndWaitAck(...)와 사용할 것
    def isConnected():
        return Common.addHeader([Common.READ_TYPE, 91])

    @staticmethod
    # DHT.readHumidity() -- writeAndWaitAck(...)와 사용할 것
    def readHumidity():
        return Common.addHeader([Common.READ_TYPE, 90])

    @staticmethod
    # DHT.readTemperature("C") -- writeAndWaitAck(...)와 사용할 것
    def readTemperature(unit: str):
        if unit in DHT._unit:
            return Common.addHeader([Common.READ_TYPE, 89]
                                    +Common.transWizAscii(DHT._unit.index(unit)))
        else:
            raise RuntimeError("InvalidValue: DHT.readTemperature(unit: str) - unit in ['C', 'F']")


class HuskyLens:
    algorithmList=['FaceRecognition', 'ObjectTracking', 'ObjectRecognition',
                   'LineTracking', 'ColorRecognition', 'TagRecognition',
                   'ObjectClassification']
    _type={'BOX': 42, 'ARROW': 43}
    arrowInfoType=['startX', 'startY', 'endX', 'endY']
    boxInfoType=['id', 'centerX', 'centerY', 'width', 'height']

    @staticmethod
    # HuskyLens.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 65])

    @staticmethod
    # HuskyLens.setMode("ObjectRecognition")
    def setMode(algorithm: str):
        if algorithm in HuskyLens.algorithmList:
            return Common.addHeader([Common.RUN_TYPE, 66]
                                    +Common.transWizAscii(HuskyLens.algorithmList.index(algorithm)))
        else:
            raise RuntimeError("InvalidValue: HuskyLens.setMode(algorithm: str) - algorithm in ['FaceRecognition', 'ObjectTracking', 'ObjectRecognition', 'LineTracking', 'ColorRecognition', 'TagRecognition', 'ObjectClassification']")

    @staticmethod
    # HuskyLens.update()
    def update():
        return Common.addHeader([Common.RUN_TYPE, 67])

    @staticmethod
    # HuskyLens.isLearned(1) -- writeAndWaitAck(...)와 사용할 것
    def isLearned(_id: int):
        return Common.addHeader([Common.READ_TYPE, 79]+Common.transWizAscii(_id))

    @staticmethod
    # HuskyLens.isDetected(1, "ARROW") -- writeAndWaitAck(...)와 사용할 것
    def isDetected(_id: int, _type: str):
        if _type not in HuskyLens._type:
            raise RuntimeError("InvalidValue: HuskyLens.isDetected(_id: int, _type: str) - _type in ['BOX', 'ARROW']")
        return Common.addHeader([Common.READ_TYPE, 84]+Common.transWizAscii(HuskyLens._type[_type])+Common.transWizAscii(_id))

    @staticmethod
    # HuskyLens.getCountLearned() -- writeAndWaitAck(...)와 사용할 것
    def getCountLearned():
        return Common.addHeader([Common.READ_TYPE, 83])

    @staticmethod
    # HuskyLens.isDetectedType("ARROW") -- writeAndWaitAck(...)와 사용할 것
    def isDetectedType(_type: str):
        if _type not in HuskyLens._type:
            raise RuntimeError("InvalidValue: HuskyLens.isDetectedType(_type: str) - _type in ['BOX', 'ARROW']")
        return Common.addHeader([Common.READ_TYPE, 82]+Common.transWizAscii(HuskyLens._type[_type]))

    @staticmethod
    # HuskyLens.getArrowInfo("startX") -- writeAndWaitAck(...)와 사용할 것
    def getArrowInfo(infoType: str):
        if infoType not in HuskyLens.arrowInfoType:
            raise RuntimeError("InvalidValue: HuskyLens.getArrowInfo(infoType: str) - infoType in ['startX', 'startY', 'endX', 'endY']")
        return Common.addHeader([Common.READ_TYPE, 81]+Common.transWizAscii(HuskyLens.arrowInfoType.index(infoType)))

    @staticmethod
    # HuskyLens.getBoxInfo("id") -- writeAndWaitAck(...)와 사용할 것
    def getBoxInfo(infoType: str):
        if infoType not in HuskyLens.boxInfoType:
            raise RuntimeError("InvalidValue: HuskyLens.getBoxInfo(infoType: str) - infoType in ['id', 'centerX', 'centerY', 'width', 'height']")
        return Common.addHeader([Common.READ_TYPE, 80]+Common.transWizAscii(HuskyLens.arrowInfoType.index(infoType)))

    @staticmethod
    # HuskyLens.drawText((0,0), "Codewiz")
    def drawText(point: tuple, text: str):
        if len(point)!=2:
            raise RuntimeError("InvalidValue: HuskyLens.drawText(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 68]
                                +Common.transWizAscii(point[0])+Common.transWizAscii(point[1])
                                +Common.transWizAscii(text))

    @staticmethod
    # HuskyLens.clearText()
    def clearText():
        return Common.addHeader([Common.RUN_TYPE, 69])


class Button:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # Button.read(13) -- writeAndWaitAck(...)와 사용할 것
    def read(pin: int):
        if pin in Button.pinList:
            return Common.addHeader([Common.READ_TYPE, 21]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Button.read(pin: int) - pin in [13, 14, 15, 27, 32, 33, 18, 19]")


class PhotoInterrupter:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # PhotoInterrupter.read(18) -- writeAndWaitAck(...)와 사용할 것
    def read(pin: int):
        if pin in PhotoInterrupter.pinList:
            return Common.addHeader([Common.READ_TYPE, 96]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: PhotoInterrupter.read(pin: int) - pin in [13, 14, 15, 27, 32, 33, 18, 19]")


class SoilAndWater:
    pinList=[32, 33, 36, 39]

    @staticmethod
    # SoilAndWater.read(36) -- writeAndWaitAck(...)와 사용할 것
    def read(pin: int):
        if pin in SoilAndWater.pinList:
            return Common.addHeader([Common.READ_TYPE, 87]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: SoilAndWater.read(pin: int) - pin in [32, 33, 36, 39]")


class Potentiometer:
    pinList=[32, 33, 36, 39]

    @staticmethod
    # Potentiometer.read(36) -- writeAndWaitAck(...)와 사용할 것
    def read(pin: int):
        if pin in Potentiometer.pinList:
            return Common.addHeader([Common.READ_TYPE, 88]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Potentiometer.read(pin: int) - pin in [32, 33, 36, 39]")


class ColorSensor:
    colorList=['Red', 'Green', 'Blue', 'White', 'Black']

    @staticmethod
    # ColorSensor.isColor("Red") -- writeAndWaitAck(...)와 사용할 것
    def isColor(color: str):
        if color in ColorSensor.colorList:
            return Common.addHeader([Common.READ_TYPE, 92]+Common.transWizAscii(ColorSensor.colorList.index(color)))
        else:
            raise RuntimeError("InvalidValue: ColorSensor.isColor(color: str) - color in ['Red', 'Green', 'Blue', 'White', 'Black']")

    @staticmethod
    # ColorSensor.getColorValue("Red") -- writeAndWaitAck(...)와 사용할 것
    def getColorValue(color: str):
        if color in ColorSensor.colorList:
            return Common.addHeader([Common.READ_TYPE, 93]+Common.transWizAscii(ColorSensor.colorList[:3].index(color)))
        else:
            raise RuntimeError("InvalidValue: ColorSensor.isColor(color: str) - color in ['Red', 'Green', 'Blue']")


class Joystick:
    stickPinList=[32, 33, 36, 39]
    btnPinList=[-1, 13, 14, 15, 27, 18, 19]
    dirList=['X', 'Y']

    @staticmethod
    # Joystick.init(12, 36, 39, 15)  # 범위12 x축36 y축39 버튼15
    # Joystick.init(12, 36, 39)  # 범위12 x축36 y축39 버튼없음
    def init(_range: int, x: int, y: int, btn=-1):
        if (x not in Joystick.stickPinList)or(y not in Joystick.stickPinList):
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - x, y in [32, 33, 36, 39]")
        if x==y:
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - x!=y ")
        if btn not in Joystick.btnPinList:
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - btn in [-1, 13, 14, 15, 27, 18, 19]")
        return Common.addHeader([Common.RUN_TYPE, 55]
                                +Common.transWizAscii(x)
                                +Common.transWizAscii(y)
                                +Common.transWizAscii(btn)
                                +Common.transWizAscii(_range))

    @staticmethod
    # Joystick.readStick("X") -- writeAndWaitAck(...)와 사용할 것
    def readStick(_dir: str):
        if _dir in Joystick.dirList:
            return Common.addHeader([Common.READ_TYPE, 86]+Common.transWizAscii(Joystick.dirList.index(_dir)))
        else:
            raise RuntimeError("InvalidValue: Joystick.readStick(_dir: str) - _dir in ['X', 'Y']")

    @staticmethod
    # Joystick.readButton() -- writeAndWaitAck(...)와 사용할 것
    def readButton():
        return Common.addHeader([Common.READ_TYPE, 85])

