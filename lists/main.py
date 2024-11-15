# Lists : Ordered, mutable , allow duplicate elements, different data type

mylist = [ "Banana", "Apple", "Cherry"]
print(mylist)

mylist2 = [5, True, "hello"]
print(mylist2)

# Iterate over a list
for i in mylist:
    print(i)

# Check if a element is in a list
if "Banana" in mylist:
    print("yes")
else:
    print("no")

# add element to list
mylist.append("Orange")
print(mylist)

# remove the last element
mylist2.pop()
print(mylist2)

# remove an element using its value
mylist.remove("Apple")
print(mylist)

# slicing [start:end:step]
#print(mylist[1:2])

# Copy one list to another
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org.copy()
print(list_cpy)

# list comprehension :  [ expression  for i in range ]
first_list =  [1, 2 , 3, 4, 5]
second_list = [ i*i for i in first_list]
print(first_list)
print(second_list)