from enum import Enum
from multiprocessing import Manager

from sensor.Sensor import Sensor


class SourceManager:
    def __init__(self, manager:Manager):
        self.ActualSensor = dict()
        self.VirtualSensor = dict()
        self.AllSensors = dict()

        self.dataLoadQueue = manager.Queue()

    def init(self):
        pass

    def addActualSensor(self, sens, man):
        self.__addSensor(self.ActualSensor, sens, man)

    def addVirtualSensor(self, sens, man):
        self.__addSensor(self.VirtualSensor, sens, man)

    def __addSensor(self, sendict:dict, sensor:Sensor, man:Manager):
        if (sensor.sensorName in sendict) is False:
            sensor.setupDataManager(man)
            sendict[sensor.sensorName] = sensor
            self.AllSensors[sensor.sensorName] = sensor
        else:
            print("error SensorName: %s already in SensorList" % sensor.sensorName)

    def getSensorbyName(self, name:str):
        if name in self.AllSensors:
            return self.AllSensors[name]
        else:
            return None

    def simEvent(self, evalue:list):
        self.dataLoadQueue.put(evalue)
        self.dataLoadQueue.put('interrupt')

    def waitSimDataLoad(self):
        loadedSensor = None

        for data in iter(self.dataLoadQueue.get, 'interrupt'):
            if data is not None and len(data) > 0:
                loadedSensor = data
        return loadedSensor

    def printSensorList(self):
        print("-"*30)
        print("Adapted Sensor List")
        for sen in self.AllSensors.values():
            print("stype: %s, scate : %s, sname : %s" % (str(sen.sensorType), str(sen.sensorCategory), sen.sensorName))
        print("-" * 30)