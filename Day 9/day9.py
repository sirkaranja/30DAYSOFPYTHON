my_tuple=(1,2,3,4,5,90)

print( "r" in my_tuple) #this returns false since we dont have r in my_tuple

#difference between list and tuples is that fro tuples you cant change the values once declared(IMMUTABLE VALUES)

#list to tuples

num_list =[1,2,3,4,0,7]

#tuple key word is used in converting list to tuples
print(tuple(num_list))  
num_list.pop(4)

#tuples can also be created without the PARANTHESIS