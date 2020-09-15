from adbutils import adb  # https://github.com/openatx/adbutils
from PIL import Image
from datetime import datetime

IP_ADDRESS = "192.168.199.202"
PORT = 5792


def remote_connect(ip="{}:{}".format(IP_ADDRESS, PORT)):
    adb.connect(ip)


def get_device(serial="{}:{}".format(IP_ADDRESS, PORT)):
    return adb.device(serial)


def screenshot(device=None, name=None):
    if device is None:
        device = get_device()
    if name is None:
        name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    device.shell("screencap -p /sdcard/Pictures/Screenshots/" + name)
    device.sync.pull("/sdcard/Pictures/Screenshots/" + name, name)
    with Image.open(name) as image:
        image.show()


remote_connect()
device = get_device()
