class EvenNumbers:
    """Class for interator of pair numbers"""

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


class FibonacciIter:
    """Class for iterator of Fibonacci succession"""

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2

        self.next = self.n1 + self.n2
        self.n1, self.n2 = self.n2, self.next

        if not self.max or not self.n2 >= self.max:
            self.counter += 1
            return self.next
        else:
            raise StopIteration


if __name__ == "__main__":
    # evens = EvenNumbers(2)
    # for even in evens:
    #     print(even)

    fibos = FibonacciIter(30)
    last = 0
    for fibo in fibos:
        # if last == fibo:
        #     print("yes", fibo)
        print(fibo)
        # last = fibo
