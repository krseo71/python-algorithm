class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    #LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    #linked_list 에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index - 1)

        next_node = prev_node.next
        prev_node.next = new_node

        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next




linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6)
linked_list.print_all()

# print(linked_list.get_node(0).data)

