def sisagold(a,operasi, b):
    return operasi(a, b)

def kurang(a, b):
    return a - b

print(sisagold(9, kurang, 7))