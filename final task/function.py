def is_prima(input):
    divide1 = input / 1
    divideself = input / input
    if divide1 == input and divideself == 1:
        return True
    else:
        return False

print(is_prima(4))

err