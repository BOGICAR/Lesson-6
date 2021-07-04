# Задание №4 - сделано
import json
import datetime


def time_delta(sec):
    sec_to_time = datetime.timedelta(seconds=sec)
    return sec_to_time


with open('acdc.json', 'r') as f:
    file_dict = json.load(f)
    piece_of_information = file_dict['album']['tracks']['track']


def task_4(piece_of_information):
    list_4 = []
    for track in piece_of_information:
        for i in track:
            list_4.append(int(track.get('duration')))
            break
    sum_list_4 = sum(list_4)
    return sum_list_4


print('Amount of second: ', task_4(piece_of_information))
print('Album time: ', str(time_delta(task_4(piece_of_information))))
