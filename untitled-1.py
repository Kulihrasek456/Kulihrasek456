def toBinary(num):
    cache = []
    if num == 1:
        cache.append(1)
        A = len(cache) -1
        for i in range(len(cache)):
            print(cache[A])
            A-=1
    else:
        cache.append(num%2)
        num=num/2
        toBinary(num)

print(toBinary(18))
    
    