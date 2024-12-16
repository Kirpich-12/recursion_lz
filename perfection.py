inp = int(input("Введите число "))

def deli(a:int, ls = None, b = 1) -> int:
    if ls is None:
        ls = []
    if b > a:
        return ls
    if a % b == 0:
        ls.append(b)
        if b * b != a:
            ls.append(a // b)
    return deli(a // b, ls, b + 1)
    
        

def divisors(n, i = 1, result=None):
    if result is None:
        result = []
    if i > n:
        return result
    if n % i == 0:
        result.append(i)
        if i * i != n:
            result.append(n // i)
    return divisors(n // i, i + 1, result)

print(deli(inp))

def perf(a:int) -> bool:
    pass
