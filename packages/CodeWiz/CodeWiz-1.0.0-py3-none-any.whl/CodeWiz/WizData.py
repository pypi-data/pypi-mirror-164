import warnings


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


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
        tmp=[]
        for c in data:
            tmp+=Common.msgFormatting(c)
        # tmp = [ord(c) for c in data]
        return [len(tmp)]+tmp

    @staticmethod
    def msgFormatting(c):
        c=ord(c)
        if c>0xff:
            return [0x08, c>>8, c&0xff]
        else:
            return [c]

    @staticmethod
    def resetMessage():
        return [254, 255, 4, 1, 3, 1]

    @staticmethod
    def sensorStart():
        return [254, 255, 3, 1, 2]

    @staticmethod
    def firmVersion():
        return [254, 255, 3, 1, 4]


class NeoPixel:
    @staticmethod
    # NeoPixel.init()
    def init(pin=23, count=5):
        return Common.addHeader([Common.RUN_TYPE, 42]+Common.transWizAscii(int(pin))+Common.transWizAscii(int(count)))

    @staticmethod
    # NeoPixel.setBrightness(60)
    def setBrightness(value: int):
        if value not in range(0,0xff+1):
            warnings.warn("[Warning/NeoPixel.setBrightness(value: int)]: value in range(0, 256)")
        return Common.addHeader([Common.RUN_TYPE, 43]+Common.transWizAscii(int(constrain(value, 0, 255))))

    @staticmethod
    # NeoPixel.setColor(1, 255, 255, 255)
    def setColor(num: int, red: int, green: int, blue: int):
        if (red not in range(0,0xff+1))or(green not in range(0,0xff+1))or(blue not in range(0,0xff+1)):
            warnings.warn("[Warning/NeoPixel.setColor(num: int, red: int, green: int, blue: int)]: color in range(0, 256)")
        return Common.addHeader([Common.RUN_TYPE, 44]
                                +Common.transWizAscii(int(num))
                                +Common.transWizAscii(int(constrain(red, 0, 255)))
                                +Common.transWizAscii(int(constrain(green, 0, 255)))
                                +Common.transWizAscii(int(constrain(blue, 0, 255))))

    @staticmethod
    # NeoPixel.setColorAll(255, 255, 255)
    def setColorAll(red: int, green: int, blue: int):
        if (red not in range(0,0xff+1))or(green not in range(0,0xff+1))or(blue not in range(0,0xff+1)):
            warnings.warn("[Warning/NeoPixel.setColorAll(red: int, green: int, blue: int)]: color in range(0, 256)")
        return Common.addHeader([Common.RUN_TYPE, 46]
                                +Common.transWizAscii(int(constrain(red, 0, 255)))
                                +Common.transWizAscii(int(constrain(green, 0, 255)))
                                +Common.transWizAscii(int(constrain(blue, 0, 255))))

    @staticmethod
    # NeoPixel.clear()
    def clear():
        return Common.addHeader([Common.RUN_TYPE, 47])

    @staticmethod
    # NeoPixel.fillRandomColor()
    def fillRandomColor():
        return Common.addHeader([Common.RUN_TYPE, 4])

    @staticmethod
    # NeoPixel.setRandomColor(1)
    def setRandomColor(num: int):
        return Common.addHeader([Common.RUN_TYPE, 6]+Common.transWizAscii(int(num)))

    @staticmethod
    # NeoPixel.rotate(True)
    def rotate(isForward: bool):
        return Common.addHeader([Common.RUN_TYPE, 5]+Common.transWizAscii(1 if isForward else 0))

    @staticmethod
    # NeoPixel.shift(True)
    def shift(isForward: bool):
        return Common.addHeader([Common.RUN_TYPE, 7]+Common.transWizAscii(1 if isForward else 0))

    @staticmethod
    # NeoPixel.gradationRGB(1, 5, '#ff0000', '#00ff00') # format(123, "x") - 숫자 16진수 문자로 변환
    def gradationRGB(_start: int, _end: int, sColor: str, eColor: str):
        return Common.addHeader([Common.RUN_TYPE, 29]
                                +Common.transWizAscii(int(_start))
                                +Common.transWizAscii(int(_end))
                                +Common.transWizAscii(sColor)
                                +Common.transWizAscii(eColor))

    @staticmethod
    # NeoPixel.gradationHSL(1, 5, '#ff0000', '#00ff00') # format(123, "x") - 숫자 16진수 문자로 변환
    def gradationHSL(_start: int, _end: int, sColor: str, eColor: str):
        return Common.addHeader([Common.RUN_TYPE, 30]
                                +Common.transWizAscii(int(_start))
                                +Common.transWizAscii(int(_end))
                                +Common.transWizAscii(sColor)
                                +Common.transWizAscii(eColor))

    @staticmethod
    # NeoPixel.wheel()
    def wheel():
        return Common.addHeader([Common.RUN_TYPE, 31])


