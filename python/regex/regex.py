import re

class RegEx:
    def __init__(self, str_):
        #print('Regex')
        self.string = str_

    def search(self):
        p = re.compile('[a-z]+')
        m = p.match(self.string)
        if m:
            print('match found:',m.group())
        else:
            print('no match')

