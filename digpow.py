# Is there an integer k 
# such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# n * k = t_sum
def digpow(n, p):
    number = list(map(int, str(n)))
    t_sum = 0
    for i in range(len(number)):
        number[i] = number[i] ** (p + i)
        t_sum += number[i]
    k = t_sum / int(n)
    k = int(k)
    if k * int(n) != t_sum:
        return -1
    else:
        return k
    return k
print(digpow(92, 1))