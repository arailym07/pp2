
#Python builtin functions exercises
# 1
from functools import reduce

numbers = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print("1. Product of all numbers:", result)


# 2
text = "Hello World!"
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())

print("2. Uppercase letters:", upper)
print("   Lowercase letters:", lower)


# 3
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

string = "Madam"
print("3. Is palindrome:", is_palindrome(string))


# 4
import time
import math

num = 25100
milliseconds = 2123

time.sleep(milliseconds / 1000)  # ждем 2123 миллисекунд (2.123 секунды)
result = math.sqrt(num)

print(f"4. Square root of {num} after {milliseconds} miliseconds is {result}")

# 5
t = (True, 1, "Hello", 3.5)
print("5. All elements are true:", all(t))




# Python Directories and Files exercises

import os
import shutil
import string

# 1
path = "."  # текущая папка
print("1. List in path:", path)

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all_items = os.listdir(path)

print("   Directories:", directories)
print("   Files:", files)
print("   All items:", all_items)
print("-" * 60)


# 2
print("2. Check path access:")
path = "."  # текущая директория

print("   Exists:", os.access(path, os.F_OK))  # существует ли путь
print("   Readable:", os.access(path, os.R_OK))  # можно ли читать
print("   Writable:", os.access(path, os.W_OK))  # можно ли записывать
print("   Executable:", os.access(path, os.X_OK))  # можно ли выполнять
print("-" * 60)


# 3
print("3. Test path:")
path = __file__  # текущий файл (можно заменить на любой путь)

if os.path.exists(path):
    print("   Path exists!")
    print("   File name:", os.path.basename(path))
    print("   Directory:", os.path.dirname(path))
else:
    print("   Path does not exist.")
print("-" * 60)


# 4
print("4. Count lines in a file:")
file_path = "example.txt"
# создаем примерный файл
with open(file_path, "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

with open(file_path, "r") as f:
    line_count = sum(1 for _ in f)
print(f"   Number of lines in {file_path}: {line_count}")
print("-" * 60)


# 5
print("5. Write list to file:")
my_list = ["apple", "banana", "cherry"]

with open("list.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")

print("   List written to list.txt")
print("-" * 60)


# 6
print("6. Generate A–Z files:")
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")
print("   26 files created!")
print("-" * 60)


# 7
print("7. Copy file contents:")
source = "example.txt"
destination = "example_copy.txt"

shutil.copy(source, destination)
print(f"   File copied from {source} to {destination}")
print("-" * 60)


# 8
print("8. Delete file safely:")
delete_path = "example_copy.txt"

if os.path.exists(delete_path):
    if os.access(delete_path, os.W_OK):
        os.remove(delete_path)
        print(f"   File '{delete_path}' deleted successfully.")
    else:
        print("   No permission to delete the file.")
else:
    print("   File does not exist.")
print("-" * 60)
