class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None


def insert(prev_node, new_data):
    # listning ixtiyoriy nuqtasiga element qo'shish
    if prev_node is None:
        print("Error")
    # yangi element qo'shamiz
    new_node = Node(new_data)
    # yangi tugunni keyingi elementga bog'laymiz
    new_node.next = prev_node.next
    # avvalgi tugunni yangi elementga bog'laymiz
    prev_node.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


l_list = LinkedList()
a = Node(15)
b = Node(20)
c = Node(30)
d = Node(40)
j = Node(21)

l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = j



#print(f"Dastlabki holat :{l_list.printList()}")
#l_list.push(15)
#print(f"Keyingi holat :{l_list.printList()}")
#print(f"Dastlabki holat :{l_list.printList()}")
#l_list.append(15)
#print(f"Keyingi holat :{l_list.printList()}")






