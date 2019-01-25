def is_merge(s, part1, part2):
    if part1 + part2 == s:
        return True
    s1 = list(map(str, s))
    if len(s) != len(part1) + len(part2):
        return False
    s2 = [None] * len(s)
    for i in range(len(s1)):
        for j in range(len(part1)):
            if  s1[i] == part1[j]:
                s2[i] = part1[j]
                s1[i] = -1
        for k in range(len(part2)):
            if s1[i] == part2[k]:
                s2[i] = part2[k]
                s1[i] = -1
    for n in s2:
        if n == None:
            return False
    s_s2 = ''.join(s2)
    if s_s2 == s:
        return True
    else:
        return False
    return False
print(is_merge('codewars', 'cwdr', 'oeas'))