import threading as tr


def infinte_loop():
    while 1 == 1:
        pass


def my_name():
    print('_-Name-_')


t1 = tr.Thread(target=infinte_loop)
t2 = tr.Thread(target=my_name)

t1.start()
t2.start()

