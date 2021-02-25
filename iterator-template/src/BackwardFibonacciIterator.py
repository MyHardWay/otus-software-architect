from IFibonacciIterator import IFibonacciIterator


class BackwardFibonacciIterator(IFibonacciIterator):

    def __init__(self, value):
        self.current_value = value + 1

    def is_last(self):
        return True if self.current_value == 0 else False

    def __next__(self):
        if self.is_last():
            raise StopIteration()
        self.current_value -= 1
        return self.__calculate_binet(self.current_value)


    def __calculate_binet(self, value):
        phi = (1 + 5 ** .5) / 2
        psi = (1 - 5 ** .5) / 2
        return int((phi ** value - psi ** value) / 5 ** .5)



