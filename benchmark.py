import timeit


def test():
    x = 1
    for i in range(10**7):
        x = i + x


if __name__ == '__main__':
    print(timeit.timeit("test()", setup="from __main__ import test", number=1))