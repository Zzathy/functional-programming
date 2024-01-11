ganjil = [i for i in range(50) if i % 2 == 1]

filter_result = filter(lambda num: num % 3 == 0, ganjil)

print(list(filter_result))