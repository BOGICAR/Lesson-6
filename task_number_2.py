# Задание №2 - сделано
import time
import datetime


def countdown(func):
    def time_1_2_3(*args, **kwargs):
        x = 3
        while x > 0:
            print(x)
            time.sleep(1)
            x -= 1
        return_value = func(*args, **kwargs)
    return time_1_2_3


@countdown
def what_time_is_it_now():
    current_datetime = datetime.datetime.now()
    current_datetime_up = current_datetime.strftime("%H:%M")
    print(current_datetime_up)
    return current_datetime_up


what_time_is_it_now()
