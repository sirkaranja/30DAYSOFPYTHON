

def addition():
    num = int(input("enter num 1:"))
    num2 = int(input("enter num 2 :"))
    num3 = int(input("enter num 3:"))
    num4 = int(input("enter num 4:"))
    arry_sum= num+num2+num3+num4
    return(arry_sum)

result = addition()
print("the sum is", result)


# # write a function in python that takes a list of numbers and 
# # returns the second-largest item in the list of the given numbers.
def largest():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    num4 = int(input("Enter number 4: "))
    num5 = int(input("Enter number 5: "))

    arr_large = [num1, num2, num3, num4, num5]
    sorted_nums = sorted(arr_large)
    return sorted_nums

sorted_list = largest()
print("The second largest number is:", sorted_list[-2])


#write a function in python that takes 3 parameters: 
# name, age, and occupation and prints this sentence as output: 
# "My name is {name}, I am {age} years old and I work as a {occupation}". 
def person_details():
    name= str(input("Enter your name :"))
    age = int(input("Enter your age: "))
    occupation = str(input("What's your occupation"))
    return name, age, occupation
name, age, occupation= person_details()
print("My name is", name, "I am ", age ,"years old and I work as a" ,occupation)

