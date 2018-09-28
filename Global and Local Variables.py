"""Rebinding should not be confused with mutation –
“rebinding” is a change to the referencing identifier;
“mutation” is a change to the referenced value.
"""
"""Which of the following procedures leaves the value passed in as the input unchanged?"""

def proc2(p):
    """function proc2(), is it because proc2() set up a local variable p, therefore only the local p is mutated???"""
    print("The initial id of p is:")
    print(id(p)) # 2108354450888
    p = p + [1]
         # [2, 3, 4, 1]
    print("The id of p after p=p+[1] is:")
    print(id(p)) # 2108355360008
    print("Print p after p=p+[1]")
    #[2, 3, 4, 1]
    print(p)

my_list = [2, 3, 4]
print("The id of my_list is:")
print(id(my_list)) # 2513995879880
print("------------------------------------")
print("print proc2(my_list):")
print(proc2(my_list))

print("Print my_list after proc2 is:")
print(my_list)     # [2, 3, 4]
print("The id of my_list after proc2 is:")
print(id(my_list)) # 62560456

def proc1(p):
    """function proc1(), is it because proc1() did not set up a local variable p, therefore the global p is mutated???"""
    p[0]=p[1]
    print(p)
my_list_two=[2,3,4]
print("print the id of my_list_two:")
print(id(my_list_two)) #2889712645384
print("print proc1(my_list_two)")
print(proc1(my_list_two)) #[3, 3, 4]
print("print my_list_two")
print(my_list_two) #[3, 3, 4]
print("print the id of my_list_two after proc1():")
print(id(my_list_two)) #2889712645384