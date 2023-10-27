class Node():
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None

    def length(self):
        count=0
        itr = self.head
        while itr:
            count+= 1
            itr = itr.next
        return count

    def insert_at_beginning(self,data):
        node = Node(str(data),next=self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

        print("Item inserted at the end of the list")
    
    def insert_values(self,data_list):
        self.head =None
        for data in data_list:
            self.insert_at_end(data)

    def insert_between(self,index,data):
        if index < 0 or index > self.length():
            raise(IndexError)
        
        if index == 1:
            self.insert_at_beginning(data)

        count=0
        itr = self.head
        while itr:
            count+=1
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr=itr.next
        print(f"{data} Inserted at {index} Successfully !!")

    def print_LList(self):
        if self.head == None:
            print("Linked List is empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr+=itr.data+'-->' if itr.next else itr.data

            itr = itr.next
        print(llstr)

    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise(IndexError)

        if index == 1 :
            self.head = self.head.next
            return 

        itr = self.head
        count=0
        while itr.next:
            if count == index-1:
                itr.next = itr.next.next
            itr =itr.next
            count+=1
        # if index == self.length():  #removes last element
        #     self.head.next=None

    def insert_after_data(self, data_after, data_to_insert):

        if self.head ==None:
            print("LIST EMPTY")
        
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head == None: 
            print("LIST EMPTY")
        
        if self.head.data == data:
            self.head = self.head.next
            return
        itr =self.head
        
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            # if itr.next.data:
            #     print(itr.next.data)
            itr = itr.next
    
    def reverse_list(self):
        #By Iteration Method
        prev=None
        next=None
        if self.head == None: 
            print("LIST EMPTY")
        
        itr = self.head
        while itr:
            next  =itr.next
            itr.next = prev
            prev = itr
            itr = next 
        self.head = prev
        print("HEAD NOW : ",self.head.data)       
        print("LIST REVERSED")
if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_values(['1','2','3'])
    # l1.print_LList() 
    # l1.remove_at(1)
    # l1.print_LList()
    l1.insert_between(3,"100")
    # l1.remove_at(2)
    l1.print_LList()
    # l1.insert_after_data('2','4')
    # l1.print_LList()
    # l1.insert_after_data('2','3')
    # l1.print_LList()
    # l1.insert_after_data('3','8')
    # l1.print_LList()

    l1.print_LList()
    l1.reverse_list()
    l1.print_LList()
    l1.print_LList()


