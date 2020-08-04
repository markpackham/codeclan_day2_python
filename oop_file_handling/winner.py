import csv

class Winner:
    def __init__(self, index, year, age, name, movie):
        self.index = int(index)
        self.year = int(year)
        self.age = int(age)
        self.name = name
        self.movie = movie

winners = []

# only read "r", as csvfile is giving it an alias just like "as" in SQL
with open("oscars.csv", "r") as csvfile:
    # use next to skip the first line that has metadata we don't want eg "name", "age", "year"
    next(csvfile)
    # skipinitialspace strip out whitespace
    reader = csv.reader(csvfile, skipinitialspace=True)

    for row in reader:
        print(row)