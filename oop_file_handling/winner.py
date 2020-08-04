import csv

class Winner:
    def __init__(self, index, year, age, name, movie):
        self.index = int(index)
        self.year = int(year)
        self.age = int(age)
        self.name = name
        self.movie = movie
    
    def values(self):
        return [self.index, self.year, self.age, self.name, self.movie]

winners = []

# only read "r", as csvfile is giving it an alias just like "as" in SQL
with open("oscars.csv", "r") as csvfile:
    # use next to skip the first line that has metadata we don't want eg "name", "age", "year"
    next(csvfile)
    # skipinitialspace strip out whitespace
    reader = csv.reader(csvfile, skipinitialspace=True)

    # for row in reader:
    #     #print(row)
    #     current_winner = Winner(row[0], row[1],row[2],row[3],row[4])
    #     winners.append(current_winner)

    for row in reader:
        # deconstruct with * then it doesn't matter how many rows we deal with
        current_winner = Winner(*row)
        winners.append(current_winner)
    
# for winner in winners:
#     print(f"{winner.name} won the Oscar for {winner.movie} in {winner.year} at {winner.age}")

# with open("oscars.csv") as csvfile:
#     reader = csv.reader(csvfile)
#     # give me 1 number for row in reader
#     count = sum(1 for row in reader)
#     #print("Number of rows: " + str(count))

# # a for append (add stuff)
# with open("oscars.csv","a") as csvfile:
#     # quoting is a keyword
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#     winner = Winner(count, 2020, 50, "Renne Zellweger", "Judy")
#     # writer.writerow([winner.index, winner.year, winner.age, winner.name, winner.movie])
#     writer.writerow(winner.values())

# always read "r" before write, "w"
with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in winners:
        # make winners a bit older
        winner.age += 1
        writer.writerow(winner.values())