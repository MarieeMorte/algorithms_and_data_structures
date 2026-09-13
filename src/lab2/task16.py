class Node:
    __slots__ = ('key', 'left', 'right', 'height', 'size')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1


def get_height(node):
    return node.height if node else 0


def get_size(node):
    return node.size if node else 0


def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))


def update_size(node):
    if node:
        node.size = 1 + get_size(node.left) + get_size(node.right)


def update_node(node):
    update_height(node)
    update_size(node)


def get_balance(node):
    return get_height(node.right) - get_height(node.left) if node else 0


def rotate_left(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    update_node(x)
    update_node(y)

    return y


def rotate_right(x):
    y = x.left
    temp = y.right

    y.right = x
    x.left = temp

    update_node(x)
    update_node(y)

    return y


def balance_tree(node):
    if not node:
        return node

    update_node(node)
    balance = get_balance(node)

    if balance > 1:
        if get_balance(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if balance < -1:
        if get_balance(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    return node


def find_min(node):
    while node.left:
        node = node.left
    return node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        return balance_tree(node)

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            successor = find_min(node.right)
            node.key = successor.key
            node.right = self.delete(node.right, successor.key)

        return balance_tree(node)

    def kth_maximum(self, k):
        current = self.root
        kth_min = get_size(self.root) - k + 1

        while current:
            left_size = get_size(current.left)

            if kth_min == left_size + 1:
                return current.key
            elif kth_min <= left_size:
                current = current.left
            else:
                kth_min -= left_size + 1
                current = current.right

        return None


def solve():
    tree = AVLTree()
    output = []

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    for i in range(1, n + 1):
        parts = lines[i].strip().split()
        if not parts:
            continue

        cmd = int(parts[0])
        key = int(parts[1])

        if cmd == 1:
            tree.root = tree.insert(tree.root, key)
        elif cmd == -1:
            tree.root = tree.delete(tree.root, key)
        elif cmd == 0:
            result = tree.kth_maximum(key)
            output.append(str(result))

    with open('output.txt', 'w') as f:
        f.write('\n'.join(output))


if __name__ == '__main__':
    solve()
