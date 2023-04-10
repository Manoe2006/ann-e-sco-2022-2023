def binary_to_decimal(binary_num):
    decimal_num = 0
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[i]) * 2**(len(binary_num)-i-1)
    return decimal_num

print(binary_to_decimal('10111'))
