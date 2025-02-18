class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def binary_search(key, node: Node):
    if node is None:
        return None
    if node.data == key:
        return node
    if node.data < key:
        binary_search(key, node.left)
    else:
        binary_search(key, node.right)

def insert(key, node: Node):
    s = node
    x = None
    while s is not None:
        x = s
        if key < x.data:
            s = s.left
        else:
            s = s.right
    if key < s.data:
        x.left = Node(key)
    else:
        x.right = Node(key)
    return

if __name__ == 'main':
    node = None
    insert(30,node)