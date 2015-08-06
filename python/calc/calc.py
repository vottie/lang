class Calc:
    # need self.
    # occur below
    # typeError: add() takes exactly 2 arguments (3 given)
    def add(x, y):
        return x + y

c = Calc()
x = 100
y = 200
result = 0
result = c.add(x,y)
print '{0} + {1} = {2}'.format(x, y, result)
