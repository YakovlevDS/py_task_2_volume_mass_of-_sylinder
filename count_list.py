import re


def count_list(parameter,par2=False,count=0):
    if par2 == True:
        typ=type(parameter[0])
        for i in parameter:
            count+=1
        return count, typ

    else:    
        for i in parameter:
            count+=1
        return count

j=[2,3,4,5,6,7,5,0] 
print(count_list(j,True,-1))   
k=[2,3,5,0]  
print(count_list(k))   

n=[2,3,4,0]  
print(count_list(n))   

m=[2,3]  
print(count_list(m))   
print(count_list('stroka list')) 

h,p=count_list(j,True,-1)
print(h)
print(p)

