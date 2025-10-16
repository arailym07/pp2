
#1
import re

pattern = r'ab*'
test_strings = ["a", "ab", "abb", "ac", "b", "aaabbb"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches ")
    else:
        print(f"'{s}' does not match ")



# 2
import re

pattern = r'ab{2,3}'
test_strings = ['a', 'abb', 'abbb', 'ac']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches ")
    else:
        print(f"'{s}' does not match")



# 3
import re

pattern = r'^[a-z]+_[a-z]+$'
test_strings = ['hello_world', 'Arailym Oralova', 'code_222', 'pp_pp']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches ")
    else:
        print(f"'{s}' does not match")



# 4
import re

pattern = r'^[A-Z][a-z]+'
text = "Hello, My name is Arailym "

# Ищем все подходящие слова
matches = re.findall(pattern, text)
print("Words that match the pattern:", matches)



# 5
import re

pattern = r'^a.*b$'    #начинается с 'a', потом любые символы, заканчивается на 'b'
test_strings = ["aab", "acb", "a123b", "ab", "bca", "abcx", "xaab"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches ")
    else:
        print(f"'{s}' does not match ")



# 6
import re

text = "Python is, an interesting.language"
# Заменяем пробелы, запятые и точки на двоеточие
result = re.sub(r'[ ,.]', ':', text)

print(result)



# 7
import re

text = "hello_world_example"
# Ищем символ "_" и букву после него и заменяем на заглавную букву
camel_case = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

print("Snake case:", text)
print("Camel case:", camel_case)



# 8
import re

text = "HelloWorldPythonProgram"

# Разбиваем строку, где встречается заглавная буква
result = re.findall(r'[A-Z][a-z]*', text)

print(result)



# 9
import re

text = "HelloWorldPythonProgram"

# Перед каждой заглавной буквой (кроме первой) вставляем пробел
result = re.sub(r'([A-Z])', r' \1', text).strip()

print(result)



# 10
import re

text = "helloWorldExample"

# Перед каждой заглавной буквой вставляем подчёркивание и делаем её маленькой
result = re.sub(r'([A-Z])', r'_\1', text).lower()

print(result)
