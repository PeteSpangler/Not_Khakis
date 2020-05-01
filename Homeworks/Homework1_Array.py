#unsorted int array, all valid values between 1 and n
# where n is size of an array
# find duplicates in the array and print them to the screen
int_array = [1, 1, 2, 15, 12, 8, 2, 4, 10, 11, 18, 17, 9, 3, 6, 4, 5, 9, 16] #random int array I came up with?

#So if there are duplicates, below is a method to create list removing those duplicates
#Complexity: time  O(N + Log(N)), space O(n)
def no_dupes(int_array):
    nodupe = []
    for u in int_array:
        if u not in nodupe:
            nodupe.append(u)
    return nodupe

q = no_dupes(int_array)

#Complexity: time: O(Log (n^2)), space O(1)
#iterate over original list and list without duplicates 
def dupelist(int_array):
    copylist = int_array.copy()
    for k in set(copylist):
        if k in copylist:
            copylist.remove(k)
    return copylist

p = dupelist(int_array)


print(p)

#time: O(N^2), space O(N)
#Goal
#time O(N), space O(1)
#1. for time you do one pass through the array


scratchpad = [0] * len(int_array)
print (scratchpad)

for num in int_array:
    if (scratchpad[num - 1] != 0):
        print (num)
    scratchpad[num - 1] = 1 # marking num as seen

#scratchpad is a true false test
#encode the int array so it fits the problem?
#try to solve without using scratchpad