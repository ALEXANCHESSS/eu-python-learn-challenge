from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating_kinopoisk(movie: dict) -> float:

            if movie["country"].count(",") >= 1 and movie["rating_kinopoisk"]:
                return float(movie["rating_kinopoisk"])
            else:
                return None

        list_rating = list(filter(None, map(get_rating_kinopoisk, list_of_movies)))
        return sum(list_rating) / len(list_rating)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def u_letter_count(movie: dict, rating: Union[float, int] = rating) -> int:
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating:
                count: int = movie["name"].count("и")
                return count
            return None

        result: int = sum(filter(None, map(u_letter_count, list_of_movies)))

        return result
