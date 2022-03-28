import sys

def my_generator(n):
    for i in range(n):
        yield i**3

values = my_generator(10)
print(type(values))


for i in range(10):
    print(next(values))

"""
The below for-loop wont print anything since we already 
consumed all values in the above loop using next.

"""
for x in values:
    print(x)


#Another Example..

def infinite_sequence():
    result = 1
    while True:
        yield result
        result += 2

values = infinite_sequence()

for i in range(10):
    print(next(values))

print("************************")

for i in range(10):
    print(next(values))
