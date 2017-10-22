# coding=utf-8
"""
    本程序使用Python实现二叉搜索树。
"""


class Node(object):
    """节点结构"""

    def __init__(self, data):
        self.lchild = None
        self.rchild = None
        self.data = data

    def insert(self, data):
        """
            插入节点。
        """
        if data < self.data:
            if not self.lchild:
                self.lchild = Node(data)
            else:
                self.lchild.insert(data)
        elif data > self.data:
            if not self.rchild:
                self.rchild = Node(data)
            else:
                self.rchild.insert(data)

    def lookup(self, data, parent=None):
        """
            查找节点。
        """
        if data < self.data:
            if not self.lchild:
                return None, None
            return self.lchild.lookup(data, self)
        elif data > self.data:
            if not self.rchild:
                return None, None
            return self.rchild.lookup(data, self)
        else:
            return self, parent

    def child_count(self):
        """
            统计子节点个数。
        """
        count = 0
        if self.lchild:
            count += 1
        if self.rchild:
            count += 1
        return count

    def delete(self, data):
        """
            删除节点。
        """
        node, parent = self.lookup(data)

        if node:
            child_count = self.child_count()
            if child_count == 0:
                # 如果该节点没有子节点，则可直接删除该节点
                if parent.lchild is node:
                    parent.lchild = None
                else:
                    parent.rchild = None
                del node
            elif child_count == 1:
                # 如果只有一个子节点，则让子节点替换该节点，该节点删除
                node_child = None
                if node.lchild:
                    node_child = node.lchild
                else:
                    node_child = node.rchild

                if parent:
                    if parent.lchild is node:
                        parent.lchild = node_child
                    else:
                        parent.rchild = node_child
                del node
            else:
                # 如果有两个子节点，则要判断节点下所有叶子
                parent = node
                successor = node.rchild
                while successor.lchild:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.lchild == successor:
                    parent.lchild = successor.rchild
                else:
                    parent.rchild = successor.rchild

    def compare(self, node):
        """
            比较两颗树。
        """
        if not node:
            return False
        if self.data != node.data:
            return False

        res = True
        if not self.lchild:
            if node.lchild:
                return False
        else:
            res = self.lchild.compare(node.lchild)

        if not res:
            return False
        if not self.rchild:
            if node.rchild:
                return False
        else:
            res = self.rchild.compare(node.rchild)

        return res

    def print_tree(self):
        """
            按顺序打印树。
        """
        if self.lchild:
            self.lchild.print_tree()

        print(self.data)

        if self.rchild:
            self.rchild.print_tree()

    def tree_data(self):
        """
            二叉树数据结构。
        """
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                # yiled node.data
                node = node.rchild


if __name__ == '__main__':
    root = Node(10)
    root.insert(3)
    root.insert(7)
    root.insert(11)

    root.print_tree()
    node, parent = root.lookup(3)
    print(node.data, parent.data)

    root.delete(10)
    root.print_tree()
