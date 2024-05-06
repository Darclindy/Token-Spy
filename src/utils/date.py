import datetime
import pytz

def convert_timestamp_to_utc(timestamp):
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    dt_object_utc = dt_object.astimezone(pytz.UTC)
    formatted_time = dt_object_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return formatted_time


def round_down_timestamp_to_nearest_five_minutes(timestamp):
    # 将时间戳转换为datetime对象
    dt = datetime.datetime.fromtimestamp(timestamp)

    # 只舍不入到最近的5分钟
    minutes = (dt.minute // 5) * 5

    # 创建一个新的datetime对象，分钟和秒数已经被舍去
    rounded_dt = dt.replace(minute=minutes, second=0)

    # 将结果转回时间戳
    return int(rounded_dt.timestamp())

if __name__ == "__main__":
    timestamp = 1529693377  # 示例的时间戳
    rounded_timestamp = round_down_timestamp_to_nearest_five_minutes(timestamp)
    print(rounded_timestamp)