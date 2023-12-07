def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# High Order Function
dgn = perkalian(5)
resultHOF = dgn(3)
print("HOF: ", resultHOF)

# Currying
resultCurrying = perkalian(2)(5)
print("Currying: ", resultCurrying)