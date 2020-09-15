from AutoClick import *
import time

WELL_NUM = 36
WELL_HEAD = (520, 1256)
EMPTY_WELL_LIST = [5, 7, 10, 14, 21, 22, 25, 27, 30]
X_RANGE = 120
Y_RANGE = 60

FUYING = (130, 2130)
MAP = (136, 1736)
DIJI = (382, 1768)

SUZHOU = (805, 1076)
YINGTIAN = (402, 1155)
ZHIDAOLE = (677, 1797)

SWIPE_MAP = (908, 1648, 908 - 776, 1648 - 599, 1)
SWIPE_SUZHOU_WELL = (10, 722, 1075, 1100, 3.5)


def suzhou_well():
    device.click(*FUYING)
    device.click(*DIJI)
    device.click(*FUYING)
    time.sleep(0.2)
    device.swipe(*SWIPE_SUZHOU_WELL)
    time.sleep(2)
    for i in range(36):
        if i in EMPTY_WELL_LIST:
            continue
        quotient = i // 6
        remainder = i % 6
        well_x = WELL_HEAD[0] + (-quotient + remainder) * X_RANGE
        well_y = WELL_HEAD[1] + (quotient + remainder) * Y_RANGE
        coor_well = (well_x, well_y)
        device.click(*coor_well)
        time.sleep(0.1)
        device.click(380, 627)
        time.sleep(0.1)
        device.click(380, 627)
        time.sleep(0.1)


def move_to_suzhou():
    device.click(*FUYING)
    device.click(*MAP)
    time.sleep(0.5)
    device.swipe(*SWIPE_MAP)
    device.click(*SUZHOU)
    time.sleep(5)
    device.click(*ZHIDAOLE)
    time.sleep(0.3)


def move_to_yingtian():
    device.click(*FUYING)
    device.click(*MAP)
    time.sleep(0.5)
    device.click(*YINGTIAN)
    time.sleep(5)
    device.click(*ZHIDAOLE)
    time.sleep(0.3)


if __name__ == "__main__":
    while True:
        move_to_yingtian()
        move_to_suzhou()
        suzhou_well()
        time.sleep(80)
