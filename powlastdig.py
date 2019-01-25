def last_digit(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    if n1 == 1:
        return n2
    if n2 == 1:
        return n1
    powers = []
    while True:
        for i in range(1, 1000):
            n = n1 ** i
            b = str(n)
            if int(b[len(b) - 1]) in powers:
                break
            else:
                powers.append(int(b[len(b) - 1]))
        break
    y = n2 % len(powers) 
    
    return powers[y - 1]
print(last_digit(2, 2))