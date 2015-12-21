def baseN(number, base):
    result = 0
    iterator = int(number**(float(1.0/base)))
    while iterator >= 0 :
        result += (number / (base ** iterator)) * 10 ** (iterator)
        number = number % base ** iterator
        iterator -=1
    return result

print baseN(9,2) # 101
print baseN(9,4)
print baseN(17, 10)
print baseN(42,4)
