
# Python iterators and generators

# 1
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2


# 2
def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


# 3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


# 5
def countdown(n):
    for i in range(n, -1, -1):  # от n до 0 включительно
        yield i



# Python date

# 1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date after subtracting 5 days:", new_date)


# 2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Without microseconds:", no_microseconds)


# 4
from datetime import datetime

# Пример: две даты
date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 9, 12, 5, 30)

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)



# Python Math library

# 1
import math

degree = float(input("Input degree: "))
radian = degree * math.pi / 180

print("Output radian: {:.6f}".format(radian))


# 2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) / 2) * height

print("Expected Output:", area)


# 3
import math

n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

area = (n * a ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)


# 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)

