def fibo(num):
    sumOfnums = 0
    if num >= 2:
        sumOfnums = fibo(num - 1) + fibo(num - 2)
        print(sumOfnums)
    elif num >= 0:
        sumOfnums = num
    return sumOfnums


def fiboNonRecursive(num):
    var1 = 0
    var2 = 1
    result = 0
    print(var1)
    print(var2)
    while(num != 0):
        result = var1 + var2
        print(result)
        var1 = var2
        var2 = result
        num -= 1
    pass


def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """
    fiboNonRecursive(4)

if __name__ == '__main__':
    main()