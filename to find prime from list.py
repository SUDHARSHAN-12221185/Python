arr=[9,10,7,23,8,15,17,19,30,31,71,81,91]
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False

    return True

print(list(filter(lambda x:prime(x),arr)))
