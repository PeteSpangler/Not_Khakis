#unsorted int array, all valid values between 1 and n
# where n is size of an array
# find duplicates in the array and print them to the screen
int_array = [1, 1, 2, 15, 12, 8, 2, 4, 10, 11, 32, 23, 9, 3, 6, 4, 88, 27, 54]
def dupes(int_array):
    if len(int_array) == len(set(int_array)):
        return False
    else:
        return True

z = dupes(int_array)
if z:
    print("Yes, there be dupes")
else:
    print("Nah son, no dupes")
#First thoughts, iterate over the array and search for duplicates
# create new list/array with those duplicates and print those?
# or sort the list first, then proceed? Append duplicates to a new list?