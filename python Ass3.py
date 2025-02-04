month_number = int(input("Enter the month: "))
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
if 1 <= month_number <= 12:
    print(f"Month {month_number} is {months[month_number - 1]}")
else:
    print("Invalid month number!")



age = int(input("Enter your age: "))
if age < 16:
    price = 6 / 2
elif age >= 60:
    price = 6 / 3
else:
    price = 6
print(f"Your ticket costs £{price:.2f}")





weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are in the 'underweight' range.")
elif 18.5 <= bmi <= 24.9:
    print("You are in the 'normal' range.")
elif 25 <= bmi <= 29.9:
    print("You are in the 'overweight' range.")
else:
    print("You are in the 'obese' range.")




 num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")


num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")



num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print(f"The reversed number is: {reverse}")
 


num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
multiples = []
for i in range(1, limit + 1):
    if i % num == 0:
        multiples.append(i)
print(f"Multiples of {num} up to {limit}: {multiples}")




while True:
    value = input("Enter a value: ")
    if value == 'done':
        print("Done")
        break
    print(value)
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()