# In python, functions are first class objects 
# so you can pass them around in variables like in JavaScript with callbacks
# Higher order functions are simple functions that takes in or returns a function

# def say_hello():
#     return "Hello World"

# # Do not do this if you are putting a funciton into a variable, () eg say_hello()
# saved_funciton = say_hello

# # prints Hello World
# print(saved_funciton())
# # prints the function itself eg <function say_hello at 0x10343b280>
# print(saved_funciton)


# def outer_function():
#     def inner_function():
#         print("Hello from the inside!")    
#     inner_function()

# outer_function()
# # can't call inner function directly (as close as we get to a private function in python)



# def ordinary():
#     print("I am an ordinary function")

# def meow():
#     print("Meow meow meow")

# def make_pretty(callback):
#     def wrapper():
#         print("I am decorated now!")
#         callback()
#     return wrapper

# pretty = make_pretty(ordinary)
# pretty_random = make_pretty(meow)

# print("Run ordinary()")
# ordinary()
# print("Run pretty()")
# pretty()
# print("Run pretty_random()")
# pretty_random()


# Use of decorator (works like annotations in Java that use @)
def make_pretty(callback):
    def wrapper():
        name = "Mark"
        print("I am decorated now!")
        callback(name)
    return wrapper

def do_twice(callback):
    def wrapper():
        callback() #ordinary()
        callback() #ordinary()
    return wrapper

# The annotator @
@do_twice
@make_pretty # == decorated_ordinary = make_pretty(ordinary)
def ordinary(name):
    print(f"The hidden name is {name}") # grab name from make_pretty's callback
    print("I am an ordinary function")

# Outputs
# I am decorated now!
# The hidden name is Mark
# I am an ordinary function
ordinary()