class Speaker:
    value=['C', 'Cs', 'D', 'Eb', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'Bb', 'B']
    octave = list(range(1, 8))
    beatList=[2, 4, 8, 16, 32]

    @staticmethod
    # Speaker.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 12])

    @staticmethod
    # Speaker.play('B', 4, 4)
    def play(note: str, octave: int, beat: int):
        if note not in Speaker.value:
            raise RuntimeError("InvalidValue: Speaker.play(note, 4, 4) - note in "+str(Speaker.value))
        if octave not in Speaker.octave:
            raise RuntimeError("InvalidValue: Speaker.play('B', octave, 4) - octave in "+str(Speaker.octave))
        if beat not in Speaker.beatList:
            raise RuntimeError("InvalidValue: Speaker.play('B', 4, beat) - beat in "+str(Speaker.beatList))
        return Common.addHeader([Common.RUN_TYPE, 13]
                                +Common.transWizAscii(Speaker.value.index(note))
                                +Common.transWizAscii(octave)+Common.transWizAscii(beat))

    @staticmethod
    # Speaker.off()
    def off():
        return Common.addHeader([Common.RUN_TYPE, 14])


class Oled:
    colorList=['Black', 'White']
    dirList = ['left to right', 'right to left', 'right bottom to upper left', 'left bottom to upper right']
    # dirList=['L2R', 'R2L', 'RB2LU', 'LB2RU']  # [왼쪽에서 오른쪽. 오른쪽에서 왼쪽, 오른쪽 아래에서 왼쪽 위, 왼쪽 아래에서 오른쪽 위]

    @staticmethod
    # Oled.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 8])

    @staticmethod
    # Oled.clear()
    def clear():
        return Common.addHeader([Common.RUN_TYPE, 11])

    @staticmethod
    # Oled.reverse(False)
    def reverseMode(value: bool):
        return Common.addHeader([Common.RUN_TYPE, 20]+Common.transWizAscii(1 if value else 0))

    @staticmethod
    # Oled.setFontSize(3)
    def setFontSize(value: int):
        if value not in range(1, 10):
            warnings.warn("[Warning/Oled.setFontSize(value: int)]: value not in range(1, 10)")
        return Common.addHeader([Common.RUN_TYPE, 15] + Common.transWizAscii(int(constrain(value, 1, 10))))

    @staticmethod
    # Oled.setCursor((0,0))
    def setCursor(point: tuple):
        if len(point)!=2:
            raise RuntimeError("InvalidValue: Oled.setCursor(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 10]
                                +Common.transWizAscii(point[0])+Common.transWizAscii(point[1]))

    @staticmethod
    # Oled.print("Hello")
    def print(msg: str):
        return Common.addHeader([Common.RUN_TYPE, 9] +Common.transWizAscii(msg))

    @staticmethod
    # Oled.printHanguel("빛:", False)
    def printHangul(msg: str, isLineBreak: bool):
        return Common.addHeader([Common.RUN_TYPE, 82] +Common.transWizAscii(msg) + Common.transWizAscii(1 if isLineBreak else 0))

    @staticmethod
    # Oled.overlap(False)
    def lineBreakMode(isOverlap: bool):
        return Common.addHeader([Common.RUN_TYPE, 16]+Common.transWizAscii(1 if isOverlap else 0))

    @staticmethod
    # Oled.scroll("RB2LU",0,0)
    def scroll(_dir: str, startLine: int, endLine: int):
        # dirList = ['left to right', 'right to left', 'right bottom to upper left', 'left bottom to upper right']
        if _dir not in Oled.dirList:
            raise RuntimeError("InvalidValue: OledData.scroll(...) - _dir in "+str(Oled.dirList))
        _range8=range(8)  # 0~7
        if (startLine not in _range8) or (endLine not in _range8):
            raise RuntimeError("InvalidValue: OledData.scroll(...) - line in range(8)")
        return Common.addHeader([Common.RUN_TYPE, 19]
                                +Common.transWizAscii(Oled.dirList.index(_dir))
                                +Common.transWizAscii(startLine)+Common.transWizAscii(endLine))

    @staticmethod
    # Oled.stopScroll()
    def stopScroll():
        return Common.addHeader([Common.RUN_TYPE, 25])

    @staticmethod
    # Oled.drawDot((0,0), "White")
    def drawDot(point: tuple, color: str):
        if color not in Oled.colorList:
            raise RuntimeError("InvalidValue: OledData.drawDot(...) - color in "+str(Oled.colorList))
        if len(point)!=2:
            raise RuntimeError("InvalidValue: OledData.drawDot(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 17]
                                +Common.transWizAscii(int(point[0]))+Common.transWizAscii(int(point[1]))
                                +Common.transWizAscii(Oled.colorList.index(color)))

    @staticmethod
    # Oled.drawLine((0, 0), (10, 10), "White")
    def drawLine(startPoint: tuple, endPoint: tuple, color: str):
        if color not in Oled.colorList:
            raise RuntimeError("InvalidValue: OledData.drawLine(...) - color in "+str(Oled.colorList))
        if (len(startPoint)!=2)or(len(endPoint)!=2):
            raise RuntimeError("InvalidValue: OledData.drawLine(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 18]
                                +Common.transWizAscii(int(startPoint[0]))+Common.transWizAscii(int(startPoint[1]))
                                +Common.transWizAscii(int(endPoint[0]))+Common.transWizAscii(int(endPoint[1]))
                                +Common.transWizAscii(Oled.colorList.index(color)))

    @staticmethod
    # Oled.drawRect((0,0), 2, 4, False, "White")
    def drawRect(point: tuple, width: int, height: int, fill: bool, color: str):
        if color not in Oled.colorList:
            raise RuntimeError("InvalidValue: Oled.drawRect(...) - color in "+str(Oled.colorList))
        if len(point)!=2:
            raise RuntimeError("InvalidValue: Oled.drawRect(...) - len(o) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 21]
                                +Common.transWizAscii(int(point[0]))+Common.transWizAscii(int(point[1]))
                                +Common.transWizAscii(int(width))+Common.transWizAscii(int(height))
                                +Common.transWizAscii(1 if fill else 0)+Common.transWizAscii(Oled.colorList.index(color)))

    @staticmethod
    # Oled.drawCircle((0,0), 1, False, "White")
    def drawCircle(o: tuple, rad: int, fill: bool, color: str):
        if color not in Oled.colorList:
            raise RuntimeError("InvalidValue: Oled.drawCircle(...) - color in "+str(Oled.colorList))
        if len(o)!=2:
            raise RuntimeError("InvalidValue: Oled.drawCircle(...) - len(o) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 22]
                                + Common.transWizAscii(int(o[0])) + Common.transWizAscii(int(o[1])) + Common.transWizAscii(int(rad))
                                + Common.transWizAscii(1 if fill else 0) + Common.transWizAscii(Oled.colorList.index(color)))

    @staticmethod
    # Oled.drawTriangle((0,0), (0,0), (0,0), False, "White")
    def drawTriangle(p1: tuple, p2: tuple, p3: tuple, fill: bool, color: str):
        if color not in Oled.colorList:
            raise RuntimeError("InvalidValue: Oled.drawTriangle(...) - color in "+str(Oled.colorList))
        if (len(p1)!=2)or(len(p2)!=2)or(len(p3)!=2):
            raise RuntimeError("InvalidValue: Oled.drawTriangle(...) - len(point) must be 2")
        return Common.addHeader([Common.RUN_TYPE, 23]
                                + Common.transWizAscii(int(p1[0])) + Common.transWizAscii(int(p1[1]))
                                + Common.transWizAscii(int(p2[0])) + Common.transWizAscii(int(p2[1]))
                                + Common.transWizAscii(int(p3[0])) + Common.transWizAscii(int(p3[1]))
                                + Common.transWizAscii(1 if fill else 0) + Common.transWizAscii(Oled.colorList.index(color)))


