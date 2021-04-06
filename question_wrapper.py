from shapes import *
from displaying import display

questions = []


def question(func):
    def wrapper():
        reset_shapes()
        func()

    questions.append((func.__name__, wrapper))


def run_all_questions(require_input: bool = False):
    for name, question in questions:
        print(name)
        question()
        display(shapes)
        print("-" * 40)
        if require_input:
            if len(input()) > 0:
                return
