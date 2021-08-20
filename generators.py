def my_gen():
    """An generator example"""

    print("Hi there!")
    n = 0
    yield n

    print("Hi there 2 !")
    n = 1
    yield n

    print("Hi there 3!")
    n = 3
    yield n


axel = my_gen()

# print(next(axel))  # 'Hi there!'
# print(next(axel))  # 'Hi there 2!'
# print(next(axel))  # 'Hi there 3!'
# print(next(axel))  # StopIteration


# this_list = [0, 1, 2, 3, 4, 5]
# second_gen = [x ** 2 for x in this_list]
# print(second_gen)


def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    while not max or n2 < max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2

        next = n1 + n2
        n1, n2 = n2, next
        counter += 1
        yield n1


# fibos = fibo_gen(10)
# for fibo in fibos:
#     print(fibo)


def fibo_gen_two(max=None):
    n1, n2 = 0, 1
    while n2 < max:
        n1, n2 = n2, n1 + n2
        yield n1


# fibos = fibo_gen_two(10)
# for fibo in fibos:
#     print(fibo)


def a_gen(arr):
    for i in arr:
        yield i ** 2


# a_list = [0, 1, 3, 4]
# this_gen = a_gen(a_list)
# for item in this_gen:
#     print(item)


def b_gen(max=None):
    n = 0
    counter = 0
    while not max or n < max:
        yield n
        n = counter ** 2
        counter += 1


# this_gen = b_gen(5)
# for item in this_gen:
#     print(item)


def c_gen(max=None):
    n = 0
    while n ** 2 < max:
        yield n ** 2
        n += 1


this_gen = c_gen(10)
for item in this_gen:
    print(item)
