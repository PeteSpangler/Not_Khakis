#unsorted int array, all valid values between 1 and n
# where n is size of an array
# find duplicates in the array and print them to the screen
int_array = [1, 1, 2, 15, 12, 8, 2, 88, 6, 32, 23, 4, 10, 11, 32, 23, 9, 3, 6, 4, 88, 27, 54] #random int array I came up with?
#check if there are duplicates in list by comparing length of list vs length of list as set
def dupes(int_array):
    if len(int_array) == len(set(int_array)):
        return False
    else:
        return True

x = dupes(int_array)

if x:
    print("Yes, there be dupes")
else:
    print("Nah son, no dupes")

#So if there are duplicates, below is a method to create list removing those duplicates
def no_dupes(int_array):
    nodupe = []
    for u in int_array:
        if u not in nodupe:
            nodupe.append(u)
    return nodupe

q = no_dupes(int_array)

#iterate over original list and list without duplicates 
def dupelist(int_array, q):
    for k in q:
        if k in int_array:
            int_array.remove(k)
    return int_array

p = dupelist(int_array, q)


print(p)