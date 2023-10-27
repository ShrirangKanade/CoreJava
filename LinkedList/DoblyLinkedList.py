class Node():
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.last = None

    def list_empty(self):
        '''Checks whether list is empty or not'''
        if self.head is None:
            return True

    def length(self):
        '''Get list length'''
        if self.list_empty():
            return
        itr = self.head
        count=0
        while itr:
            itr =itr.next
            count+=1
        return count
    
    def insert_at_start(self,data):
        '''INerst values at start of list'''
        if self.list_empty():
            self.head =Node(str(data),None,None)
            return
        print('self.head.data ->',self.head.data) 
        
        self.head = Node(str(data),None,self.head)
        print('self.head.data ->',self.head.data)

        
    def insert_at_end(self,data):
        if self.list_empty():
            self.head=Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,itr,None)
        self.last = itr.next

    def prev_next_value_of_index(self,index):
        '''gives previous and next values of given index'''
        #index starts from 0
        count=0
        itr =self.head
        while itr:
            if count==index:

                print('\n itr.data -->',itr.data)
                try :
                    print('\n itr.prev.data -->',itr.prev.data)
                except:
                    pass
                try:
                    print('\n itr.next.data -->',itr.next.data)   
                except:
                    pass
                break    
            itr = itr.next
            count+=1

    def insert_at(self,data,index):
        '''insert values at any given index'''
        if index<0 or index>self.length():
            raise(IndexError)
        
        if index == 0:
            self.insert_at_start(data)
            return
        
        itr = self.head
        count=0
        while itr:
            if count == index-1:
                node = Node(data,prev=itr,next=itr.next)
                itr.next = node
                ################ MAIN ##################
                node.next.prev = node
                break
            itr = itr.next
            count+=1
            if index==self.length():
                self.insert_at_end(data)  
        print(f"{data} Inserted at {index} Successfully !!")

                
        
    def insert_values(self,lists):
        ''' Take list of values and convert it to linkedlist'''
        self.head=None
        for data in lists:
            self.insert_at_end(data)

    def print_list(self):
        ''' prints the list'''
        if self.head is None:
            print("LIST EMPTY")
        
        itr = self.head
        listx=''
        while itr:
            listx+=itr.data + "-->" if itr.next else itr.data
            itr = itr.next
        print('list is : ',listx)

    def remove_at(self,index):
        if index < 0 or index > self.length():
            raise(IndexError)
        
        if index==0:
            self.head =self.head.next
            if self.head:
                self.head.prev = None
            return
        itr = self.head 
        count=0
        while itr:
            if count == index - 1:
                node_to_remove = itr.next
                itr.next = node_to_remove.next
                if node_to_remove.next:
                    node_to_remove.next.prev = itr
                break
            itr=itr.next
            count+=1
        # if index == self.length():
        #     itr.

    def reverse_list(self):
        prev = None
        next = None
        if self.head is None:
            return "List Empty"
        
        itr = self.head
        while itr:

            next = itr.next
            itr.next=prev
            itr.prev =next        #linking reversibly
            prev = itr
            itr = next 
        self.head = prev
        print("HEAD NOW :",self.head)

        
if __name__ == '__main__':
    l1 = DoublyLinkedList()
    
    # l1.insert_at_start('11')
    l1.print_list()
    l1.insert_values([str(i) for i in range(5)])
    l1.print_list()
    # l1.remove_at(3)
    l1.reverse_list()
    l1.print_list()
    l1.prev_next_value_of_index(1)