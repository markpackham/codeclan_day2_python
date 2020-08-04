def generate_evens(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            # yield lets us return more than one item & not calculate till needed LAZY evaluations
            yield i
        i += 1

# even_numbers = generate_evens(100)
# for even_number in even_numbers:
#     print(even_number)

list_of_event_numbers = list(generate_evens(100))
list_of_event_numbers.append(100000)
print(list_of_event_numbers)

# LAZY evaluations improve performances, only evaulate something when needed

# Lists (like ArrayLists) offer flexability in size however aren't great for performance
# Generators lack flexability, they have fixed sizes but they offer better performance
# Look for yield keyword to help you spot generators (although generators aren't commonly used)