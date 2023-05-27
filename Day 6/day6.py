#removing duplicate numbers
num = [1,3,3,4,6,7,9,10,5,10]

print(list(set(num)))
#this removes all duplicates in the list num





sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Remove the 0th, 4th, and 5th elements using list slicing
modified_list = sample_list[1:4]

# Print the modified list
print(modified_list)


#check for prime numbers

num = [3,6,9,12]

answer = True

for i in range(len(num)):
    if num[i] %3 !=0:
        answer= False
    break
print(answer)
