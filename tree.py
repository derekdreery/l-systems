import turtle as t
import re

# example curves:
# init: "F-F-F-F", mapping: "F" => "F-F+F+FF-F-F+F", delta = 90
# init: "F--F--F", mapping: "F" => "F+F--F+F", delta = 45

def draw_string(string, delta=90, d=10):
    for c in string:
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

class Tree:
    def __init__(self, rules, init=''):
        self.rules = rules
        self.init = init

    def run(self, iterations = 10):
        self.string = self.init
        for i in range(iterations):
            for (pre, post) in self.rules:
                self.string = self.string.replace(pre, post)

tree = Tree([("F", "F+F--F+F")], "F--F--F")
tree.run(4)
print(tree.string)
draw_string(tree.string, 60, 1)
