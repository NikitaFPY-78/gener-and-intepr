import types

def flat_generator(list_of_lists):
    main_coursor = 0
    while main_coursor < len(list_of_lists):
        nested_coursor = 0
        # print(main_coursor)
        while nested_coursor < len(list_of_lists[main_coursor]):
            # print (main_coursor, nested_coursor)
            yield list_of_lists[main_coursor][nested_coursor]
            nested_coursor += 1
        main_coursor += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    dlina = 0
    for i in list_of_lists_1:
        dlina = dlina + len(i)

    item = 0
    gen = flat_generator(list_of_lists_1)
    while item < dlina:
        print(next(gen))
        item += 1

    test_2()