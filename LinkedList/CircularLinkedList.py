
'''For the insertion of a node at the beginning, we need to traverse the whole list. 
Also, for insertion at the end, the whole list has to be traversed. If instead of the start pointer, we take a pointer to the last node, 
then in both cases there won’t be any need to traverse the whole list. So insertion at the beginning or at the end takes constant time,
 irrespective of the length of the list.
'''
class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class CircularLinkedlist():
    def __init__(self):
        self.last=None
    
    def length(self):
        if self.last is None:
            print("Empty")   
        
        itr = self.last.next
        count=0
        while itr:
            count+=1
            itr = itr.next
            if itr==self.last.next:
                break
        return count
    
    def insert_at(self,data,index):
        if index<0 or index>self.length():
            return "INvalid INdex"

        if index==0:
            self.insert_at_start(data)
            return
        elif index==self.length():
            self.insert_at_end(data)
            return
        
        itr = self.last.next
        count=0
        while itr:
            if count== index-1:
                newnode = Node(data,next=itr.next)
                itr.next = newnode
                break
            count+=1
            itr = itr.next
        
   
    def add_to_empty_list(self,data):
        if self.last is None:
            node = Node(data,self.last)
            self.last = node
            self.last.next = node
            return

    def insert_at_start(self,data):
        if self.last is None:
            self.add_to_empty_list(data)
            return
        new_node = Node(data,next=self.last.next)
        self.last.next =new_node
        return
    
    def insert_at_end(self,data):
        if self.last is None:
            self.add_to_empty_list(data)
            return
        
        temp = self.last.next
        newnode = Node(data,next=temp)
        self.last.next = newnode
        self.last = newnode
        return

    def insert_values(self,data_list):
        self.last =None
        for data in data_list:
            self.insert_at_end(data)

    def print_next_of_item(self,index):
        count=0
        itr = self.last.next
        while itr:
            if count == index:
                print("itr.data --> ",itr.data)
                print("itr.next.data --> ",itr.next.data)
                break
            itr = itr.next
            count+=1
            if itr == self.last.next:
                print("\nINVALID INDEX")
                break
            
    def remove_at(self,index):
        if index<0 or index>self.length():
            print("INvlaid InDEX")
            return
        if index ==1:
            self.last.next = self.last.next.next
            return
        
        prev = None
        itr = self.last.next
        count=0
        while itr:
            count+=1
            if count==self.length():
                prev.next=self.last.next
                self.last = prev
                break

            if count == index:
                prev.next = itr.next
                break

            prev=itr
            itr = itr.next
        
        
        
        
             
    def print_llist(self):
         
        if (self.last == None):
            print("List is empty")
            return
        temp = self.last.next
        print()
        while temp:
            print(temp.data, end=" " )
            temp = temp.next
            if temp == self.last.next:
                break
        # if self.last is None:
        #     return 'List EMpty'
        
        # itr = self.last.next
        # listx = ""
        # while itr != self.last:
        #     listx+=itr.data+'-->' if itr.next else itr.data
        #     itr = itr.next
        # listx+=itr.data +'\n\t    '+'|'+'__'*6+'|' if itr.next else itr.data
        # print("List Now : ",listx)
        # print("Self.last.next : ",self.last.data)


if __name__ == "__main__":
    l1 = CircularLinkedlist()
    l1.insert_at_start('0')
    l1.print_llist()
    l1.remove_at(1)
    l1.print_llist()
    