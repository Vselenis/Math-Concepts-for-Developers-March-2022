from turtle import *


def draw_branch(branch_length, angle):
    color("brown")
    pensize(branch_length / 10)
    if branch_length > 5:
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 14, angle)
        left(2 * angle)
        draw_branch(branch_length - 14, angle)
        right(angle)
        backward(branch_length)
        color("green")
        stamp()

    if branch_length < 5:
        color("green")
        stamp()


def draw_tree(trunk_length, angle):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle)
    done()


draw_tree(100, 10)

#
# from turtle import *
#
#
# def draw_branch(branch_length, angle):
#
#     if branch_length > 5:
#         forward(branch_length)
#         right(angle)
#         draw_branch(branch_length - 14, angle)
#         left(2 * angle)
#         draw_branch(branch_length - 14, angle)
#         right(angle)
#         backward(branch_length)
#
#
#
# def draw_tree(trunk_length, angle):
#     speed("fastest")
#     left(90)
#     up()
#     backward(trunk_length)
#     down()
#     draw_branch(trunk_length, angle)
#     done()
#
#
# draw_tree(90, 90)
#


