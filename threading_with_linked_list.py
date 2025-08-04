# Define a class called Node to represent a node in a linked list
import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(f"Data {current.data} printed from thread {threading.current_thread().name}")
            current = current.next

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            current = self.head
            prev = None
            while current:
                if current.data != data:
                    prev = current
                    current = current.next
                else:
                    prev.next = current.next
                    return


def check_linkedlist(l1):
    ll = LinkedList()
    for l in l1:
        ll.insert(l)
    ll.display()


l1=[234, 42, 545, 12, 6346, 232, 74, 745, 465, 121, 764, 56, 678, 783, 82, 56, 239]
l2=[334,534, 535, 6456, 2342, 754, 6456, 2342, 656, 232, 745754, 3534, 757, 8568, 3252, 64574, 745, 745, 3523, 532525]
l3=[5345, 536, 456, 8678, 2347, 96795, 2326, 9784, 75675, 1241, 12545, 567, 858679, 56858, 4574, 5685, 323, 23525]
l4=[868, 6783, 789346, 56867, 56856, 121, 6796, 2352, 547, 667976, 697698, 67967, 2352, 2352, 7979, 235295, 5623]

# check_linkedlist(l1)


tr1 = threading.Thread(target=check_linkedlist, args=(l1,))
tr2 = threading.Thread(target=check_linkedlist, args=(l2,))
tr3 = threading.Thread(target=check_linkedlist, args=(l3,))
tr4 = threading.Thread(target=check_linkedlist, args=(l4,))
tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()







# ll.insert(2)
# ll.insert(3)
# ll.insert(4)
# ll.insert(5)
# ll.insert(6)
# ll.insert(7)
# ll.insert(8)
# ll.insert(9)
# ll.display()
# print("Deleting element 4")
# ll.delete(4)
# print("Updated List")
# ll.display()
# ll.delete(23)
# ll.insert(23)
# ll.display()