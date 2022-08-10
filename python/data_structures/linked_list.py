class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None



class LinkedList:
    """
    Create a Linked List class with an insert, includes and 'to string' methods
    """

    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, value):

        #Create a new node
        newNode = Node(value)

        #If there is a node already with the head value, set the next value to the new node
        if (self.head):
            current = self.head #head attribute value
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            #Otherwise give the new node the "head" attribute
            self.head = newNode


    def __str__(self):
        #return self.data
        try:
            return self.value
        except (AttributeError):
            return 'NULL'

class TargetError:
    pass
