import time


class WizSensorData:
    sensorData={
        "mic":0,
        "light":0,
        "hallSensor":0,
        "distance":0,
        "touchPin_1":False,     # 13
        "touchPin_2":False,     # 14
        "touchPin_3":False,     # 15
        "touchPin_4":False,     # 27
        "touchPin_5":False,     # 32
        "touchPin_6":False,     # 33
        "button_right":False,   # 4
        "button_left":False,    # 26
        "gyroX":0,
        "gyroY":0,
        "gyroZ":0,
        "tempSensor":0,
    }

    def getMic(self):
        return self.sensorData["mic"]

    def getLight(self):
        return self.sensorData["light"]

    def getHall(self):
        return self.sensorData["hallSensor"]

    def getDistance(self):
        return self.sensorData["distance"]

    def getTouchValue(self):
        return {
            13: self.sensorData["touchPin_1"], 14: self.sensorData["touchPin_2"],
            15: self.sensorData["touchPin_3"], 27: self.sensorData["touchPin_4"],
            32: self.sensorData["touchPin_5"], 33: self.sensorData["touchPin_6"],
        }

    def getButtonValue(self):
        return {"left": self.sensorData["button_left"], "right": self.sensorData["button_right"]}

    def getGyroValue(self):
        return {"X": self.sensorData["gyroX"], "Y": self.sensorData["gyroY"], "Z": self.sensorData["gyroZ"]}

    def getTemperature(self):
        return self.sensorData["tempSensor"]

    @staticmethod
    def getCurrentTime():
        curTime = time.strftime('%A %S %M %H %d %m %Y', time.localtime(time.time())).split(" ")
        key=["dayOfTheWeek", "second", "minute", "hour", "day", "month", "year"]
        return dict(zip(key, curTime))