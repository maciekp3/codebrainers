#!/usr/bin/env python3

# tree = """          *
#             ***
#            *****
#           *******
#          *********
#         *********** """

# text = "ala ma kota\na kot ma ale"

#print(text)
#print(tree)

# for i in range(30):
#     for j in range(-30, 30):
#         if i > abs(j):
#           print("J", end = '')
#         else:
#             print(" ", end = '')
#     print()

# def add(a, b):
#     c = a + b
#     return c 

def choinka():
    for i in range(6):
        for j in range(-6, 6):
            if i > abs(j):
                print("*", end = '')
            else:
                print(" ", end = '')
        print()

# for x in range(10):
#    choinka(x)


# def my_range(stop):
#     i = 0
#     lrange = []
#     while i < stop:
#         #print(i)
#         lrange.append(i)
#         i += 1
#     return lrange

# print(my_range(10))

# for i in my_range(10):
#     print(i)

def my_range(start=0, stop=10, step=1):
    lrange = []
    if step <=0:
        return lrange
    while start < stop:
        #print(i)
        lrange.append(start)
        start += step
    return lrange

#print(my_range(0, 10, 1))

def anyarg(*args, **kwargs):
    print(args)
    print(kwargs)

def only_named(**kwargs):
    print(kwargs)

def proper_range(*args, **kwargs):
    print(args, kwargs)
    if len(args) == 1:
        return my_range(0, args[0])
    elif len(args) == 2:
        return my_range(args[0], args[1])
    elif len(args) == 3:
        return my_range(args[0], args[1], args[2])
    else:
        return my_range(kwargs['start'], kwargs['stop'], kwargs['step'])

def proper_range_star(*args, **kwargs):
    print(args, kwargs)
    if len(args) == 1:
        return my_range(0, args[0])
    elif 1 < len(args) < 4:
        return my_range(*args)

def proper_range_star2(*args, **kwargs):
    print(args, kwargs)
    if len(args) == 1 and len(kwargs) == 0:
        return my_range(0, args[0])
    else:
        return my_range(*args, **kwargs)
    




print(proper_range(10))
print(proper_range(2, 10))
print(proper_range(1, 12, 2))
print(proper_range(start=1, stop=12, step=2))

