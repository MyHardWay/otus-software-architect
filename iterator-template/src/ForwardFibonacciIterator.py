from IFibonacciIterator import IFibonacciIterator


class ForwardFibonachiIterator(IFibonacciIterator):

    def __init__(self, value):
        self.counter = value
        self.cur_fib = 0
        self.next_fib = 1
        self.first_iter = 0

    def is_last(self):
        return True if self.counter == 0 else False

    def __next__(self):
        if self.is_last():
            raise StopIteration()
        if self.first_iter == 0:
            self.first_iter = 1
            return 0
        self.counter -= 1
        next_fib = self.cur_fib + self.next_fib
        self.cur_fib = self.next_fib
        self.next_fib = next_fib
        return self.cur_fib

