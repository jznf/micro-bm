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


def read_stuff():
    with open('stuff.txt', 'r') as stuff:
        read_stuff = stuff.readline()
        print(read_stuff[:20])
        print(read_stuff[-20:])


if __name__ == '__main__':
    print(timeit.timeit("add_stuff()", setup="from __main__ import add_stuff", number=1))
    print(timeit.timeit("write_stuff()", setup="from __main__ import write_stuff", number=1))
    print(timeit.timeit("read_stuff()", setup="from __main__ import read_stuff", number=1))