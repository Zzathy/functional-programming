data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# def splitData(data):
#     for dt in data:
#         dataSplit = dt.split(" ")

#         integers = filter(lambda i: i in dataSplit if , dataSplit)

#         if dataSplit is int:
#             return dataSplit
#         # return dataSplit
# print(splitData(data))

# for i in range(len(data)):
#     dataSplit = data[i].split(" ")

#     print(dataSplit[0])

def splitData(data):
    dts = data.split()
    integers = [str(dts[i]) for i in range(0, len(dts), 2)]
    return integers

integerValue = list(filter(None, map(splitData, data)))

def sublist():
    for sublist in integerValue:
        print(sublist)

def main():
    sublist()

if __name__ == "__main__":
    main()