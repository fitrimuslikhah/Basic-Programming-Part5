def pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    for i in range(n):
        result *= x
    return result

if __name__ == '__main__':
    print(pow(2, 3))   # 8
    print(pow(7, 2))   # 49
    print(pow(10, 5))  # 100000
    print(pow(17, 6))  # 24137569
    print(pow(5, 3))   # 125


if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125