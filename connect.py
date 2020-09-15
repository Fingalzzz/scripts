from ppadb.client import Client as adbClient


def adbConnect():
    client = adbClient()
    client.remote_connect("192.168.199.202", 5792)
    device = client.device("192.168.199.202:5792")
#    device.shell("input tap 500 500")
    return device
