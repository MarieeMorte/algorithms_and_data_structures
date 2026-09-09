class Node:
    __slots__ = ('key', 'left', 'right')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key == current.key:
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def delete(self, key):
        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.key = successor.key

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def exists(self, key):
        current = self.root
        while current is not None:
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

        while current is not None:
            if current.key > key:
                result = current.key
                current = current.left
            else:
                current = current.right

        return result

    def prev(self, key):
        result = None
        current = self.root

        while current is not None:
            if current.key < key:
                result = current.key
                current = current.right
            else:
                current = current.left

        return result


def main():
    tree = BST()
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
                tree.insert(x)
            elif op == 'delete':
                tree.delete(x)
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
    main()
