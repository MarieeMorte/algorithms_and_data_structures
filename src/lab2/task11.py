class Node:
    __slots__ = ('key', 'left', 'right', 'height')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))


def get_balance(node):
    return get_height(node.right) - get_height(node.left) if node else 0


def rotate_left(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    update_height(x)
    update_height(y)

    return y


def rotate_right(x):
    y = x.left
    temp = y.right

    y.right = x
    x.left = temp

    update_height(x)
    update_height(y)

    return y


def balance_tree(node):
    if not node:
        return node

    update_height(node)
    balance_factor = get_balance(node)

    if balance_factor > 1:
        if get_balance(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if balance_factor < -1:
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

    def exists(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def next(self, key):
        result = None
        current = self.root

        while current:
            if current.key > key:
                result = current.key
                current = current.left
            else:
                current = current.right

        return result

    def prev(self, key):
        result = None
        current = self.root

        while current:
            if current.key < key:
                result = current.key
                current = current.right
            else:
                current = current.left

        return result


def solve():
    tree = AVLTree()
    output = []

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            op = parts[0]
            x = int(parts[1])

            if op == 'insert':
                tree.root = tree.insert(tree.root, x)
            elif op == 'delete':
                tree.root = tree.delete(tree.root, x)
            elif op == 'exists':
                output.append('true' if tree.exists(x) else 'false')
            elif op == 'next':
                res = tree.next(x)
                output.append(str(res) if res is not None else 'none')
            elif op == 'prev':
                res = tree.prev(x)
                output.append(str(res) if res is not None else 'none')

    with open('output.txt', 'w') as f:
        f.write('\n'.join(output))


if __name__ == '__main__':
    solve()
