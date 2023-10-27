class item:
    def __init__(self,data=None,next=None):
        self.data = int(data)
        self.next = next

class Queue:
    def __init__(self):
        self.rear =None
        self.front = None
    
    def is_empty(self):
        return self.front == None
    
    def enqueue(self,val):
        if self.is_empty():
            self.front = item(val,None)
            self.rear = self.front
            return
        
        newnode =item(val,None)
        self.rear.next = newnode
        self.rear = newnode
        return
    
    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = self.front.next
        return temp.data
    
    def show(self):
        if self.is_empty():
            return 
        
        temp = self.front
        print("ITEMS IN QUEUE :")
        while temp:

            print(temp.data)
            temp = temp.next
        print("*"*50)
        return

    def rev_fun(self,num):
        if num == 0:
            return 0
        else:
            self.enqueue(num%10)
            res = self.rev_fun(num//10)
            res = 10*res + self.dequeue()
            return res
        
if __name__ == "__main__":
    queue = Queue()
    rev = queue.rev_fun(123)
    print(rev)
