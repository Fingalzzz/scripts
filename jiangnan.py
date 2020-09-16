import autoclick
import time

FUYING = (130, 2130)
MAP = (136, 1736)
DIJI = (382, 1768)

SUZHOU = (805, 1076)
YINGTIAN = (402, 1155)
ZHIDAOLE = (677, 1797)

# SWIPE_MAP = (908, 1648, 908 - 776, 1648 - 599, 0.5)
SWIPE_MAP_START = (908, 1648)
SWIPE_MAP_CHANGES = (-776, -559)
# SWIPE_SUZHOU_WELL = (10, 722, 1075, 1100, 1.5)
SWIPE_SUZHOU_WELL_START = (10, 722)
SWIPE_SUZHOU_WELL_CHANGES = (1065, 378)

WELL_NUM = 36
WELL_HEAD = (520, 1256)
EMPTY_WELL_LIST = [5, 7, 10, 14, 21, 22, 25, 27, 30]
X_RANGE = 120
Y_RANGE = 60


def suzhou_fish_shop():
    pass


def suzhou_well(device):
    autoclick.tap(device, FUYING)
    autoclick.tap(device, DIJI)
    autoclick.tap(device, FUYING)
    autoclick.swipe(device, SWIPE_SUZHOU_WELL_START, SWIPE_SUZHOU_WELL_CHANGES,
                    3)
    # device.swipe(*SWIPE_SUZHOU_WELL)
    for i in range(36):
        if i in EMPTY_WELL_LIST:
            continue
        quotient = i // 6
        remainder = i % 6
        well_x = WELL_HEAD[0] + (-quotient + remainder) * X_RANGE
        well_y = WELL_HEAD[1] + (quotient + remainder) * Y_RANGE
        coor_well = (well_x, well_y)
        autoclick.tap(device, coor_well)
        device.click(380, 627)
        device.click(380, 627)


def move_to_suzhou(device):
    autoclick.tap(device, FUYING)
    autoclick.tap(device, MAP)
    time.sleep(0.5)
    # device.swipe(*SWIPE_MAP)
    autoclick.swipe(device, SWIPE_MAP_START, SWIPE_MAP_CHANGES, 1)
    autoclick.tap(device, SUZHOU)
    time.sleep(7)
    autoclick.tap(device, ZHIDAOLE)


def move_to_yingtian(device):
    autoclick.tap(device, FUYING)
    autoclick.tap(device, MAP)
    time.sleep(0.5)
    autoclick.tap(device, YINGTIAN)
    time.sleep(7)
    autoclick.tap(device, ZHIDAOLE)


if __name__ == "__main__":
    op6t = autoclick.connect()
    while True:
        move_to_yingtian(op6t)
        move_to_suzhou(op6t)
        suzhou_well(op6t)
        time.sleep(80)
