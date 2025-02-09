import Spaceship


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)


    # Homework Code
    # Make sure to reuse existing function for the correct edge cases for both TODOs
    # Write appropriate test function below to test for the new functions.

    # TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
    def insert_at_index(self, index: int, value: int):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        current = self.head
        for i in range(index-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return


    # TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
    def delete_at_index(self, index: int):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            if not self.head:
                return None
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value
        current = self.head
        for i in range(index-1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        self.length -= 1
        return value

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship.Spaceship("Voyager", 300)
s2 = Spaceship.Spaceship("Enterprise", 300)
s3 = Spaceship.Spaceship("Atlantis", 300)
s4 = Spaceship.Spaceship("Challenger", 300)
s5 = Spaceship.Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
#start list is artemis, chal, voyager, enterprise, atlantis
#atlantis, from  now foes to second position
mylinkedlist.insert_at_index(2, s5)
mylinkedlist.print_list()
#deletes challenger
mylinkedlist.delete_at_index(1)
mylinkedlist.print_list()