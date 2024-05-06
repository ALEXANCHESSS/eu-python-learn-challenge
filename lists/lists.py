class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max: int = 0
        result_list: list[int] = []
        for i in input_list:
            if i > max:
                max = i
        if not max:
            return input_list
        else:
            for i in input_list:
                if i >= 0:
                    result_list.append(max)
                else:
                    result_list.append(i)
            return result_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        low: int = 0
        mid: int = len(input_list) // 2
        high: int = len(input_list) - 1

        def start_search(low: int, mid: int, high: int) -> int:
            if low > high:
                return -1
            elif input_list[mid] == query:
                return mid
            elif input_list[mid] < query:
                low = mid + 1
                mid = (low + high) // 2
                return start_search(low, mid, high)
            else:
                high = mid - 1
                mid = (low + high) // 2
                return start_search(low, mid, high)

        return start_search(low, mid, high)
