from functools import reduce

b=[10,20,19,11,51,69]
c=reduce(lambda x,y : x+y,b)
print(c)

d=reduce(lambda x,y : x-y,b)
print(d)


e=reduce(lambda x,y : x/y,b)
print(e)

d=reduce(lambda x,y : x*y,b)
print(d)