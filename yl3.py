def Fibonacci(n):  #Arvutab n-nda Fibonacci numbri rekursiivselt
    if n <= 0:
        return 0  #kui n on 0, tagastab 0
    elif n == 1:
        return 1  #kui n on 1 annab 1, sequence algab 1st
    elif n == 2:
        return 1  #siin -> F(2) = 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)  #kui on muu siis teeb selle arvutuse

print(Fibonacci(10))