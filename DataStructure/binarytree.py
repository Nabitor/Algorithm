# coding=utf-8
"""
    本程序使用Python实现基本的二叉树。
"""


class Node(object):
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchildD:\DevelopTools\Anaconda3
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            queue = []
            queue.append(self.root)

            while queue:
                node_ = queue.pop(0)
                if node_.lchild == None:
                    node_.lchild = node
                    return
                elif node_.rchild == None:
                    node_.rchild = node
                    return
                else:
                    queue.append(node_.lchild)
                    queue.append(node_.rchild)

    def pre_order_recursion(self, start):
        """
            使用递归的方式遍历。
        """
        node = start
        if node == None:
            return

        print(node.data)

        if node.lchild == None and node.rchild == None:
            return

        self.pre_order_recursion(node.lchild)
        self.pre_order_recursion(node.rchild)

    def pre_order_no_recursion(self):
        """
            使用非递归方式先序遍历。
        """
        if self.isEmpty():
            return

        stack = []
        node = self.root
        while node or stack:
            while node:
                print node.data
                stack.append(node)
                node = node.lchild

            if stack:
                node = stack.pop()
                node = node.rchild

    def in_order_recursion(self, start):
        """
            使用递归的方式中序遍历。
        """
        node = start
        if node == None:
            return

        self.in_order_recursion(node.lchild)
        print(node.data)
        self.in_order_recursion(node.rchild)

    def in_order_no_recursion(self):
        if self.isEmpty():
            return

        node = self.root
        stack = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.lchild

            if stack:
                node = stack.pop()
                print(node.data)
                node = node.rchild

    def post_order_recursion(self, start):
        node = start
        if node == None:
            return

        self.post_order_recursion(node.lchild)
        self.post_order_recursion(node.rchild)
        print(node.data)

    def post_order_no_recursion(self):
        if self.isEmpty():
            return

        node = self.root
        stack = []
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop()
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
            stack.append(node)
        while stack:
            print(stack.pop().data)

    def level_order(self):
        node = self.root
        if node == None:
            return

        queue = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)

    def isEmpty(self):
        return True if self.root.data == -1 else False


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    print(arr)

    tree = BinaryTree()
    for i in arr:
        tree.add(i)
    print("level_order:")
    tree.level_order()

    print("pre_order_recursion:")
    tree.pre_order_recursion(tree.root)

    print("pre_order_no_recursion:")
    tree.pre_order_no_recursion()

    print("in_order_recursion:")
    tree.in_order_recursion(tree.root)

    print("in_order_no_recursion:")
    tree.in_order_no_recursion()

    print("post_order_recursion:")
    tree.post_order_recursion(tree.root)

    print("post_order_no_recursion:")
    tree.post_order_no_recursion()
