def timeformat(seconds):
    minutes = 0
    hours = 0
    if seconds / 60 >= 1:
        for i in range(0, seconds, 60):
            if seconds - 60 < 0:
                break
            else:
                minutes += 1
                seconds -= 60
            if minutes == 60:
                hours += 1
                minutes = 0
            
    s = [str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2)]
    outpt = ':'.join(s)
    return outpt

print(timeformat(86399))
print(timeformat(86399))
print(timeformat(86399))
print(timeformat(86399))
print(timeformat(86399))