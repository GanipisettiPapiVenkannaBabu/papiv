'''l=[1,3,8,7,9,8]
for i in range(len(l)):
    if i%2==0:
        print(i,l[i])
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2==0:    
        empty.append(l[i])
        print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0:
        print(l[i])
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    empty.append(l[i]**2)
print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2!=0:
        empty.append(i+10)
print(empty)
'''
'''
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)-1,-1,-1):
    empty.append(l[i])
print(empty)
'''
'''
n=["papi","venkanna","babu","ganipisetti"]
search=input()
for i in n:
    if i== search:
        print("avaliable")
        break
else:
        print("na")
'''
'''
n=["papi","venkanna","babu","ganipisetti"]
empty=[]
for i in n:
    empty.append(len(i))
print(empty)'''
'''
n=["papi","venkanna","babu","ganipisetti"]
i=0
d={}
while i<len(n):
    d[n[i]]=len(n[i])
    i+=1
print(d)
'''
'''
n=["papi","venkanna","babu","ganipisetti"]
empty={}
for i in range(len(n)):
    empty[n[i]]=len(n[i])
print(empty)'''




    
