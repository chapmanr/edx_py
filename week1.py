n=12
if n%2 == 0:
  print("even")
else:
  print("odd")

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear]=="friendly":
        print("Hello, "+bear+" bear!")
    else:
        print("odd")
n=12
is_prime = True
for i in range(2,n):
   if n%i == 0:
     is_prime=False
print(is_prime)

n=100
number_of_times = 0
while n >= 1:
   n //= 2
   number_of_times += 1
print(number_of_times)


sum_val=[i**2 for i in range(3)]
print(sum_val)
sum_val=sum([i for i in range(10) if i%2!=0])
print(sum_val)


F = open("input.txt", "w") 
F.write("Hello\nWorld") 
F.close() 
lines = [] 
for line in open("input.txt"): 
    lines.append(line.strip()) 
print(lines) 


def modify(mylist): 
    mylist[0] *= 10 
    return(mylist) 
L = [1, 3, 5, 7, 9] 
M = modify(L) 
print(M is L)


def is_vowel(letter):
   if type(letter) == int:
        letter = str(letter)
   if letter in "aeiouy":
     return(True)
   else:
     return(False)

import random
alphanumerics = "abcdefghijklmnopqrtsuvwxyz"

for i in range(10):
    choice = random.choice(alphanumerics)
    print(choice, is_vowel(choice))

print("4 ", is_vowel(4))


def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N *= i
     return(N)

for x in range(10):
    print("fac ", x, " = ", factorial(x))