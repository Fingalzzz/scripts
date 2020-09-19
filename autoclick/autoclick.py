from adbutils import adb  # https://github.com/openatx/adbutils
from PIL import Image
from datetime import datetime
import time
import json
import sys


class AdbConnectError(Exception):
    """
    Raised when cannot connect to the phone
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


with open('config.json') as f:
    config = json.load(f)
    IP_ADDRESS = config.get("ip_address")
    PORT = config.get("port")

try:
    message = adb.connect("{}:{}".format(IP_ADDRESS, PORT))
    if "cannot" in message:
        raise AdbConnectError(message)
except AdbConnectError as e:
    print(e)
    sys.exit(
        "Please read the README and change ip_address and port in the config.py file."
    )
else:
    device = adb.device()


def screenshot(name=None):
    if name is None:
        name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    device.shell("screencap -p /sdcard/Pictures/Screenshots/auto.png")
    device.sync.pull("/sdcard/Pictures/Screenshots/auto.png", name)
    device.shell("rm /sdcard/Pictures/Screenshots/auto.png")
    with Image.open(name) as image:
        image.show()


def tap(coordinate: (int, int)):
    device.click(*coordinate)
    time.sleep(0.2)


def swipe(start_coordinate: (int, int), changes_coordiante: (int, int),
          swipe_time):
    end_coordinate = map(sum, zip(start_coordinate, changes_coordiante))
    device.swipe(*start_coordinate, *end_coordinate, swipe_time)
    time.sleep(0.3)
