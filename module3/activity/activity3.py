random_list = [10, 3.1, "Hello", 7, "Python", 2.7, "World", 412, 5.5, "AI", 70]

def map_integer(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda value: isinstance(value, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

def printHasilFloat(float_values):    
    return f"Data Float : {tuple(float_values)}"
    
def printHasilString(string_values):
    return f"Data String : {[s for s in string_values if s.isalpha()]} "

def main():
    print(printHasilFloat(float_values))
    
    print("Data Int : ")
    for result in map(map_integer, int_values):
        print(result)

    print(printHasilString(string_values))
    
if __name__ == "__main__":
    main()