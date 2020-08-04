# # does initial setup and returns and iterator object(calls__next()___)
# __iter__()

# # return the next value in the sequence
# __next__()

# # Any object with an __iter__ and __next__ is iterable

import random

# pick 6 random numbers, make sure there are no duplicates
class LotterMachine:
    def __iter__(self):
        self.numbers = []
        return self

    def __next__(self):
        # We only want 6 numbers
        if len(self.numbers) == 6:
            raise StopIteration
        else:
            number = random.randint(1, 49)
            # make sure we don't get duplicates 
            # (if we do we get None - so a While loop might be better than a For to avoid duplicates)
            if number not in self.numbers:
                self.numbers.append(number)
                return number


machine = LotterMachine()
# it has an iter and next so we can loop through it
for number in machine:
    print(number)

# What would have been the next number of our lottery machine
next_value = next(iter(machine))
print("The next number will be " + str(next_value)