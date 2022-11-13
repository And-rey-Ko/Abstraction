# Домашнее задание к уроку 8. Абстракции, объекты и классы.
import random

q = [{
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}]

""" Создаем класс Question для вопроса """


class Question:

    def __init__(self, question, complication, answer, points, is_question=False, user_answer=None):
        self.question = question
        self.complication = complication
        self.answer = answer
        self.points = points
        self.user_answer = user_answer

    def __repr__(self):
        return f"{self.question}, {self.complication}, {self.answer}, {self.points}, {self.user_answer}"

    """Возвращает вопрос в понятном пользователю виде, например:
       Вопрос: What do people often call American flag?
       Сложность 4/5
    """

    def build_question(self):
        return self.question

    """Возвращает int, количество баллов.
       Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """

    def get_points(self):
        return int(self.points)

    """Возвращает True, если ответ пользователя совпадает 
       с верным ответом иначе False.
    """

    def is_correct(self):
        return self.answer == self.user_answer

    """Возвращает в случае верного ответа :
       Ответ верный, получено __ баллов
       Возвращает в случае неверного ответа :
       Ответ неверный, верный ответ __
    """

    def build_feedback(self):
        if self.answer == self.user_answer:
            return f"Ответ верный, получено {self.points} баллов"
        else:
            return f"Ответ неверный, верный ответ {self.answer}"


"""Считывает вопросы и раскладывает в экземпляры класса Question. Все экземпляры складываются в список questions."""


def create_list_objects(q):
    return [Question(u["q"], u["d"], u["a"], int(u["d"]) * 10) for u in q]


"""Выводит статистику на основе списка questions."""


def get_statistics(q):
    points = 0
    count = 0
    amount = len(questions)
    for question in questions:
        if question.is_correct():
            points += question.get_points()
            count += 1
    return (f"Вот и все!" +
            f"\nОтвечено {count} вопросов из {amount}" +
            f"\nНабрано {points} баллов")


questions = create_list_objects(q)
print("Игра начинается!")
random.shuffle(questions)
for question in questions:
    print(question.build_question())
    print(f"Сложность {round(question.get_points() / 10)}/5")
    user_answer = input()
    question.user_answer = user_answer
    if question.is_correct():
        print(question.build_feedback())
    else:
        print(question.build_feedback())
print(' ')
print(get_statistics(questions))