class RadioMesh:
    @staticmethod
    def init(groupName: str):
        # RadioMesh.init("GroupName")
        return Common.addHeader([Common.RUN_TYPE, 104] + Common.transWizAscii(groupName))

    @staticmethod
    def send(msg: str):
        # RadioMesh.send("Message")
        return Common.addHeader([Common.RUN_TYPE, 105]+ Common.transWizAscii(msg))

    @staticmethod
    # RadioMesh.getReceivedMsg() -- write(...)와 사용할 것
    def getReceivedMsg():
        return Common.addHeader([Common.READ_TYPE, 102])

    @staticmethod
    # RadioMesh.clearMsg()
    def clearMsg():
        return Common.addHeader([Common.RUN_TYPE, 106])


class Servo:
    pinNumber = {15: 2, 27: 3, 18: 6, 19: 7}
    mode = ["SCON", "MCON"]

    @staticmethod
    # Servo.init("SCON"); Servo.init("MCON", 18)
    def init(mode: str, pin=18):
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 100])
        elif mode == "MCON":
            if pin in Servo.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 97] + Common.transWizAscii(Servo.pinNumber[pin]))
            else:
                raise RuntimeError("InvalidValue: Servo.init(...) - pin in "+str([*Servo.pinNumber.keys()]))
        else:
            raise RuntimeError("InvalidValue: Servo.init(...) - mode in "+str(Servo.mode))

    @staticmethod
    # Servo.setAngle("SCON", 0); Servo.setAngle("MCON", 0, 18)
    def setAngle(mode: str, value: int, pin=18):
        if (value<0)or(value>180):
            warnings.warn("[Warning/Servo.setAngle(mode: str, value: int, pin=18)]: 0<=value<=180")
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 99]+ Common.transWizAscii(int(constrain(value,0,180))))
        elif mode == "MCON":
            if pin in Servo.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 96] + Common.transWizAscii(Servo.pinNumber[pin])+ Common.transWizAscii(int(constrain(value,0,180))))
            else:
                raise RuntimeError("InvalidValue: Servo.setAngle(...) - pin in "+str([*Servo.pinNumber.keys()]))
        else:
            raise RuntimeError("InvalidValue: Servo.setAngle(...) - mode in "+str(Servo.mode))

    @staticmethod
    # Servo.setVelocity("SCON",100); Servo.setVelocity("MCON", -100,18)
    def setVelocity(mode: str, value: int, pin=18):
        if (value<-100)or(value>100):
            warnings.warn("[Warning/Servo.setVelocity(mode: str, value: int, pin=18)]: -100<=value<=100")
        if mode=="SCON":
            return Common.addHeader([Common.RUN_TYPE, 92]+ Common.transWizAscii(int(constrain(value,-100,100))))
        elif mode == "MCON":
            if pin in Servo.pinNumber:
                return Common.addHeader([Common.RUN_TYPE, 93] + Common.transWizAscii(Servo.pinNumber[pin])+ Common.transWizAscii(int(constrain(value,-100,100))))
            else:
                raise RuntimeError("InvalidValue: Servo.run(...) - pin in "+str([*Servo.pinNumber.keys()]))
        else:
            raise RuntimeError("InvalidValue: Servo.run(...) - mode in"+str(Servo.mode))


