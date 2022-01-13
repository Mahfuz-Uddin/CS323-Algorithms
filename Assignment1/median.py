l = []#Empty list
i = 0
for i in range(1,999):
    if(i%2 != 0):
        l.append(i)#Inserting odd numbers into the list
#l is a set of odd numbers from 1 thru 20001
print(l)
print("Length of list is: ",len(l))#this gives size of list
print("Median is: ",(1+999)//2)#This gives the middle number in the list