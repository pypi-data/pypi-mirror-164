from CodeWiz.WizSerial import WizSerial
from CodeWiz.WizDefaultSensor import WizSensorData
from CodeWiz import WizData


class _V:
    Sensor= WizSensorData()
    wizSerial=None


class Device:
    Sensor= _V.Sensor

    @staticmethod
    def connect(COM):
        if _V.wizSerial is None:
            _V.wizSerial=WizSerial(COM, _V.Sensor)
        return _V.wizSerial
        #     return _V.wizSerial
        # else:
        #     return _V.wizSerial

    @staticmethod
    def disconnect():
        if _V.wizSerial is not None:
            _V.wizSerial.end()
            _V.wizSerial=None

    @staticmethod
    def getFirmwareVersion():
        if _V.wizSerial is None:
            return "Not Connected"
        else:
            _V.wizSerial.write(WizData.Common.firmVersion)
            return _V.wizSerial.getData()

    @staticmethod
    def sensorStart():
        if _V.wizSerial is None:
            raise RuntimeError("Must be connected to CodeWiz")
        _V.wizSerial.runDefaultSensor()

    class NeoPixel:
        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.init(*params))

        @staticmethod
        def setBrightness(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.setBrightness(*params))

        @staticmethod
        def setColor(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.setColor(*params))

        @staticmethod
        def setColorAll(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.setColorAll(*params))

        @staticmethod
        def clear():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.clear())

        @staticmethod
        def fillRandomColor():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.fillRandomColor())

        @staticmethod
        def setRandomColor(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.setRandomColor(*params))

        @staticmethod
        def rotate(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.rotate(*params))

        @staticmethod
        def shift(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.shift(*params))

        @staticmethod
        def gradationRGB(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.gradationRGB(*params))

        @staticmethod
        def gradationHSL(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.gradationRGB(*params))

        @staticmethod
        def wheel():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.NeoPixel.wheel())

    class Speaker:
        @staticmethod
        def getNoteList():
            return list(WizData.Speaker.value)

        @staticmethod
        def getOctaveList():
            return list(WizData.Speaker.octave)

        @staticmethod
        def getBeatList():
            return list(WizData.Speaker.beatList)

        @staticmethod
        def init():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Speaker.init())

        @staticmethod
        def play(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Speaker.play(*params))

        @staticmethod
        def off():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Speaker.off())

    class Oled:
        @staticmethod
        def getColorList():
            return list(WizData.Oled.colorList)

        @staticmethod
        def getDirList():
            return list(WizData.Oled.dirList)

        @staticmethod
        def init():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.init())

        @staticmethod
        def clear():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.clear())

        @staticmethod
        def reverseMode(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.reverseMode(*params))

        @staticmethod
        def setFontSize(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.setFontSize(*params))

        @staticmethod
        def setCursor(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.setCursor(*params))

        @staticmethod
        def print(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.print(*params))

        @staticmethod
        def printHangul(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.printHangul(*params))

        @staticmethod
        def lineBreakMode(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.lineBreakMode(*params))

        @staticmethod
        def scroll(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.scroll(*params))

        @staticmethod
        def stopScroll():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.stopScroll())

        @staticmethod
        def drawDot(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.drawDot(*params))

        @staticmethod
        def drawLine(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.drawLine(*params))

        @staticmethod
        def drawRect(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.drawRect(*params))

        @staticmethod
        def drawCircle(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.drawCircle(*params))

        @staticmethod
        def drawTriangle(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Oled.drawTriangle(*params))

    class RadioMesh:
        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.RadioMesh.init(*params))

        @staticmethod
        def send(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.RadioMesh.send(*params))

        @staticmethod
        def getReceivedMsg():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.RadioMesh.getReceivedMsg())
            return _V.wizSerial.getData()

        @staticmethod
        def clearMsg():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.RadioMesh.clearMsg())

    class Servo:
        @staticmethod
        def getConnectList():
            return list(WizData.Servo.mode)

        @staticmethod
        def getPinList():
            return list(WizData.Servo.pinNumber.keys())

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Servo.init(*params))

        @staticmethod
        def setAngle(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Servo.setAngle(*params))

        @staticmethod
        def setVelocity(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Servo.setVelocity(*params))

    class WaterPump:
        @staticmethod
        def getMotorList():
            return WizData.WaterPump.motorNum

        @staticmethod
        def init():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WaterPump.init())

        @staticmethod
        def run(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WaterPump.run(*params))

    class Propeller:
        @staticmethod
        def getPinList():
            return list(WizData.Propeller.pinNumber)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Propeller.init(*params))

        @staticmethod
        def run(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Propeller.run(*params))

    class Vibrator:
        @staticmethod
        def getPinList():
            return list(WizData.Vibrator.pinNumber)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Vibrator.init(*params))

        @staticmethod
        def run(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Vibrator.run(*params))

    class DcMotor:
        @staticmethod
        def getMotorList():
            return list(WizData.DcMotor.motorNum)

        @staticmethod
        def init():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DcMotor.init())

        @staticmethod
        def run(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DcMotor.run(*params))

    class DotMatrix:
        @staticmethod
        def getPinList():
            return list(WizData.DotMatrix.pinNumber)

        @staticmethod
        def getDirList():
            return list(WizData.DotMatrix.isRow)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.init(*params))

        @staticmethod
        def printStr(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.printStr(*params))

        @staticmethod
        def clearMatrix(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.clearMatrix(*params))

        @staticmethod
        def clearMatrixAll():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.clearMatrixAll())

        @staticmethod
        def setLine(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.setLine(*params))

        @staticmethod
        def setDot(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.setDot(*params))

        @staticmethod
        def setBrightness(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.setBrightness(*params))

        @staticmethod
        def setLimit(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.setLimit(*params))

        @staticmethod
        def setShutdown(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DotMatrix.setShutdown(*params))

    class Laser:
        @staticmethod
        def getPinList():
            return list(WizData.Laser.pinList)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Laser.init(*params))

        @staticmethod
        def run(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Laser.run(*params))

    class Mesh:
        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.init(*params))

        @staticmethod
        def send(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.send(*params))

        @staticmethod
        def isReceived(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.isReceived(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def getReceivedMsg():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.getReceivedMsg())
            return _V.wizSerial.getData()

        @staticmethod
        def isConnected():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.isConnected())
            return _V.wizSerial.getData()

        @staticmethod
        def clearMsg():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Mesh.clearMsg())

    class InfraredThermometer:
        @staticmethod
        def getConnectList():
            return list(WizData.InfraredThermometer.connect)

        @staticmethod
        def getUnitList():
            return list(WizData.InfraredThermometer.unit)

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.InfraredThermometer.read(*params))
            return _V.wizSerial.getData()

    class DHT:  # Digital Humidity Temperature
        @staticmethod
        def getPinList():
            return list(WizData.DHT.pinList)

        @staticmethod
        def getUnitList():
            return list(WizData.DHT.unit)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DHT.init(*params))

        @staticmethod
        def isConnected():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DHT.isConnected())
            return _V.wizSerial.getData()

        @staticmethod
        def readHumidity():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DHT.readHumidity())
            return _V.wizSerial.getData()

        @staticmethod
        def readTemperature(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.DHT.readTemperature(*params))
            return _V.wizSerial.getData()

    class HuskyLens:
        @staticmethod
        def getModeList():
            return list(WizData.HuskyLens.algorithmList)

        @staticmethod
        def getTypeList():
            return list(WizData.HuskyLens.type.keys())

        @staticmethod
        def getArrowInfoType():
            return list(WizData.HuskyLens.arrowInfoType)

        @staticmethod
        def getBoxInfoType():
            return list(WizData.HuskyLens.boxInfoType)

        @staticmethod
        def init():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.init())

        @staticmethod
        def setMode(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.setMode(*params))

        @staticmethod
        def update():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.update())

        @staticmethod
        def isLearned(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.isLearned(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def isDetected(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.isDetected(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def getCountDetected():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.getCountDetected())
            return _V.wizSerial.getData()

        @staticmethod
        def isDetectedType(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.isDetectedType(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def getArrowInfo(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.getArrowInfo(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def getBoxInfo(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.getBoxInfo(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def drawText(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.drawText(*params))

        @staticmethod
        def clearText():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.HuskyLens.clearText())

    class Button:
        @staticmethod
        def getPinList():
            return list(WizData.Button.pinList)

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Button.read(*params))
            return _V.wizSerial.getData()

    class PhotoInterrupter:
        @staticmethod
        def getPinList():
            return list(WizData.PhotoInterrupter.pinList)

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.PhotoInterrupter.read(*params))
            return _V.wizSerial.getData()

    class WaterSensor:
        @staticmethod
        def getPinList():
            return list(WizData.WaterSensor.pinList)

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WaterSensor.read(*params))
            return _V.wizSerial.getData()

    SoilMoistureSensor = WaterSensor

    class Potentiometer:
        @staticmethod
        def getPinList():
            return list(WizData.Potentiometer.pinList)

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.PhotoInterrupter.read(*params))
            return _V.wizSerial.getData()

    class ColorSensor:
        @staticmethod
        def getColorList():
            return list(WizData.ColorSensor.colorList)

        @staticmethod
        def isColor(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.ColorSensor.isColor(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def getColorValue(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.ColorSensor.getColorValue(*params))
            return _V.wizSerial.getData()

    class Joystick:
        @staticmethod
        def getStickList():
            return list(WizData.Joystick.stickPinList)

        @staticmethod
        def getButtonList():
            return list(WizData.Joystick.btnPinList)

        @staticmethod
        def getDirList():
            return list(WizData.Joystick.dirList)

        @staticmethod
        def init(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Joystick.init(*params))

        @staticmethod
        def readStick(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Joystick.readStick(*params))
            return _V.wizSerial.getData()

        @staticmethod
        # Joystick.readButton() -- write(...)와 사용할 것
        def readButton():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Joystick.readButton())
            return _V.wizSerial.getData()

    class PortManager:
        @staticmethod
        def getPinList():
            return list(WizData.PortManager.pinList)

        @staticmethod
        def usePin(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.PortManager.usePin(*params))

        @staticmethod
        def digitalWrite(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.PortManager.digitalWrite(*params))

        @staticmethod
        def analogWrite(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.PortManager.analogWrite(*params))

    class Bluetooth:
        @staticmethod
        def getModeList():
            return list(WizData.Bluetooth.mode)

        @staticmethod
        def init(_mode, _name, _interval):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Bluetooth.init(_mode, _name, _interval))
            if _mode==WizData.Bluetooth.mode[0]:
                return _V.wizSerial.getData()
            elif _mode==WizData.Bluetooth.mode[1]:
                return True
            else:
                return False

        @staticmethod
        def send(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Bluetooth.send(*params))

        @staticmethod
        def getReceivedMsg(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Bluetooth.getReceivedMsg(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def read(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Bluetooth.read(*params))
            return _V.wizSerial.getData()

        @staticmethod
        def readLine(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.Bluetooth.readLine(*params))
            return _V.wizSerial.getData()

    class WizCar:
        @staticmethod
        def getDirList():
            return list(WizData.WizCar.dir)

        @staticmethod
        def getSpeedList():
            return list(WizData.WizCar.speed)

        @staticmethod
        def setMotor(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WizCar.setMotor(*params))

        @staticmethod
        def runPreset(*params):
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WizCar.runPreset(*params))

        @staticmethod
        def stop():
            if _V.wizSerial is None:
                raise RuntimeError("Must be connected to CodeWiz")
            _V.wizSerial.write(WizData.WizCar.stop())