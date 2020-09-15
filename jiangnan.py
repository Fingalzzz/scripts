from AutoClick import *
import time

VERSION_CODE = "1.1.1"

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


def tap(coordinate: (int, int)):
    device.click(*coordinate)
    time.sleep(0.2)


def suzhou_well():
    tap(FUYING)
    tap(DIJI)
    tap(FUYING)
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
        tap(coor_well)
        device.click(380, 627)
        device.click(380, 627)


def move_to_suzhou():
    tap(FUYING)
    tap(MAP)
    device.swipe(*SWIPE_MAP)
    tap(SUZHOU)
    time.sleep(7)
    tap(ZHIDAOLE)


def move_to_yingtian():
    tap(FUYING)
    tap(MAP)
    tap(YINGTIAN)
    time.sleep(7)
    tap(ZHIDAOLE)


if __name__ == "__main__":
    print(VERSION_CODE)
    while True:
        move_to_yingtian()
        move_to_suzhou()
        suzhou_well()
        time.sleep(80)
