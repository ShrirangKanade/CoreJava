class ManageHeir():
    def __init__(self,name,designation):
        self.name =name
        self.designation = designation
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

    def printtree(self,format):
        
        if format:
            lvl = lambda node : node.getlevel()
            prefix = "|__"
            if format == "Name":
                spaces = lvl(self)*" "+ prefix  + self.name
            elif format == "Designation":
                spaces = lvl(self)*" "+ prefix  + self.designation
            elif format == "Both":
                spaces = lvl(self)*" "+ prefix  + self.name + " "+"(" + self.designation + ")"
            else:
                spaces = lvl(self)*" "+ prefix  + self.name     
            print(spaces)
            if self.children:
                for child in self.children:
                        child.printtree(format)

# def TreeCreate(class_name):
#     while a := input("Wanna enter a node?") != "NO":
#         name = input("Enter the name  : ")
#         designation = input("Enter designation : ")
#         new_object = class_name(name,designation)
#         print("object created")
#         node_type = input("Is it a child/parent : ")
         
if __name__ == "__main__":
    # rootx = ManageHeir("a","b")
    assign = lambda name,designation : ManageHeir(name,designation)
    print(type(assign))
    
    root = assign("Nilpul", "CEO")
    # print(type(root))
    root_child1 = assign("Chinmay","CTO")
    root_child2 = assign("Gels","HR Head")

    child1_child_1 = assign("Vishwa","Infrastructure Head")
    child_1_child__1=assign("Dhaval","Cloud Manager")
    child_1_child__2=assign("Abhijit","App Manager")

    child2_child_1 = assign("Peter","Recruitment Manager")
    child2_child_2 = assign("Waqas","Policy Manager")    
    #Tree Creation
    root.addchild(root_child1)
    root.addchild(root_child2)

    root_child1.addchild(child1_child_1)
    child1_child_1.addchild(child_1_child__1)
    child1_child_1.addchild(child_1_child__2)

    root_child2.addchild(child2_child_1)
    root_child2.addchild(child2_child_2)

    root.printtree("Designation")
# a = input("Here : ")
# print(a)