import sys

#klass = globals()['TxtReader']
#obj = klass('sample.csv')
#obj.parse()

mod = __import__('txt_reader',fromlist=['TxtReader'])
klass = getattr(mod, 'TxtReader')
obj = klass('sample.txt')

mod = __import__('csv_reader',fromlist=['CSVReader'])
klass = getattr(mod, 'CSVReader')
obj = klass('sample.csv')
obj.parse()
