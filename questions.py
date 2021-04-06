from question_wrapper import question
from shapes import *

# View questions in ./questions.pdf


@question
def q1():
    rect(0, 0, 0.75, 0.5)


@question
def q2():
    tri(0, 0, 0.5, 1, UP | RIGHT)


@question
def q3_add():
    rect(0, 0, 5, 3)
    rect(0.5, 3, 2, 6)
    rect(0, 9, 5, 2)


@question
def q3_sub():
    rect(0, 0, 5, 11)
    irect(0, 3, 0.5, 6)
    irect(2.5, 3, 2.5, 6)


@question
def q4():
    rect(0, 0, 1.5, 4)
    semi(2, 4, 2, UP)


@question
def q5():
    rect(0, 0, 5, 3)
    semi(2.5, 3, 2.5, UP)


@question
def q6():
    rect(0, 0, 2, 2)
    isemi(1, 2, 0.625, DOWN)
    irect(1, 0, 0.75, 0.5)