class WaterPump:
    motorNum = ["MOTOR_L", "MOTOR_R"]

    @staticmethod
    # WaterPump.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 89])

    @staticmethod
    # WaterPump.run("MOTOR_L", 1023)
    def run(motor: str, value: int):
        if (value<0)or(value>1023):
            warnings.warn("[Warning/WaterPump.run(motor: str, value: int)]: 0<=value<=1023")
        if motor in WaterPump.motorNum:
            return Common.addHeader([Common.RUN_TYPE, 90]
                                    +Common.transWizAscii(WaterPump.motorNum.index(motor))
                                    +Common.transWizAscii(1)
                                    +Common.transWizAscii(int(constrain(value,0,1023))))
        else:
            raise RuntimeError("InvalidValue: WaterPump.run(motor: str, value: int) - motor in"+str(WaterPump.motorNum))


class Propeller:
    pinNumber = [27, 18, 19]

    @staticmethod
    # Propeller.init(18)
    def init(pin: int):
        if pin in Propeller.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 53]+ Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Propeller.init(pin: int) - pin in "+str(Propeller.pinNumber))

    @staticmethod
    # Propeller.run(18, 1023)
    def run(pin: int, value: int):
        if (value<0)or(value>1023):
            warnings.warn("[Warning/Propeller.run(pin: int, value: int)]: 0<=value<=1023")
        if pin in Propeller.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 54]+ Common.transWizAscii(pin)+ Common.transWizAscii(int(constrain(value,0,1023))))
        else:
            raise RuntimeError("InvalidValue: Propeller.run(pin: int, value: int) - pin in"+str(Propeller.pinNumber))


