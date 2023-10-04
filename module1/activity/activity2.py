random_list = [10, 3.1, "Hello", 7, "Python", 2.7, "World", 412, 5.5, "AI", 70]

float_tuple = ()
string_list = []
int_dict = {}

for index in random_list:
    if type(index) == float:
        float_tuple += (index,)
    elif type(index) == str:
        string_list.append(index)
    elif type(index) == int:
        satuan = index & 10
        puluhan = (index // 10) % 10
        ratusan = index // 100

        int_dict[index] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}

print(float_tuple)
print (string_list)
print(int_dict)