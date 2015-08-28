class TxtReader:
    def __init__(self, f):
        self.f = f

    def parse(self):
        file = open(self.f)
        line = file.readline()
        
        while line:
            print(line)
            line = file.readline()
        file.close

#t = TxtReader('sample.txt')
#t.parse()
