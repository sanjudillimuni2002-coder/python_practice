import random

item=[None]*12
def a ():
    for i in range(12):
        item[i]=random.randint(0,1)
        print(item[i])
a()
