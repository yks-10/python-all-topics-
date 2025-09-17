# 1. Variables & data type

roll_no = 12        # int
average = 97.9      # float
complex_a = 2+5j    # complex - real imag
print(complex_a.real)
print(complex_a.imag)

name = "Yogesh"     # string
name_size = len(name) # len() method
print(name_size)
print(name.upper())
print(name.lower())
print(name.title())
print(name.islower())
print(name.isupper())
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())
print(name.isspace())
print(name.isnumeric())
print(name.capitalize())
print(name.casefold())
print(name.swapcase())
print(name.__len__())
print(name.count('Y'))
print(name.__contains__('Y'))
print(name.__eq__("Yogesh"))
print(name.__ge__("Yogesh"))

#  bollen
value = None
if value:
    print("Yes")
else:
    print("No")

# type casting
value = "55678"
print(value)
print(int(value))
print(float(value))
print(list(value))
print(tuple(value))
print("".join(set(value)))

# operators
ramu, somu = 0,0
ramu +=2
somu += 3
somu = ramu-somu
print(somu, ramu)
print(0*5)
print(0**5)
print("0^5", 0^5)
print(0%5)
print(0//5)
print(11/5)
print(11//5)

# assignment operator
x,y = 5, 4
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
x+=1
y-=1
print("x is",x,"y is",y)
print(f"y is {y}")
x%=y
print(x)
x/=y
print(y)

# membership operator | in
nick_name, name = "yks", "yogesh"
print(nick_name in name)
print(nick_name not in name)

# identity operator
# is checks the memory  == checks the values

print("IDENTITY")
x = 4
y=4
x1 = x
y1 = 4
print(x is x1)
print(x is y)
print(x is not y1)
print(x==y1)

# input
# name = input("What is your name?")
# mark = int(input("What is your mark?"))
# list_mark = list(map(int, input().split()))
# print(list_mark)

x = 2
print(f"value is {x:.10f}")

# conditional statement

x, y = 2, 4
if x==y:
    print("YES")
elif x!=y:
    print("NO")
else:
    print("YES")

# looping
# for while | break, continue, pass
print([ i for i in range(10) ])

while x!=y:
    print(x)
    x+= 1

# data structure
roll_no =[1,2,3,3,] # list
print(roll_no)

roll_no.append(7)
roll_no.sort()
print(roll_no)
roll_no.extend([1,2,3,4,5,6])
print(roll_no)
print(sorted(roll_no))
print(roll_no.index(7))
print(7 in roll_no)
print(roll_no.count(7))
print(set(roll_no))
roll_tuple = (1,2,3,4) # tuple
roll_set = {1,2,3,4}
roll_dict ={"abi":1,"bay":2,"cat":3}
print(roll_dict.values())
print(roll_dict.items())
print(list(roll_dict.keys()))


# Function

def add(a=20,b=10):
    return a+b
print(add(1,2))
print(add(2))


def subtract(*args):
    return args[0]-args[1]
print(subtract(2,2))

def multiply(**kwargs):
    return kwargs['x']*kwargs['y']
print(multiply(x=10,y=10))


def add(x,y,**kwargs):
    return x+y+kwargs['x1']
print(add(1,2,x1=2000))


def validation(x):
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x<=0:
        raise ValueError("x must be positive")
    return x

try:
    validation(5)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("Yey")
finally:
    print("Yey")


