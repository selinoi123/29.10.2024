# question_num_1

#START

number: float = float(input("Enter a number : "))

if number > 10:
    difference: float = number - 10
    print(f"The difference between number {number} and the number 10 is :{difference} ")
else:
    multiplies: float = 10 * number
    print(f"The multiplies between number {number} and the number 10 is :{multiplies} ")

#END

# question_num_2

#START

number_one: int = int(input("Enter a numbers : "))
number_two: int = int(input("Enter a number : "))
number_three: int = int(input("Enter a number : "))

sum_number: int = number_one + number_two + number_three

if sum_number > 100:
    print(f"The sum of the numbers is : {sum_number}")
else:
    print(f"The amount {sum_number} is less than 100")

#END

# question_num_3

#START

number_1: float = float(input("Enter the first decimal number: "))
number_2: float = float(input("Enter the second decimal number: "))

fraction1 = number_1 - int(number_1)
fraction2 = number_2 - int(number_2)

if fraction1 > fraction2:
    print(fraction1)
elif fraction1 < fraction2:
    print(fraction2)
else:
    print("Equal")

#END

# question_num_4

#START

age: int = int(input("Enter your age (Less than 120 and more than 0): "))

if 0 < age < 120 :
    print(age)
else:
    print("Invalid age ")

#END

# question_num_5

#START

number: int = int(input("Enter a number with three digits : "))

Second_digit: int = number // 10 % 10

print(Second_digit)

#END

# question_num_6

#START

number: int = int(input("Enter an integer number greater than 0 : "))

for i in range(number, 0, -1):
    print(i, end=", ")


#END

# question_num_7

#START

num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2, 1):
    if i % 2 == 0:
        print(i, end=", ")
#END

# question_num_8

#START

number: int = int(input("Enter a number: "))

for i in range(1, number + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=", ")

#END

# question_num_9

#START

number: int = int(input("Enter a number: "))

for i in range(1, number + 1):
    if i % 7 == 0 :
        print(i, end=", ")

#END

# question_num_11

#START

array_numbers: list[int] = []
num = -1

while num != 0:
    num = int(input("Enter a numbers : "))
    if num < 0 :
        array_numbers.append(num)

print(sum(array_numbers))

#END

# question_num_12

#START

array_numbers: list[int] = []   # 1
temp = 0

for i in range(4):
    num = int(input("Enter a ten numbers : "))
    array_numbers.append(num)
print(array_numbers)

for i in range(0, len(array_numbers)//2):
   temp = array_numbers[i]
   array_numbers[i] = array_numbers[len(array_numbers) - 1 - i]
   array_numbers[len(array_numbers) - 1 - i] = temp

print(array_numbers)

#END

# question_num_13

#START

array_numbers: list[int] = []
number = -1
count = 0

while number != 0:
    number = int(input("Enter a numbers : "))
    array_numbers.append(number)

for num in array_numbers:
    if num > 1:
        is_prime = True
        for i in range(2, 10):
            print(i)
            if num % i == 0 and num > i:
                is_prime = False
                break
        if is_prime == True:
            count += 1

print(f"You typed {count} prime numbers")

#END

# question_num_14

#START

array_numbers: list[int] = []
num = 0

for i in range(5):
    num = int(input("Enter a five numbers : "))
    array_numbers.append(num)

average: float = sum(array_numbers) / len(array_numbers)
larger_than_average: list[int] = []

for i in array_numbers:
    if i > average :
        larger_than_average.append(i)

print(f"larger than average is : {average}")
print(f"And the numbers that are bigger than the average is :{larger_than_average}.")

#END

# question_num_15

#START

num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))

count_difference  = 0

while num1 >= num2:
    num1 -= num2
    count_difference += 1

print(f"The result of the division is : {count_difference}")

#END

# question_num_16

#START

num: int = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

digit_sum = hundreds + tens + units

if digit_sum % 3 == 0:
    print("The sum of the digits is divisible by 3.")
else:
    print("The sum of the digits is not divisible by 3.")


#END

# question_num_17

#START

text = input("Enter a string: ")

reversed_text: str = ""
for i in text:
    reversed_text = i + reversed_text

if text == reversed_text:
    print(f"The string {text} is a Inverted.")
else:
    print(f"The string {text} is not a Inverted.")

#END

