class BSTNode:
    def __init__(self,data=None):
        self.data =data
        self.left =None
        self.right=None

    
    def add_node(self,value):
        print(self.data)
        if value == self.data:
            return
        
        #Left side check
        if value < self.data:  
            if self.left:
                self.left = self.left.add_node(value)
                
            else:
                self.left = BSTNode(value)
                print(f"{value} Added to Left")
        #right side check
        else:
            if self.right:    
                self.right = self.right.add_node(value)
                print("Added to right")
            else:
                self.right = BSTNode(value)
                print(f"{value} Added to right")
    
    def print_tree(self):
        elements=[]
        print("P :", self.left.data)
        if self.left:
            elements+= self.left.print_tree()
        
        elements.append(self.data) 

        if self.right:
            elements+= self.right.print_tree()
        
        return elements

if __name__ == "__main__":
    T = BSTNode(20)
    T.add_node(10)
    T.add_node(5)
    # T.add_node(21)
    # T.add_node(4)
    # T.add_node(6)
    # T.add_node(3)
    g=T.print_tree()    
    print(g)