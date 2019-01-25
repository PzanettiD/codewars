def countBits(n):
    return "{0:b}".format(n).count('1')
print(countBits(1234))