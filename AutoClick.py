from adbutils import adb  # https://github.com/openatx/adbutils
from PIL import Image
from datetime import datetime
import time

IP_ADDRESS = "192.168.199.202"
PORT = 5792
# adb.connect("{}:{}".format(IP_ADDRESS, PORT))
# device = adb.device()


def connect(ip="{}:{}".format(IP_ADDRESS, PORT)):
    adb.connect(ip)
    return adb.device()


def screenshot(device=None, name=None):
    if device is None:
        device = connect()
    if name is None:
        name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    device.shell("screencap -p /sdcard/Pictures/Screenshots/" + name)
    device.sync.pull("/sdcard/Pictures/Screenshots/" + name, name)
    with Image.open(name) as image:
        image.show()


def tap(device, coordinate: (int, int)):
    device.click(*coordinate)
    time.sleep(0.2)


def swipe(device, start_coordinate: (int, int), changes_coordiante: (int, int),
          swipe_time):
    end_coordinate = map(sum, zip(start_coordinate, changes_coordiante))
    device.swipe(*start_coordinate, *end_coordinate, swipe_time)
    time.sleep(0.3)
