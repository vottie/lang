class Calc:
    # need self.
    # occur below
    # typeError: add() takes exactly 2 arguments (3 given)
    def add(self, x, y):
        if not isinstance(x, int):
            raise TypeError("%r: integer expected" %  (x))
        if not isinstance(y, int):
            raise TypeError("%r: integer expected" %  (y))
        return x + y

