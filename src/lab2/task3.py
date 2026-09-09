class Node:
    __slots__ = ('key', 'left', 'right')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    """Вставка ключа в BST (без дубликатов)"""
    if root is None:
        return Node(key)

    current = root
    while True:
        if key == current.key:
            return root
        elif key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root
            current = current.right


def find_next(root, key):
    """Поиск минимального элемента > key"""
    result = 0
    current = root

    while current is not None:
        if current.key > key:
            result = current.key
            current = current.left
        else:
            current = current.right

    return result


def main():
    root = None
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

            if op == '+':
                root = insert(root, x)
            else:
                output.append(str(find_next(root, x)))

    with open('output.txt', 'w') as f:
        f.write('\n'.join(output))


if __name__ == '__main__':
    main()
