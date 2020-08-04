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
        #print(row)
        current_winner = Winner(row[0], row[1],row[2],row[3],row[4])
        winners.append(current_winner)
    
for winner in winners:
    print(f"{winner.name} won the Oscar for {winner.movie} in {winner.year} at {winner.age}")