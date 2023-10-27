class LocationTree():
    def __init__(self,location):
        self.location = location

        self.children = []
        self.parent = None
    
    def addchild(self,child):
        child.parent = self
        self.children.append(child)

    def getlevel(self):
        count=0
        p = self.parent
        while p:
            count+=1
            p = p.parent
           
        return count

        # def print_tree(self, property_name):
        #     if property_name == 'both':
        #         value = self.name + " (" + self.designation + ")"
        #     elif property_name == 'name':
        #         value = self.name
        #     else:
        #         value = self.designation

        #     spaces = ' ' * self.get_level() * 3
        #     prefix = spaces + "|__" if self.parent else ""
        #     print(prefix + value)
        #     if self.children:
        #         for child in self.children:
        #             child.print_tree(property_name)
        
    def printtree(self,level):
            
            spaces = " " *self.getlevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix+ self.location)
            if self.children:
                for child in self.children:
                    if child.getlevel()<=level:
                        child.printtree(level)

# def TreeCreate(class_name):
#     while a := input("Wanna enter a node?") != "NO":
#         name = input("Enter the name  : ")
#         designation = input("Enter designation : ")
#         new_object = class_name(name,designation)
#         print("object created")
#         node_type = input("Is it a child/parent : ")
def buildtree():
    assign = lambda location: LocationTree(location)

    root = assign("Global")
    # print(type(root))
    root_child1 = assign("India")
    root_child2 = assign("Usa")

    child1_child_1 = assign("Gujarat")
    child_1_child__1=assign("Baroda")
    child_1_child__2=assign("Gandhianagar")

    child2_child_1 = assign("California")
    child_1_child__11= assign("San Francisco")   
    child_1_child__22=assign("Palo ALto")
    #Tree Creation
    root.addchild(root_child1)
    root.addchild(root_child2)

    root_child1.addchild(child1_child_1)
    child1_child_1.addchild(child_1_child__1)
    child1_child_1.addchild(child_1_child__2)

    root_child2.addchild(child2_child_1)
    child2_child_1.addchild(child_1_child__11)
    child2_child_1.addchild(child_1_child__22)

    
    return root      
if __name__ == "__main__": 
    root = buildtree()
    root.printtree(1)
    root.printtree(2)
    root.printtree(3)