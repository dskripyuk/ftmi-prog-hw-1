def reverse_number(n):
    reversed_num = 0
    while n != 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num
number = int(input("Введите число: "))
reversed_number = reverse_number(number)
print(reversed_number)

# Your code here (づ๑•ᴗ•๑)づ♡