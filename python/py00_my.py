print("hello world")

s= """this part up here 
this part on a lower line"""
print(s)

b = None
print(b)
#print(b + 9) error

import random
# basic syntax overview example
r = random.randint(0, 100)
while r < 85:
    if r > 70:
        print(r, ": so close!", sep=" ")
    elif r > 45: # yes, the else if syntax is odd...
        print(r, end="-")
        print(": Getting there...")
    else:
        print(f"{r}: Still so far away!")
        
    r = random.randint(0, 100)
print("OUT!")

def say_hi():
    print("Hi")
def shout(message="Hi"):
    print(message, "!", sep="")
shout()
shout("I love python")
shout(message="And keyword arguments")

print(type(shout))

#lists
list = [0,1,2,3,4,5,6,7,8,9,10]
print(list[3:])
print(list[0:3])
print(list[1:3])

#dictionaries
dict = {"key1":1, "key2":2, "key3":3}
print(dict)
if 3 in dict: #false
    print("3 is in dictionary")
if "key3" in dict:
    print("key3 is in dictionary")
#if "key3":3 in dict:
    #print("line above errors")
dict2 = {1:"bkey1", 2:"akey2", 3:"ckey3"}
print(dict2)

for k in dict2:
    print(k," = key in dict 2, value =", dict2[k])
    
for k,v in dict2.items():
    print(k," = key, value =", v)

#collection functions (not methods!)
print(len(dict2))
print(max(dict2))
print(min(dict2))
print(sorted(dict2)) #sorted by key
print(sorted(dict2.items(), key=lambda t: t[1])) #sorted by val

#generator
def enum(seq):
    n = 0
    for i in seq:
        yield n, i
        n += 1
        
for elem in enum(list):
    print(elem)

#creating a context
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("foo")