class Vibrator:
    pinNumber = [13, 14, 15, 27, 18, 19]

    @staticmethod
    # Vibrator.init(18)
    def init(pin: int):
        if pin in Vibrator.pinNumber:
            return Common.addHeader([Common.RUN_TYPE, 50]+ Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Vibrator.init(pin: int) - pin in"+str(Vibrator.pinNumber))

    @staticmethod
    # Vibrator.run(True) - True면 1보냈고 그 외에는 전부 0보냄
    def run(value: bool):
        return Common.addHeader([Common.RUN_TYPE, 51] + Common.transWizAscii(1 if value else 0))


class DcMotor:
    motorNum = ["MOTOR_L", "MOTOR_R"]

    @staticmethod
    # DcMotor.init()
    def init():
        return Common.addHeader([Common.RUN_TYPE, 89])

    @staticmethod
    # DcMotor.run("MOTOR_L", False, 1023) # 2번인자 True면 시계방향 아니면 반시계방향
    def run(motor: str, _dir: bool, value: int):
        if motor in DcMotor.motorNum:
            return Common.addHeader([Common.RUN_TYPE, 90]
                                    +Common.transWizAscii(DcMotor.motorNum.index(motor))
                                    +Common.transWizAscii(0 if _dir else 1)
                                    +Common.transWizAscii(value))
        else:
            raise RuntimeError("InvalidValue: DcMotor.run(...) - motor in"+str(DcMotor.motorNum))


class DotMatrix:
    pinNumber = [15, 27, 18, 19]
    isRow = ["COL", "ROW"]

    @staticmethod
    # DotMatrix.init(1, 18, 19, 15)
    def init(count: int, din: int, cs: int, clk: int):
        def _isCorrectInputData() -> bool:
            tmp = set()
            tmp.add(din)
            tmp.add(cs)
            tmp.add(clk)
            if (len(tmp)==3) \
                    and (din in DotMatrix.pinNumber) \
                    and (cs in DotMatrix.pinNumber) \
                    and (clk in DotMatrix.pinNumber):
                return True
            else:
                return False
        if _isCorrectInputData():
            if (count<1)or(count>8):
                warnings.warn("[Warning/DotMatrix.init(count: int, din: int, cs: int, clk: int)]: 1<=count<=8")
            return Common.addHeader([Common.RUN_TYPE, 56]
                                    +Common.transWizAscii(int(constrain(count,1,8)))
                                    +Common.transWizAscii(din)
                                    +Common.transWizAscii(cs)
                                    +Common.transWizAscii(clk))
        else:
            raise RuntimeError("InvalidValue: DotMatrix.init(count: int, din: int, cs: int, clk: int) Please enter 3 non-duplicate pins")

    @staticmethod
    # DotMatrix.printStr(1, "Hello")
    def printStr(num: int, msg: str):
        if (num<1)or(num>8):
            warnings.warn("[Warning/DotMatrix.printStr(num: int, msg: str)]: 1<=num<=8")
        return Common.addHeader([Common.RUN_TYPE, 57]
                                +Common.transWizAscii(int(constrain(num,1,8))-1)
                                +Common.transWizAscii(msg))

    @staticmethod
    # DotMatrix.clearMatrix(1)
    def clearMatrix(num: int):
        if (num<1)or(num>8):
            warnings.warn("[Warning/DotMatrix.clearMatrix(num: int)]: 1<=num<=8")
        return Common.addHeader([Common.RUN_TYPE, 58] +Common.transWizAscii(int(constrain(num,1,8))-1))

    @staticmethod
    # DotMatrix.clearMatrixAll()
    def clearMatrixAll():
        return Common.addHeader([Common.RUN_TYPE, 59])

    @staticmethod
    # DotMatrix.setLine(1, "COL", 2, "11111111")
    def setLine(num: int, isRow: str, lineNum: int, data: str):
        if isRow in DotMatrix.isRow:
            tmpData=''
            for c in data:
                if c=='0' or c==' ':
                    tmpData+='0'
                else:
                    tmpData+='1'
            if len(tmpData)!=8:
                warnings.warn("[Warning/DotMatrix.setLine(num: int, isRow: str, lineNum: int, data: str)]: data length must be 8")
                tmpData.zfill(8)
                tmpData = tmpData[:8]
            return Common.addHeader([Common.RUN_TYPE, 60]
                                    +Common.transWizAscii(int(constrain(num,1,8))-1)
                                    +Common.transWizAscii(DotMatrix.isRow.index(isRow))
                                    +Common.transWizAscii(int(constrain(lineNum,1,8))-1)
                                    +Common.transWizAscii(tmpData))
        else:
            raise RuntimeError("InvalidValue: DotMatrix.setLine(num: int, isRow: str, lineNum: int, data: str) - isRow in"+str(DotMatrix.isRow))

    @staticmethod
    # DotMatrix.setDot(1, 2, 2, True)
    def setDot(num: int, row: int, col: int, isHigh: bool):
        if (not(1<=num<=8)) or (not(1<=row<=8)) or (not(1<=col<=8)):
            warnings.warn("[Warning/DotMatrix.setDot(num: int, row: int, col: int, isHigh: bool)]: Numbers are used only from 1 to 8")
        return Common.addHeader([Common.RUN_TYPE, 61]
                                +Common.transWizAscii(int(constrain(num,1,8))-1)
                                +Common.transWizAscii(int(constrain(row,1,8))-1)
                                +Common.transWizAscii(int(constrain(col,1,8))-1)
                                +Common.transWizAscii(1 if isHigh else 0))

    @staticmethod
    # DotMatrix.setBrightness(1, 8)
    def setBrightness(num: int, brightness: int):
        if not(1<=num<=8):
            warnings.warn("[Warning/DotMatrix.setBrightness(num: int, brightness: int)]: 1<=num<=8")
        if not(1<=brightness<=15):
            warnings.warn("[Warning/DotMatrix.setBrightness(num: int, brightness: int)]: 1<=brightness<=15")
        return Common.addHeader([Common.RUN_TYPE, 62]
                                +Common.transWizAscii(int(constrain(num,1,8))-1)
                                +Common.transWizAscii(int(constrain(brightness,1,15))))

    @staticmethod
    # DotMatrix.setLimit(1, 8)
    def setLimit(num: int, limit: int):
        if not(1<=num<=8):
            warnings.warn("[Warning/DotMatrix.setLimit(num: int, limit: int)]: 1<=num<=8")
        if not(1<=limit<=8):
            warnings.warn("[Warning/DotMatrix.setLimit(num: int, limit: int)]: 1<=limit<=8")
        return Common.addHeader([Common.RUN_TYPE, 63]
                                +Common.transWizAscii(int(constrain(num,1,8))-1)
                                +Common.transWizAscii(int(constrain(limit,1,8))-1))

    @staticmethod
    # DotMatrix.setShutdown(1, False)
    def setShutdown(num: int, isShutdown: bool):
        if not(1<=num<=8):
            warnings.warn("[Warning/DotMatrix.setShutdown(num: int, isShutdown: bool)]: 1<=num<=8")
        return Common.addHeader([Common.RUN_TYPE, 64]
                                +Common.transWizAscii(int(constrain(num,1,8))-1)
                                +Common.transWizAscii(1 if isShutdown else 0))


class Laser:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # Laser.init(18)
    def init(pin: int):
        if pin in Laser.pinList:
            return Common.addHeader([Common.RUN_TYPE, 48]
                                    +Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Laser.init(pin: int) - pin in"+str(Laser.pinList))

    @staticmethod
    # Laser.run(True)
    def run(isOn: bool):
        return Common.addHeader([Common.RUN_TYPE, 49]
                                +Common.transWizAscii(1 if isOn else 0))


class Mesh:
    @staticmethod
    # Mesh.init("GroupName")
    def init(groupName: str):
        return Common.addHeader([Common.RUN_TYPE, 101] + Common.transWizAscii(groupName))

    @staticmethod
    # Mesh.send("Message")
    def send(Message: str):
        return Common.addHeader([Common.RUN_TYPE, 102] + Common.transWizAscii(Message))

    @staticmethod
    # Mesh.isReceived("Message") -- write(...)와 사용할 것
    def isReceived(Message: str):
        return Common.addHeader([Common.READ_TYPE, 97] +Common.transWizAscii(Message))

    @staticmethod
    # Mesh.getReceivedMsg() -- write(...)와 사용할 것
    def getReceivedMsg():
        return Common.addHeader([Common.READ_TYPE, 95])

    @staticmethod
    # Mesh.isConnected() -- write(...)와 사용할 것
    def isConnected():
        return Common.addHeader([Common.READ_TYPE, 99])

    @staticmethod
    # Mesh.clearMsg()
    def clearMsg():
        return Common.addHeader([Common.RUN_TYPE, 103])


class InfraredThermometer:
    connect=["SCON", "MCON"]
    unit=["C", "F"]

    @staticmethod
    # InfraredThermometer.read("SCON", "C") -- write(...)와 사용할 것
    def read(_type: str, unit: str):
        if (_type in InfraredThermometer.connect)and(unit in InfraredThermometer.unit):
            return Common.addHeader([Common.READ_TYPE, 100+InfraredThermometer.connect.index(_type)]
                                    +Common.transWizAscii(InfraredThermometer.unit.index(unit)))
        else:
            raise RuntimeError("InvalidValue: InfraredThermometer.read(_type: str, unit: str) \
            _type in"+str(InfraredThermometer.connect)+", unit in"+str(InfraredThermometer.unit))


class DHT:  # Digital Humidity Temperature
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]
    unit=['C', 'F']

    @staticmethod
    # DHT.init(18)
    def init(pin: int):
        if pin in DHT.pinList:
            return Common.addHeader([Common.RUN_TYPE, 83]
                                    +Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: DHT.init(pin: int) - pin in "+str(DHT.pinList))

    @staticmethod
    # DHT.isConnected() -- write(...)와 사용할 것
    def isConnected():
        return Common.addHeader([Common.READ_TYPE, 91])

    @staticmethod
    # DHT.readHumidity() -- write(...)와 사용할 것
    def readHumidity():
        return Common.addHeader([Common.READ_TYPE, 90])

    @staticmethod
    # DHT.readTemperature("C") -- write(...)와 사용할 것
    def readTemperature(unit: str):
        if unit in DHT.unit:
            return Common.addHeader([Common.READ_TYPE, 89]
                                    +Common.transWizAscii(DHT.unit.index(unit)))
        else:
            raise RuntimeError("InvalidValue: DHT.readTemperature(unit: str) - unit in "+str(DHT.unit))


class HuskyLens:
    algorithmList=['FaceRecognition', 'ObjectTracking', 'ObjectRecognition',
                   'LineTracking', 'ColorRecognition', 'TagRecognition',
                   'ObjectClassification']
    type={'BOX': 42, 'ARROW': 43}
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
            raise RuntimeError("InvalidValue: HuskyLens.setMode(algorithm: str) - algorithm in "+str(HuskyLens.algorithmList))

    @staticmethod
    # HuskyLens.update()
    def update():
        return Common.addHeader([Common.RUN_TYPE, 67])

    @staticmethod
    # HuskyLens.isLearned(1) -- write(...)와 사용할 것
    def isLearned(_id: int):
        return Common.addHeader([Common.READ_TYPE, 79]+Common.transWizAscii(_id))

    @staticmethod
    # HuskyLens.isDetected(1, "ARROW") -- write(...)와 사용할 것
    def isDetected(_id: int, _type: str):
        if _type not in HuskyLens.type:
            raise RuntimeError("InvalidValue: HuskyLens.isDetected(_id: int, _type: str) - _type in "+str([*HuskyLens.type.keys()]))
        return Common.addHeader([Common.READ_TYPE, 84]+Common.transWizAscii(_id)+Common.transWizAscii(HuskyLens.type[_type]))

    @staticmethod
    # HuskyLens.getCountDetected() -- write(...)와 사용할 것
    def getCountDetected():
        return Common.addHeader([Common.READ_TYPE, 83])

    @staticmethod
    # HuskyLens.isDetectedType("ARROW") -- write(...)와 사용할 것
    def isDetectedType(_type: str):
        if _type not in HuskyLens.type:
            raise RuntimeError("InvalidValue: HuskyLens.isDetectedType(_type: str) - _type in "+str([*HuskyLens.type.keys()]))
        return Common.addHeader([Common.READ_TYPE, 82]+Common.transWizAscii(HuskyLens.type[_type]))

    @staticmethod
    # HuskyLens.getArrowInfo(1, "startX") -- write(...)와 사용할 것
    def getArrowInfo(_id: int, infoType: str):
        if infoType not in HuskyLens.arrowInfoType:
            raise RuntimeError("InvalidValue: HuskyLens.getArrowInfo(infoType: str) - infoType in "+str(HuskyLens.arrowInfoType))
        return Common.addHeader([Common.READ_TYPE, 81]+Common.transWizAscii(_id)+Common.transWizAscii(HuskyLens.arrowInfoType.index(infoType)))

    @staticmethod
    # HuskyLens.getBoxInfo(1, "centerX") -- write(...)와 사용할 것
    def getBoxInfo(_id: int, infoType: str):
        if infoType not in HuskyLens.boxInfoType:
            raise RuntimeError("InvalidValue: HuskyLens.getBoxInfo(infoType: str) - infoType in "+str(HuskyLens.boxInfoType))
        return Common.addHeader([Common.READ_TYPE, 94]+Common.transWizAscii(_id)+Common.transWizAscii(HuskyLens.boxInfoType.index(infoType)))

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
    # Button.read(13) -- write(...)와 사용할 것
    def read(pin: int):
        if pin in Button.pinList:
            return Common.addHeader([Common.READ_TYPE, 21]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Button.read(pin: int) - pin in "+str(Button.pinList))


class PhotoInterrupter:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # PhotoInterrupter.read(18) -- write(...)와 사용할 것
    def read(pin: int):
        if pin in PhotoInterrupter.pinList:
            return Common.addHeader([Common.READ_TYPE, 96]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: PhotoInterrupter.read(pin: int) - pin in "+str(PhotoInterrupter.pinList))


class WaterSensor:
    pinList = [32, 33, 36, 39]

    @staticmethod
    # SoilAndWater.read(36) -- write(...)와 사용할 것
    def read(pin: int):
        if pin in WaterSensor.pinList:
            return Common.addHeader([Common.READ_TYPE, 87]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: SoilAndWater.read(pin: int) - pin in "+str(WaterSensor.pinList))


SoilMoistureSensor = WaterSensor


class Potentiometer:
    pinList=[32, 33, 36, 39]

    @staticmethod
    # Potentiometer.read(36) -- write(...)와 사용할 것
    def read(pin: int):
        if pin in Potentiometer.pinList:
            return Common.addHeader([Common.READ_TYPE, 88]+Common.transWizAscii(pin))
        else:
            raise RuntimeError("InvalidValue: Potentiometer.read(pin: int) - pin in "+str(Potentiometer.pinList))


class ColorSensor:
    colorList=['Red', 'Green', 'Blue', 'White', 'Black']

    @staticmethod
    # ColorSensor.isColor("Red") -- write(...)와 사용할 것
    def isColor(color: str):
        if color in ColorSensor.colorList:
            return Common.addHeader([Common.READ_TYPE, 92]+Common.transWizAscii(ColorSensor.colorList.index(color)))
        else:
            raise RuntimeError("InvalidValue: ColorSensor.isColor(color: str) - color in "+str(ColorSensor.colorList))

    @staticmethod
    # ColorSensor.getColorValue("Red") -- write(...)와 사용할 것
    def getColorValue(color: str):
        if color in ColorSensor.colorList:
            return Common.addHeader([Common.READ_TYPE, 93]+Common.transWizAscii(ColorSensor.colorList[:3].index(color)))
        else:
            raise RuntimeError("InvalidValue: ColorSensor.getColorValue(color: str) - color in "+str(ColorSensor.colorList[:3]))


class Joystick:
    stickPinList=[32, 33, 36, 39]
    btnPinList=[-1, 13, 14, 15, 27, 18, 19]
    dirList=['X', 'Y']

    @staticmethod
    # Joystick.init(12, 36, 39, 15)  # 범위12 x축36 y축39 버튼15
    # Joystick.init(12, 36, 39)  # 범위12 x축36 y축39 버튼없음
    def init(_range: int, x: int, y: int, btn=-1):
        if (x not in Joystick.stickPinList)or(y not in Joystick.stickPinList):
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - x, y in "+str(Joystick.stickPinList))
        if x==y:
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - x!=y ")
        if btn not in Joystick.btnPinList:
            raise RuntimeError("InvalidValue: Joystick.init(_range: int, x: int, y: int, btn=-1) - btn in "+str(Joystick.btnPinList))
        return Common.addHeader([Common.RUN_TYPE, 55]
                                +Common.transWizAscii(x)
                                +Common.transWizAscii(y)
                                +Common.transWizAscii(btn)
                                +Common.transWizAscii(_range))

    @staticmethod
    # Joystick.readStick("X") -- write(...)와 사용할 것
    def readStick(_dir: str):
        if _dir in Joystick.dirList:
            return Common.addHeader([Common.READ_TYPE, 86]+Common.transWizAscii(Joystick.dirList.index(_dir)))
        else:
            raise RuntimeError("InvalidValue: Joystick.readStick(_dir: str) - _dir in "+str(Joystick.dirList))

    @staticmethod
    # Joystick.readButton() -- write(...)와 사용할 것
    def readButton():
        return Common.addHeader([Common.READ_TYPE, 85])


class PortManager:
    pinList=[13, 14, 15, 27, 32, 33, 18, 19]

    @staticmethod
    # PortManager.usePin(13)
    def usePin(pin: int):
        if pin in PortManager.pinList:
            return Common.addHeader([Common.READ_TYPE, 37]+Common.transWizAscii(PortManager.pinList.index(pin)))
        else:
            raise RuntimeError("InvalidValue: PortManager.usePin(pin: int) - pin in "+str(PortManager.pinList))

    @staticmethod
    # PortManager.digitalWrite(13, Ture)
    def digitalWrite(pin: int, isHigh: bool):
        if pin in PortManager.pinList:
            return Common.addHeader([Common.READ_TYPE, 2]
                                    +Common.transWizAscii(pin)
                                    +Common.transWizAscii(1 if isHigh else 0))
        else:
            raise RuntimeError("InvalidValue: PortManager.digitalWrite(pin: int, isHigh: bool) - pin in "+str(PortManager.pinList))

    @staticmethod
    # PortManager.analogWrite(13, 1023)
    def analogWrite(pin: int, value: int):
        if pin not in PortManager.pinList:
            raise RuntimeError("InvalidValue: PortManager.analogWrite(pin: int, value: int) - pin in "+str(PortManager.pinList))
        if value<0 or value>1023:
            warnings.warn("[Warning/PortManager.analogWrite(pin: int, value: int)]: value in range(0, 1024)")

        return Common.addHeader([Common.READ_TYPE, 38]
                                +Common.transWizAscii(pin)
                                +Common.transWizAscii(int(constrain(value,0,1023))))


class Bluetooth:
    mode=["master", "slave"]

    @staticmethod
    def init(_mode, _name, _interval=50):
        # Bluetooth.init("mastar", "WizFish", 50)
        if _mode==Bluetooth.mode[0]:
            return Common.addHeader([Common.READ_TYPE, 78]+ Common.transWizAscii(_name) + Common.transWizAscii(int(_interval)))
        elif _mode==Bluetooth.mode[1]:
            return Common.addHeader([Common.RUN_TYPE, 40] + Common.transWizAscii(_name))
        else:
            raise RuntimeError("InvalidValue: Bluetooth.init(_mode, _name, _interval=50) - _mode in "+str(Bluetooth.mode))

    @staticmethod
    def send(msg: str):
        # Bluetooth.send("Message")
        return Common.addHeader([Common.RUN_TYPE, 41]+ Common.transWizAscii(msg))

    @staticmethod
    # Bluetooth.getReceivedMsg()
    def getReceivedMsg():
        return Common.addHeader([Common.READ_TYPE, 74])

    @staticmethod
    # Bluetooth.read()
    def read():
        return Common.addHeader([Common.READ_TYPE, 76])

    @staticmethod
    # Bluetooth.readLine()
    def readLine():
        return Common.addHeader([Common.READ_TYPE, 75])


class WizCar:
    dir=['forward', 'backward', 'left', 'right']
    speed=['slow', 'normal', 'fast', 'extreme']

    @staticmethod
    def setMotor(lValue, rValue):
        # WizCar.setMotor(777, 777)
        if (lValue not in range(-1000, 1001)) or (rValue not in range(-1000, 1001)):
            warnings.warn("[Warning/WizCar.setMotor(lValue, rValue)]: values in range(-1000, 1001)")

        return Common.addHeader([Common.RUN_TYPE, 107]
                                + Common.transWizAscii(int(constrain(lValue,-1000,1000)))
                                + Common.transWizAscii(int(constrain(rValue,-1000,1000)))
                                )

    @staticmethod
    def runPreset(_dir, _speed):
        # WizCar.runPreset('forward', 'fast')
        if _dir not in WizCar.dir:
            raise RuntimeError("InvalidValue: WizCar.runPreset(_dir, _speed) - _dir in "+str(WizCar.dir))
        if _speed not in WizCar.speed:
            raise RuntimeError("InvalidValue: WizCar.runPreset(_dir, _speed) - _speed in "+str(WizCar.speed))

        return Common.addHeader([Common.RUN_TYPE, 108]
                                + Common.transWizAscii(WizCar.dir.index(_dir))
                                + Common.transWizAscii(WizCar.speed.index(_speed))
                                )

    @staticmethod
    def stop():
        # WizCar.stop()
        return Common.addHeader([Common.RUN_TYPE, 109])