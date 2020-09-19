import autoclick
import time

FUYING = (130, 2130)
MAP = (136, 1736)
DIJI = (382, 1768)

SUZHOU = (805, 1076)
YINGTIAN = (402, 1155)
ZHIDAOLE = (677, 1797)

PEOPLE = (380, 627)
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
    # TODO: click fish shop to make money <19-09-20, Fingalzzz> #
    pass


def suzhou_well():
    autoclick.tap(FUYING)
    autoclick.tap(DIJI)
    autoclick.tap(FUYING)
    autoclick.swipe(SWIPE_SUZHOU_WELL_START, SWIPE_SUZHOU_WELL_CHANGES, 3)
    for i in range(36):
        if i in EMPTY_WELL_LIST:
            continue
        quotient = i // 6
        remainder = i % 6
        well_x = WELL_HEAD[0] + (-quotient + remainder) * X_RANGE
        well_y = WELL_HEAD[1] + (quotient + remainder) * Y_RANGE
        coor_well = (well_x, well_y)
        autoclick.tap(coor_well)
        autoclick.tap(PEOPLE)
        autoclick.tap(PEOPLE)


def move_to_suzhou():
    autoclick.tap(FUYING)
    autoclick.tap(MAP)
    time.sleep(0.5)
    # device.swipe(*SWIPE_MAP)
    autoclick.swipe(SWIPE_MAP_START, SWIPE_MAP_CHANGES, 1)
    autoclick.tap(SUZHOU)
    time.sleep(7)
    autoclick.tap(ZHIDAOLE)


def move_to_yingtian():
    autoclick.tap(FUYING)
    autoclick.tap(MAP)
    time.sleep(0.5)
    autoclick.tap(YINGTIAN)
    time.sleep(7)
    autoclick.tap(ZHIDAOLE)


if __name__ == "__main__":
    while True:
        move_to_yingtian()
        move_to_suzhou()
        suzhou_well()
        time.sleep(80)
