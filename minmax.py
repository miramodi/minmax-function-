    
my_list2=[567483,278736,8787,1,378638387]

my_list=[10,34,2,76,67]

def find_min(my_list):
    minimum=my_list[0]
    for i in my_list:
        if i<minimum:
            minimum=i
    print (minimum)
    
def find_max(my_list):
    minimum=my_list[0]
    for i in my_list:
        if i>minimum:
            minimum=i
    print (minimum)
    
find_max(my_list2)
find_min(my_list2)
print(max(my_list2))
