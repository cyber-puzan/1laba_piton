n = int(input("введите натуральное число: "))
sum = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum += digit
    n //= 10
if sum > 0:
    print("сумма нечетных чисел = ", sum)
else:
    print("в числе нет нечетных чисел.")

