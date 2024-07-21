class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_index = 0
        self.index = -1
        self.current_iter = iter(self.list_of_list)
        return self

    def __next__(self):
        self.index += 1
        if (self.index) + 1 > len(self.list_of_list[self.list_index]):
            self.list_index += 1
            self.index = 0
        if (self.list_index) + 1 > len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.list_index][self.index]



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

