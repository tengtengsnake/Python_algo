from array import*
x=array('i',[5,15,25,35,45])
n=x.pop() # return the last element in the array x  default value is -1
print('delete',n)
for data in x:
    print(data)
n=x.pop(2)
print('delete',n)
for data in x:
    print(data)
