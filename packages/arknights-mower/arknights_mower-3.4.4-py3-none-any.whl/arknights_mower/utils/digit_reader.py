import cv2 as cv
import numpy as np
from pathlib import Path
import os
from .image import loadimg, saveimg
from .. import __rootdir__


class DigitReader:
    def __init__(self, template_dir=None):
        if not template_dir:
            template_dir = Path(os.path.dirname(os.path.abspath(__file__))) / Path("templates")
        if not isinstance(template_dir, Path):
            template_dir = Path(template_dir)
        self.time_template = []
        self.drone_template = []
        for i in range(10):
            self.time_template.append(
                loadimg(f'{__rootdir__}/resources/orders_time/{i}.png', True)
            )
            self.drone_template.append(
                loadimg(f'{__rootdir__}/resources/drone_count/{i}.png', True)
            )

    def get_drone(self, img_grey, h=1080, w=1920):
        drone_part = img_grey[h * 32 // 1080:h * 76 // 1080, w * 1144 // 1920:w * 1225 // 1920]
        drone_part = cv.resize(drone_part, (81, 44), interpolation=cv.INTER_AREA)
        result = {}
        for j in range(10):
            res = cv.matchTemplate(
                drone_part,
                self.drone_template[j],
                cv.TM_CCORR_NORMED,
            )
            threshold = 0.95
            loc = np.where(res >= threshold)
            for i in range(len(loc[0])):
                offset = loc[1][i]
                accept = True
                for o in result:
                    if abs(o - offset) < 5:
                        accept = False
                        break
                if accept:
                    result[loc[1][i]] = j
        l = [str(result[k]) for k in sorted(result)]
        return int("".join(l))

    def get_time(self, img_grey, h, w):
        digit_part = img_grey[h * 510 // 1080:h * 543 // 1080, w * 499 // 1920:w]
        digit_part = cv.resize(digit_part, (1421, 33), interpolation=cv.INTER_AREA)
        result = {}
        for j in range(10):
            res = cv.matchTemplate(
                digit_part,
                self.time_template[j],
                cv.TM_CCOEFF_NORMED,
            )
            threshold = 0.85
            loc = np.where(res >= threshold)
            for i in range(len(loc[0])):
                x = loc[1][i]
                accept = True
                for o in result:
                    if abs(o - x) < 5:
                        accept = False
                        break
                if accept:
                    if len(result) == 0:
                        digit_part = digit_part[:, loc[1][i] - 5: loc[1][i] + 116]
                        offset = loc[1][0] - 5
                        for m in range(len(loc[1])):
                            loc[1][m] -= offset
                    result[loc[1][i]] = j
        l = [str(result[k]) for k in sorted(result)]
        return f"{l[0]}{l[1]}:{l[2]}{l[3]}:{l[4]}{l[5]}"

    def 识别制造加速总剩余时间(self, img_grey, h, w):
        时间部分 = img_grey[h * 665 // 1080:h * 709 // 1080, w * 750 // 1920:w * 960 // 1920]
        时间部分 = cv.resize(时间部分, (210*58//71, 44*58//71), interpolation=cv.INTER_AREA)
        result = {}
        for j in range(10):
            res = cv.matchTemplate(
                时间部分,
                self.drone_template[j],
                cv.TM_CCORR_NORMED,
            )
            threshold = 0.92
            loc = np.where(res >= threshold)
            for i in range(len(loc[0])):
                offset = loc[1][i]
                accept = True
                for o in result:
                    if abs(o - offset) < 5:
                        accept = False
                        break
                if accept:
                    result[loc[1][i]] = j
        l = [str(result[k]) for k in sorted(result)]
        return f"{l[0]}{l[1]}{l[2]}:{l[3]}{l[4]}:{l[5]}{l[6]}"
