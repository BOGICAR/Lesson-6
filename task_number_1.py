# Задание №1 - сделано
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def task_1():
    new_dict = dict(zip(coin, code))
    return new_dict


print(task_1())
