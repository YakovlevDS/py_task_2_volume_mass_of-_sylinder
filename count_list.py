import re


def count_list(parameter,count=0):
    for i in parameter:
        count+=1
    return count

j=[2,3,4,5,6,7,5,0] 
print(count_list(j))   
k=[2,3,5,0]  
print(count_list(k))   

n=[2,3,4,0]  
print(count_list(n))   

m=[2,3]  
print(count_list(m))   
print(count_list('stroka list'))   

