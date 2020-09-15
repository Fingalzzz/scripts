from AutoClick import *

WELL_NUM = 36
WELL_HEAD = (850, 300)
EMPTY_WELL_LIST = [7, 10, 14, 21, 22, 25, 27]
X_RANGE = 120
Y_RANGE = 60

FUYING = (200, 1000)
MAP = (300, 500)
DIJI = (600, 500)

SUZHOU = (1100, 700)
YINGTIAN = (800, 700)

SWIPE_MAP = (1800, 900, 1800 - 867, 900 - 563, 1)
SWIPE_SUZHOU_WELL = (200, 200, 200 + 2000, 200 + 532, 1.5)


def suzhou_well():
    device.click(*FUYING)
    device.click(*DIJI)
    device.click(*FUYING)
    device.swipe(*SWIPE_SUZHOU_WELL)
    for i in range(36):
        if i in EMPTY_WELL_LIST:
            continue
        quotient = i // 6
        remainder = i % 6
        well_x = WELL_HEAD[0] + (quotient - remainder) * X_RANGE
        well_y = WELL_HEAD[1] + (quotient + remainder) * Y_RANGE
        coor_well = (well_x, well_y)
        device.click(*coor_well)
        device.click(1250, 250)
        device.click(1250, 250)


def move_to_suzhou():
    device.click(*FUYING)
    device.click(*MAP)
    device.shell("sleep 0.5")
    device.swipe(*SWIPE_MAP)
    device.click(*SUZHOU)


def move_to_yingtian():
    device.click(*FUYING)
    device.click(*MAP)
    device.shell("sleep 0.5")
    device.click(*YINGTIAN)


if __name__ == "__main__":
    move_to_yingtian()
    device.shell("sleep 5")
    move_to_suzhou()
    device.shell("sleep 5")
    suzhou_well()
