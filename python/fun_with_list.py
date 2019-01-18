new_list = []

for x in range(10):
    new_list.append(x)

print(new_list)

new_list = []
for x in range(10):
    x = x**2
    new_list.append(x)

print(new_list)

print( [x for x in range(10)])
print( [x**2 for x in range(10)])

for x in range(10):
    if x> 3:
        x = x ** 2
        new_list.append(x)

print(new_list)

print( [x**2 for x in range(10) if x >3])

def power2(x):
    return x**2

def greater3(x):
    if x>3:
        return True
    else:
        return False
       
print( list(map(power2, range(10))))
print( list(filter(greater3, range(10))))
print( list(map(power2, filter(greater3, range(10)))))

print(list(map(lambda x : x **2, range(10))))
