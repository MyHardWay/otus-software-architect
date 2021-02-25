class FibonacciCollection(object):
    def __init__(self, iterator, sequence):
        self.sequence = sequence
        self.iterator = iterator(sequence)

    def __iter__(self):
        return self.iterator

