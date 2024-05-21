class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1  # курсор списка вложенного в основной список
        return self

    def __next__(self):

        # увеличиваем nested_list_cursor
        self.nested_list_cursor+=1

        # если nested_list_cursor больше длины списка вложенного
        if self.nested_list_cursor >= len(self.main_list[self.main_list_cursor]):
            # увеличиваем main_list_cursor
            self.main_list_cursor+=1
            # сбрасываем nested_list_cursor
            self.nested_list_cursor = 0

        # если main_list_cursor больше длины основного списка

        if self.main_list_cursor >= len(self.main_list):
            raise StopIteration

        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()