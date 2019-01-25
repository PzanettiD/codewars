def evenodd(numbers):
    #your code here
    numbers = list(map(int, numbers.split(" ")))
    evenC = 0
    oddC = 0
    for num in numbers:
        int(num)
        if num % 2 == 0:
            evenC += 1
        else:
            oddC += 1
    
    for n in range(len(numbers)):
        if evenC > oddC:
            if numbers[n] % 2 != 0:
                return n + 1
        else:
            if numbers[n] % 2 == 0:
                return n + 1
print(evenodd("2 4 5 6 8"))