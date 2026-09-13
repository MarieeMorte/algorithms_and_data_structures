class Node:
    __slots__ = ('key', 'left', 'right', 'parent', 'sum')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.sum = key


def get_sum(node):
    return node.sum if node else 0


def update_sum(node):
    if node:
        node.sum = node.key + get_sum(node.left) + get_sum(node.right)


def is_left_child(node):
    return node.parent and node.parent.left == node


def is_right_child(node):
    return node.parent and node.parent.right == node


def rotate(x):
    p = x.parent
    g = p.parent

    if is_left_child(x):
        p.left = x.right
        if x.right:
            x.right.parent = p
        x.right = p
    else:
        p.right = x.left
        if x.left:
            x.left.parent = p
        x.left = p

    p.parent = x
    x.parent = g

    if g:
        if g.left == p:
            g.left = x
        else:
            g.right = x

    update_sum(p)
    update_sum(x)


class SplayTree:
    def __init__(self):
        self.root = None

    def splay(self, x):
        while x.parent:
            p = x.parent
            g = p.parent

            if g:
                if is_left_child(x) == is_left_child(p):
                    rotate(p)
                else:
                    rotate(x)

            rotate(x)

        self.root = x

    def find(self, key):
        if not self.root:
            return None

        current = self.root
        last = None

        while current:
            last = current
            if key == current.key:
                self.splay(current)
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        if last:
            self.splay(last)
        return None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        if self.find(key):
            return

        current = self.root
        parent = None

        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node = Node(key)
        new_node.parent = parent

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.splay(new_node)

    def delete(self, key):
        if not self.find(key):
            return

        node = self.root

        left = node.left
        right = node.right

        if left:
            left.parent = None
        if right:
            right.parent = None

        if not left:
            self.root = right
        else:
            max_left = left
            while max_left.right:
                max_left = max_left.right

            self.splay(max_left)
            self.root = max_left
            self.root.right = right
            if right:
                right.parent = self.root
            update_sum(self.root)

    def sum_range(self, l, r):
        if l > r:
            return 0

        if not self.root:
            return 0

        if not self.find(l):
            pass

        left, right = self.split(self.root, l)

        mid, right2 = self.split(right, r + 1) if right else (None, None)

        result = get_sum(mid)

        self.root = self.merge(self.merge(left, mid), right2)

        return result

    def split(self, node, key):
        if not node:
            return None, None

        current = node
        last = None

        while current:
            last = current
            if current.key >= key:
                current = current.left
            else:
                current = current.right

        if not last:
            return None, node

        self.splay(last)

        if last.key >= key:
            left = last.left
            if left:
                left.parent = None
            last.left = None
            update_sum(last)
            return left, last
        else:
            right = last.right
            if right:
                right.parent = None
            last.right = None
            update_sum(last)
            return last, right

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        max_left = left
        while max_left.right:
            max_left = max_left.right

        self.splay(max_left)
        max_left.right = right
        right.parent = max_left
        update_sum(max_left)

        return max_left


def solve():
    tree = SplayTree()
    output = []
    mod = 1000000001
    x = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    if not lines:
        return

    n = int(lines[0].strip())

    for i in range(1, n + 1):
        parts = lines[i].strip().split()
        if not parts:
            continue

        op = parts[0]

        if op == '+':
            key = (int(parts[1]) + x) % mod
            tree.insert(key)
        elif op == '-':
            key = (int(parts[1]) + x) % mod
            tree.delete(key)
        elif op == '?':
            key = (int(parts[1]) + x) % mod
            found = tree.find(key) is not None
            output.append('Found' if found else 'Not found')
        elif op == 's':
            l = (int(parts[1]) + x) % mod
            r = (int(parts[2]) + x) % mod
            if l > r:
                l, r = r, l
            result = tree.sum_range(l, r)
            output.append(str(result))
            x = result

    with open('output.txt', 'w') as f:
        f.write('\n'.join(output))


if __name__ == '__main__':
    solve()
