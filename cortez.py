def name(g,*a,key):
    print(g)
    print(a)
    print(key)

name(56,3,56,4566,2,key=10)   
#   поиск уникальных значений в нескольких массивах списках
def unique_item(*arg):
    unique_list=[]
    for i in arg:
        for y in i:
            if y not in unique_list:
                unique_list.append(y)  
    return unique_list            
z=[1,2,3,4,5,6,7,8,3,4]
s=[1,2,3,4,5,6,7,8,3,3,4,5,6,7,6,6,6,6,11,34,4]
d=[1,2,3,2,2,2,2,2,2,10,4,5,6,7,8,3,4]
t=unique_item(z,s,d)
print(t)