def generator_ganjil(input):
    for i in range(input):
        if i % 2 == 1:
            yield 1

ganjil = generator_ganjil(50)
print(next(ganjil))