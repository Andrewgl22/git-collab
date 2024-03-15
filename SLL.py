# variables
# lists and dictionaries = built in data structures

# Time and Space, Runtime and Memory

# Singly Linked List

# classes allow us to define new data structures
# methods and attributes = functions and variables


# Graphs

# Node

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_to_back(self,val):
        new_node = Node(val)
        # if list is empty, add first node as head
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        # loop through until the end of the list
        while runner.next:
            runner = runner.next
        # set the empty next attribute to the new node
        runner.next = new_node
        return self
        
SLL1 = SLL()

SLL1.add_to_back(8).add_to_back(9).add_to_back(15)
print(SLL1.head.val)
print(SLL1.head.next.val)







    


    





# node1 = Node(2)
# node1.next = Node(1)
# print(node1.next.val)














