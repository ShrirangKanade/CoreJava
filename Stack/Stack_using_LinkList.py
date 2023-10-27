class item:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class Stack:
    def __init__(self):
        self.top = None
    
    def is_underflow(self):
        return self.top == None
    
    def push(self,value):
        if self.is_underflow():
            self.top = item(value)
            return
        
        node = item(value,self.top)
        self.top =node
        return
    
    def pop(self):
        if self.is_underflow():
            print("EMPTY")
        
        temp = self.top
        self.top = self.top.next
        return temp.data
    
    def peek(self):
        if self.top != None:
            print("PEEK : ",self.top.data)
            return self.top.data
        else:
            return "EMPTY"
    
    def show(self):

        if self.is_underflow():
            return "Empty"
        
        temp = self.top
        print("\n Items in Stack : ")
        while temp:
            print(temp.data)
            temp = temp.next
        
    def reverse_string(self,val):
        res=""
        for i in val:
            self.push(i)
        temp=self.top
        while temp.next:
            res += temp.data
            temp = temp.next
        print(res) 
    
    def is_eq_balanced(self,eqn):
        dict_ch= {'{':'}','(':')','[':']'}

            
        for i in eqn:
            if i=='(' or i=='{' or i=="[":
                self.push(i)
            
            if i==')' or i=='}' or i==']':
                if dict_ch[self.peek()] == i:
                    self.pop()
        if self.top !=None:
            print("False")    
        else:
            print("True")
        
        

if __name__ == "__main__":
    st = Stack()
    st.push("10")
    st.push("20")
    st.show()
    st.pop()
    st.show()