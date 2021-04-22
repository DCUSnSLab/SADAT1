import datetime as pydatetime
import numpy
from numpy import inf
import math
from GrabberROS import GrabberROS
from log.makeRPLidarLog import RPLidarLogType
from sensor.SenAdptMgr import AttachedSensorName


def get_now():
    return pydatetime.datetime.now()

def get_now_timestamp():
    return get_now().timestamp()


class GrabberROSrplidar(GrabberROS):
    def __init__(self, _log):
        super().__init__(_log, AttachedSensorName.RPLidar2DA3, 'LidarGrabber', 'scan')

    def userCallBack(self, msg):
        # print(len(msg.ranges))
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        angle_inc = msg.angle_increment
        #print(angle_min, angle_max, angle_inc)
        cnt = 0

        rpdata = RPLidarLogType()
        distance = list()
        angle = list()
        timestamp = 0

        for data in msg.ranges:
            range = data
            if data == inf:
                range = 0
            rosdata = self._log.makeDatafromROS(math.degrees(angle_min+(angle_inc * cnt)), range*1000, cnt, get_now_timestamp())
            distance.append(rosdata['distance'])
            angle.append(rosdata['angle'])
            timestamp = rosdata['timestamp']
            cnt += 1

        rpdata.distance = numpy.array(distance)
        rpdata.angle = numpy.array(angle)
        rpdata.timestamp = timestamp
        rpdata.start_flag = True
        self.sendData(rpdata)