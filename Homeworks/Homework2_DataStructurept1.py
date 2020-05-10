# What I want you to work on from here to Sunday is 
# learn how to create basic data structures in Python. 
# I want you to use classes, and start with the following:

# 1) A class called IntNode, which holds an int value 
# and a pointer to another IntNode.
class IntNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# 2) A class called IntList, which has two pointers to IntNodes,
# one called head, and another one called tail. 
# Also, I want IntList to have the following methods:
# Size(), which returns an int with the amount of nodes in the list.
# Insert(int value) which inserts the value at the end of the list.
# Contains(int value) which returns true or false depending on whether
#  the value is contained in the list or not.
# Delete(int position) which deletes the value at the specified position.
# Get(int position) which returns the int value at the specified position.
class IntList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def insert(self, new_data):
        new_IntNode = IntNode(new_data)
        if self.head is None:
            self.head = new_IntNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_IntNode

    def Contains(self, x):
        current = self.head
        while current != None:
            if current.data ==x:
                return True
            current = current.next
        return False

    def Delete(self, position):
        if self.head ==None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next



# 3) Finally, a small program that inserts values 5,3,6 and 5 into your list, 
# and then iterates with a loop to extract the values and print them on screen.

# After you're done with this, let me know and send me a link to the python file(s) 
# in GitHub so I can take a look and then we can talk about small algorithms and
#  more complex data structures to play with.