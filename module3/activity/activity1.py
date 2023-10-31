data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

def conversion(week=0):
    def cDay(day=0):
        def cHour(hour=0):
            def cMinute(minute=0):
                return (week * 7 * 24 * 60) + (day * 24 * 60) + (hour * 60) + minute
            return cMinute
        return cHour
    return cDay

def splitData(data):
    totalMinute = []
    for dt in data:
        dataSplit = dt.split(" ")
        
        week = int(dataSplit[0])
        day = int(dataSplit[2])
        hour = int(dataSplit[4])
        minute = int(dataSplit[6])

        conversionResult = conversion(week)(day)(hour)(minute)
        totalMinute.append(conversionResult)
    return totalMinute

print(splitData(data))