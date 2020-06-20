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
        if self.root!=None:
            self.add_node_recu(self.root,data)
        else:
            temp=Node(data)
            self.root=temp

    def add_node_recu(self,rtnode,data):
        if rtnode.data > data:
            if rtnode.left is None:
                temp=Node(data)
                rtnode.left=temp
            else:
                self.add_node_recu(rtnode.left,data)
        if rtnode.data < data:
            if rtnode.right is None:
                temp=Node(data)
                rtnode.right=temp
            else:
                self.add_node_recu(rtnode.right,data)


    def print_bt(self):
        if self.root:
            self.print_inord_recur(self.root)
        print(self.list1)

    def print_inord_recur(self,nd):
        if not nd:
            return
        self.print_inord_recur(nd.left)
        self.list1.append(nd.data)
        self.print_inord_recur(nd.right)



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
