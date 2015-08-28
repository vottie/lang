import csv

class CSVReader:
    def __init__(self, f):
        self.f = f

    def parse(self):
        with open(self.f, 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                print(row)


