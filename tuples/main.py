# Tuple: ordered, immutable, allows duplication elements

# Create a tuple
mytuple =  (1, "hello", True) # or mytuple = 1, "hello", True

# Create a tuple from a list
secondtuple = tuple([1, 3, 4])
print(secondtuple)

# count 
first_tuple = ('a', 'p', 'p', 'l', 'e')
print(first_tuple.count('p'))

# get the index
print(first_tuple.index('p'))

# unpacking
#my_tuple = "Naruto", 17, "Konoha"

#name, age, city =  my_tuple
#print("Name: {}, Age: {}, City: {} ".format(name, age, city))

# unpacking using * 
t = (0, 1, 2, 3, 4, 5)

i1, *i2,i3 =  t
print(i1)
print(i3)
print(i2)

# compare lists with tuple
import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")