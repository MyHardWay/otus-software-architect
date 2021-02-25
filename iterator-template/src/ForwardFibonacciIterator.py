from IFibonacciIterator import IFibonacciIterator


class ForwardFibonachiIterator(IFibonacciIterator):

    def __init__(self, value):
        self.last_value = value
        self.index = 0
        self.current_value = 0
        self.next_value = 1

    def is_last(self):
        return True if self.index == self.last_value else False

    def __next__(self):
        if self.current_value == 0:
            self.__fibonacci_step()
            return 0
        if self.is_last():
            raise StopIteration()
        self.__fibonacci_step()
        return self.current_value

    def __fibonacci_step(self):
        self.current_value, self.next_value = self.next_value, self.next_value + self.current_value
        self.index += 1
