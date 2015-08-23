from component import Component

class MyList:
    def __init__(self):
        a = Component(1, 'foo')
        b = Component(2, 'bar')
        c = Component(3, 'baz')
        self.x = [a, b, c]

    def show(self):
        for i in self.x:
            print('Component id({0}), name({1})'.format(i.id, i.name))

    def find(self, target):
        for i in self.x:
            if i.id == target:
                print('Component id({0}), name({1})'.format(i.id, i.name))

    def add(self, val):
        c = Component(4, val)
        self.x.append(c)
        #self.show()

    def delete(self, val):
        for i in self.x:
            if i.name == val:
                print('Component delete. id({0}), name({1})'.format(i.id, i.name))
                self.x.remove(i)
                #self.show()

    def update(self, val, up_val):
        for i in self.x:
            if i.name == val:
                prev = i.name
                i.name = up_val
                print('Component id({0}), name({1})->({2})'.format(i.id, prev, i.name))
        #self.show()
