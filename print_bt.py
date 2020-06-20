class Node():
    """docstring for BTNode."""

    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None

class BT():
    """docstring for ."""

    def __init__(self):
        self.root = None
        self.list1=[]

    def add_node(self,data):
        # pass
    # def add_node(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insert_recur(self.root,data)

    def insert_recur(self,current_node,data):
        if data <= current_node.data:
            if current_node.left==None:
                current_node.left=Node(data)
            else:
                self.insert_recur(current_node.left,data)
        elif data > current_node.data:
            if current_node.right==None:
                current_node.right=Node(data)
            else:
                self.insert_recur(current_node.right,data)

    def print_bt(self):
        if self.root:
            self.print_pre_recur(self.root)
        print(self.list1)
        self.list1.clear()

        if self.root:
            self.print_inord_recur(self.root)
        print(self.list1)
        self.list1.clear()

        if self.root:
            self.print_post_recur(self.root)
        print(self.list1)


    def print_pre_recur(self,nd):
        if not nd:
            return
        self.list1.append(nd.data) #preorder
        self.print_pre_recur(nd.left)
        self.print_pre_recur(nd.right)

    def print_inord_recur(self,nd):
        if not nd:
            return
        self.print_inord_recur(nd.left)
        self.list1.append(nd.data)
        self.print_inord_recur(nd.right)

    def print_post_recur(self,nd):
        if not nd:
            return
        self.print_post_recur(nd.left)
        self.print_post_recur(nd.right)
        self.list1.append(nd.data)


def main():
    b1=BT()
    b1.add_node(5)
    b1.add_node(7)
    b1.add_node(6)
    b1.add_node(2)
    b1.add_node(4)
    b1.add_node(3)
    b1.print_bt()

if __name__ == '__main__':
    main()
