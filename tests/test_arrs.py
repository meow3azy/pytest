from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([1, 2, 3], 3, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == 3
    assert arrs.get([1, 2, 3], -3, "test") == 1
    assert arrs.get([1, 2, 3], 2) == 3
    assert arrs.get([1, 2, 3], -4) is None
    assert arrs.get([], 0) is None


    def test_negative_index():
        assert arrs.get([1, 2, 3], -1) == 3
        assert arrs.get([1, 2, 3], -2) == 2
        assert arrs.get([1, 2, 3], -3) == 1
        assert arrs.get([], -1) == None
        assert arrs.get([], -2) == None
        assert arrs.get([], -3) == None


def test_slice():
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([1, 2, 3, 4], -2, None) == [3, 4]
        assert arrs.my_slice([1, 2, 3, 4], None, -1) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
        assert arrs.my_slice([], 0, 3) == []
        assert arrs.my_slice([1, 2, 3, 4], 0, 10) == [1, 2, 3, 4]
        assert arrs.my_slice([1, 2, 3, 4], 1, 1) == [2]


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """
    if 0 <= index < len(array):
        return array[index]
    return default
