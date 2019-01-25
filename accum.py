def accum(s):
    # your code
    text = []
    for i in range(len(s)):
        temp = s[i] * (i + 1)
        text.append(temp.capitalize())
    new_s = '-'.join(text)
    return new_s

b = accum('abcd')
print(b)