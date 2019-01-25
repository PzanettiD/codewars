def validBraces(string):
    p = string.count('(')
    p1 = string.count(')')
    b = string.count('[')
    b1 = string.count(']')
    c = string.count('{')
    c1 = string.count('}')
    if p != p1 or b != b1 or c != c1:
        return False
    output = True
    for s in range(len(string)):
        if string[s] == '(':
            for i in range(len(string)):
                if string[i] == ')':
                    if s < i:
                        output = True
                    else:
                        output = False
        if string[s] == '[':
            for i in range(len(string)):
                if string[i] == ']':
                    if s < i:
                        output = True
                    else:
                        output = False
        if string[s] == '{':
            for i in range(len(string)):
                if string[i] == '}':
                    if s < i:
                        output = True
                    else:
                        output = False
    if output:
        return True
    else:
        return False
print(validBraces('(}{)'))