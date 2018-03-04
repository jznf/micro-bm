import timeit
import uuid


def add_stuff():
    x = 1
    for i in range(10**7):
        x = i + x


def write_stuff():
    with open('stuff.txt', '+w') as stuff:
        stuff_to_write = ''
        for i in range(10**6):
            stuff_to_write += str(uuid.uuid4())
        stuff.write(stuff_to_write)


def write_stuff_usb():
    with open('/Volumes/2GB/stuff.txt', '+w') as stuff:
        stuff_to_write = ''
        for i in range(10**6):
            stuff_to_write += str(uuid.uuid4())
        stuff.write(stuff_to_write)


def read_stuff():
    with open('stuff.txt', 'r') as stuff:
        stuff_to_read = stuff.readline()


def read_stuff_usb():
    with open('/Volumes/2GB/stuff.txt', 'r') as stuff:
        stuff_to_read = stuff.readline()


if __name__ == '__main__':
    add_time = timeit.timeit("add_stuff()", setup="from __main__ import add_stuff", number=1)
    write_time = timeit.timeit("write_stuff()", setup="from __main__ import write_stuff", number=1)
    write_time_usb = timeit.timeit("write_stuff_usb()", setup="from __main__ import write_stuff_usb", number=1)
    read_time = timeit.timeit("read_stuff()", setup="from __main__ import read_stuff", number=1)
    read_time_usb = timeit.timeit("read_stuff_usb()", setup="from __main__ import read_stuff_usb", number=1)

    print('add_time: {} means {}'.format(add_time, add_time / 0.6363586450024741))
    print('write_time: {} means {}'.format(write_time, write_time / 9.470535683998605))
    print('write_time_usb: {} means {}'.format(write_time_usb, write_time_usb / 14.60818093099806))
    print('read_time: {} means {}'.format(read_time, read_time / 0.07656324999697972))
    print('read_time_usb: {} means {}'.format(read_time_usb, read_time_usb / 0.059092697003507055))
