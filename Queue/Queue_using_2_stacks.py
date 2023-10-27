from Stack_using_LinkList import item,Stack


if __name__ == "__main__":
    st1 = Stack()
    st2 = Stack()
   
    def enqueue(val):
        st1.push(val)
        return
    
    def dequeue():
        
        if st2.is_underflow():
            if st1.is_underflow():
                return "EMPTY"
            else:
                temp = st1.top
                while temp:
                    st2.push(temp.data)
                    st1.pop()
                    temp = temp.next
               
        st2.pop()
    flag = 1
    while flag==1:
        choice  = int(input("1. Enqueue 2.Dequeue : ")) 
        if choice==1:
            val = input("Enter VAl :")
            enqueue(val)
            st1.show()
        
        elif choice==2:
            dequeue()
            st2.show()
        else:
            print("Invalid INput")
        
        flag = int(input("(1/0) : "))

        
            