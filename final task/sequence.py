items = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

numbers = []
strings = []

for x in items:
    if type(x) is int:
        numbers.append(x)
    elif type(x) is str:
        strings.append(x)

def combine(numbers, strings):
    products = {}

    for x in range(3):
        products[strings[x]] = numbers[x]

    return products

print(combine(numbers, strings))