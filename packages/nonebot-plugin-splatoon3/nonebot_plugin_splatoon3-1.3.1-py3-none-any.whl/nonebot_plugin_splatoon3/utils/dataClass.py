import datetime
import re
from datetime import timedelta


# 类 图片信息 ImageInfo
class ImageInfo:
    def __init__(self, name, url, zh_name, source_type):
        self.name = name
        self.url = url
        self.zh_name = zh_name
        self.source_type = source_type


# 类 数据表 Weapon_Info + Weapon_Images
class WeaponData:
    # zh 字段暂且预留，方便后续翻译的进行
    # 为了便于先进行 INFO 信息的查询，image 字段默认留空
    def __init__(
        self,
        name,
        sub_name,
        special_name,
        special_points,
        level,
        weapon_class,
        image=None,
        sub_image=None,
        special_image=None,
        weapon_class_image=None,
        zh_name="None",
        zh_sub_name="None",
        zh_special_name="None",
        zh_weapon_class="None",
        zh_father_class="None",
    ):
        self.name = name
        self.image = image
        self.sub_name = sub_name
        self.sub_image = sub_image
        self.special_name = special_name
        self.special_image = special_image
        self.special_points = special_points
        self.level = level
        self.weapon_class = weapon_class
        self.weapon_class_image = weapon_class_image
        self.zh_name = zh_name
        self.zh_sub_name = zh_sub_name
        self.zh_special_name = zh_special_name
        self.zh_weapon_class = zh_weapon_class
        self.zh_father_class = zh_father_class


# 类 时区工具
class TimeUtil(object):
    @classmethod
    def parse_timezone(cls, timezone):
        """
        解析时区表示
        :param timezone: str eg: +8
        :return: dict{symbol, offset}
        """
        result = re.match(r"(?P<symbol>[+-])(?P<offset>\d+)", timezone)
        symbol = result.groupdict()["symbol"]
        offset = int(result.groupdict()["offset"])

        return {"symbol": symbol, "offset": offset}

    @classmethod
    def convert_timezone(cls, dt, timezone="+0") -> datetime.datetime:
        """默认是utc时间，需要提供时区"""
        result = cls.parse_timezone(timezone)
        symbol = result["symbol"]

        offset = result["offset"]

        if symbol == "+":
            return dt + timedelta(hours=offset)
        elif symbol == "-":
            return dt - timedelta(hours=offset)
        else:
            raise Exception("dont parse timezone format")
