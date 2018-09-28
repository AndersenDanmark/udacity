##1Assignning 3 values to 3 variables at once

a,b,c=[1,2,3]
print(a)
#==>1
print(b)
#==>2
print(c)
#==>3

##2Assignning 3 values to 3 variables at once
#Mutating lists. Which of the following procedures leaves the value passed in as the input unchanged?
def proc2(p):
    p=p+[1]
    return p

print(proc2([1,2,3]))

#==>[1, 2, 3, 1]
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#2 How to clone or copy a list?
#Using new_list = my_list then modifies new_list every time my_list changes.
#See the example below
def proc3(p):
    q=p
    p.append(4)
    print(p)
#==>[1, 2, 3, 4]
    q.pop()
    print(p)
#==>[1, 2, 3]
    return p
print(proc3([1,2,3]))
#==>[1, 2, 3]
#Why is this?
#With new_list = my_list, you don't actually have two lists. 
# The assignment just copies the reference to the list, not the actual list,
#  so both new_list and my_list refer to the same list after the assignment.
#o actually copy the list, you have various possibilities:
#new_list = old_list[:] This is the fasted way in terms of computation time
# new_list = old_list.copy()
# new_list = list(old_list)
# import copy new_list = copy.copy(old_list)
#import copy new_list = copy.deepcopy(old_list)
def proc4(p):
    q=[]
    while p:
        q.append(p.pop())
        print(p)
    while q:
        p.append(q.pop())
        print(p)
    return p
print(proc4([1,2,3]))

def proc1(p):
    p[0]=p[1]
    print(p)
p=[1,2,3]
print("print proc1(p)")
print(proc1(p))
print("print p")
print(p)