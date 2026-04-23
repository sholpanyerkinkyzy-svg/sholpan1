#2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sortted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(words)
#4
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x ** 2  if x % 2 == 0 else x *3 , numbers))
print(result)
#1.6
numbers = [0, -3, 5, -7, 8]

check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
result = [check(n) for n in numbers]

print(result)

print(result)
#2.2
def filter_words(words):
    for word in words:
        if len(word) > 4:
            if "а" in word.lower():
                yield "с а"
            else:
                yield word
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)
 #2.4
def squares(n):
    for i in range(1, n + 1):
        sq = i ** 2
        if sq % 2 == 0:
            yield "чётный квадрат"
        else:
            yield sq

for x in squares(5):
    print(x)
#3.2
import math
matrix = [[1,2,3], [4,5,6], [7,8,9]]
row_products = [(lambda row: math.prod(row))(row) for row in matrix]
print(row_products)
#3.4
numbers = [1,2,3,4,5]
status_dict = {x: ("чётное" if x % 2 == 0 else "нечётное") for x in numbers}
print(status_dict)
#3.6
fizzbuzz = ["FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(1, 21)]
print(fizzbuzz)
#5.2
words = ["кот", "машина", "арбуз", "дом"]
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print(result)

#5.4
numbers = [0, 5, 12, 7, 20, -3, 8]
result = list(map(lambda x: x / 2 if x % 2 == 0 else x * 3,
                  filter(lambda x: x > 5, numbers)))

print(result)
#4.2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
process = lambda w: (w.upper() + "*" if "а" in w.lower() else w.upper()) if len(w) > 4 else "short"
result = [process(w) for w in words]
print(result)
#4.4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
result_dict = {x:("Отлично"  if scors >= 90 else : 70 <= scors <= 90
