from flask import Flask
from flask import request, jsonify, Response
from typing import Optional, Tuple


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    users: dict[str, dict[str, Optional[int]]] = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post("/user")
        def create_user() -> Tuple[Response, int]:
            data: dict = request.get_json()
            if "name" not in data:
                return jsonify({"errors": {"name": "This field is required"}}), 422

            FlaskExercise.create_user(data["name"])
            return jsonify({"data": f"User {data['name']} is created!"}), 201

        @app.get("/user/<string:name>")
        def get_user(name: str) -> Tuple[Response, int]:
            result = FlaskExercise.user_exists(name)
            if not result:
                return jsonify({}), 404

            return jsonify({"data": f"My name is {name}"}), 200

        @app.route("/user/<string:name>", methods=["PATCH"])
        def update_user(name: str) -> Tuple[Response, int]:
            data: dict = request.get_json()
            new_name: str = data["name"]
            FlaskExercise.update_user(name, new_name)
            return jsonify({"data": f"My name is {new_name}"}), 200

        @app.delete("/user/<string:name>")
        def delete_user(name: str) -> Tuple[str, int]:
            result = FlaskExercise.delete_user(name)
            if not result:
                return "", 404

            return "", 204

    @classmethod
    def create_user(cls, name: str, age: Optional[int] = None) -> None:
        if name not in cls.users:
            cls.users[name] = {"age": age}

    @classmethod
    def user_exists(cls, name: str) -> bool:
        return name in cls.users

    @classmethod
    def update_user(cls, old_name: str, new_name: str, age: Optional[int] = None) -> None:
        if old_name in cls.users:
            cls.users[old_name]["age"] = age
            cls.users[new_name] = cls.users[old_name]
            del cls.users[old_name]

    @classmethod
    def delete_user(cls, name: str) -> bool:
        if name not in cls.users:
            return False

        del cls.users[name]
        return True
