import sys
from txt_reader import TxtReader
from csv_reader import CSVReader

klass = globals()['TxtReader']
obj = klass('sample.csv')
obj.parse()

