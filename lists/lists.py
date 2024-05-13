class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list):
            max: int = input_list[0]
        else:
            return input_list

        result_list: list[int] = []

        for element in input_list[1:]:
            if element > max:
                max = element

        for element in input_list:
            if element >= 0:
                result_list.append(max)
            else:
                result_list.append(element)
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
        high: int = len(input_list) - 1

        def start_search(low: int, high: int) -> int:
            if low > high:
                return -1

            mid: int = (low + high) // 2

            if input_list[mid] == query:
                return mid
            if input_list[mid] < query:
                low = mid + 1
                return start_search(low, high)
            else:
                high = mid - 1
                return start_search(low, high)

        return start_search(low, high)
