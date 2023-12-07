def uppercase_operator(function):
    def wrapper():
        func = function()
        # make_uppercase = func.upper()
        return func.upper()
    return wrapper

@uppercase_operator
def say_hi():
    return "hello there"

result = say_hi()
print(result)