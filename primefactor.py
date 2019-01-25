def primeFactors(n):
    divider = 2
    result = n
    dividers = []
    ntimes = []
    count = 1
    while divider <= n:
        if result % divider == 0:
            result = result / divider
            if divider in dividers:
                count += 1
            else:
                ntimes.append(count)
                count = 1
                dividers.append(divider)
        else:
            divider += 1
        if result == 1:
            break
    outpt = []
    for j in range(len(dividers)):
        if j == len(dividers) - 1:
            if ntimes[0] == 1:
                s = f'({dividers[j]})'
            else:
                f'({dividers[j]}**{ntimes[0]})'
        elif ntimes[j + 1] != 1:
            s = f'({dividers[j]}**{ntimes[j + 1]})'
        else:
            s = f'({dividers[j]})'
        outpt.append(s)
    print(ntimes)
    out = ''.join(outpt)
    return out

a = primeFactors(7775460)
print(a)