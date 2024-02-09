def print_rangoli(size):
    chrs = [chr(i) for i in range(97,97+size)]
    chrs = chrs[::-1]
    j=0
    result=''
    listx=[]
    
    #for Top Pattern
    for i in range(len(chrs)):
        j=i-1
        res=chrs[i]
        while j>=0:
            result+=chrs[j]+res+chrs[j]
            j-=1
            res = result
            result=''
        else:
            listx.append(res)
            
    #for bottom pattern
    mid = len(res)//2
    j=mid
    while j>=0:
        result+= res[:j]+res[j+2:]
        res = result
        j-=1
        result=''
        listx.append(res)
        
    listx.pop() #pops last empty element
    
    #Accessing Mid value
    global mid_value 
    mid_value= len(listx[len(listx)//2])
    
    #Decorating with - for final output
    def decorate(string):
        deco_stuff = mid_value - len(string)
        return "-"*deco_stuff + "-".join(string) + "-"*deco_stuff    
    
    ans= list(map(decorate, listx)) #List of string's output
    final_res=""
    for i in ans:
        final_res+=i+"\n" #Make a single string with each line separated
    print(final_res)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
