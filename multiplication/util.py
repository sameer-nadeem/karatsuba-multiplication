from math import floor


def add(x, y):
    if(not isBigInt(x) and not isBigInt(y)):
        return str(int(x) + int(y))

    lx = len(x)
    ly = len(y)
    n = lx
    if(ly > lx):
        x = x.zfill(ly)
        n = ly
    if(lx > ly):
        y = y.zfill(lx)
        n = lx

    result = ''
    r = 0
    q = 0
    for i in range(n - 1, -1, -1):
        val = int(x[i]) + int(y[i]) + q
        r = int(val % 10)
        q = floor(val / 10)
        if i == 0:
            result = str(val) + result
            break
        result = str(r) + result

    return result


def isBigInt(x):
    x = int(x)
    if x.bit_length() <= 64:
        return False
    return True


def isGreater(x, y):
    if(len(x) > len(y)):
        return True
    if(len(x) < len(y)):
        return False

    for i in range(len(x)):
        if(int(x[i]) > int(y[i])):
            return True
        if(int(x[i]) < int(y[i])):
            return False

    return False


def sub(x, y):
    if(not isGreater(x, y)):
        t = x
        x = y
        y = t

    lx = len(x)
    ly = len(y)

    n = lx
    if(ly > lx):
        x = x.zfill(ly)
        n = ly
    if(lx > ly):
        y = y.zfill(lx)
        n = lx

    result = ''
    carry = 0

    for i in range(n-1, -1, -1):
        val = int(x[i]) - int(y[i]) - carry
        carry = 0

        if val < 0:
            val = val + 10
            carry = 1

        result = str(val) + result

    return str(int(result))


def xpower10(x, y):
    x = str(x)
    if not isBigInt(x):
        return str(int(x)*(10**y))

    return x.ljust(len(x) + y, '0')
