import turtle as t
import re

# example curves:
# init: "F-F-F-F", mapping: "F" => "F-F+F+FF-F-F+F", delta = 90
# init: "F--F--F", mapping: "F" => "F+F--F+F", delta = 45


class LSystemTree:
    def __init__(self, rules, init=''):
        self.rules = rules
        self.init = init

    def run(self, iterations = 10):
        self.string = self.init
        for i in range(iterations):
            for (pre, post) in self.rules:
                self.string = self.string.replace(pre, post)

    def draw(self, delta=90, d=10):
        for c in self.string:
            if c == 'F':
                t.forward(d)
            elif c == 'f':
                t.penup()
                t.forward(d)
                t.pendown()
            elif c == '+':
                t.left(delta)
            elif c == '-':
                t.right(delta)

tree = LSystemTree([
    ("F", "FF"),
    ("f", "ff"),
    ("D", "+FD----f++FD----f---FD----f----")
], "FD")
tree.run(4)
tree.draw(45, 5)
