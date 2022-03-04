print ('Before func')
def show():
    print('body func1')

def show2():
    print('body func2')
    x = 7+z
    return x

print('after func')
z=7
y=show2()
print(y)
show()
print(show()) #none

