def duplicate():
    num1 = int(input("Enter num 1:"))
    num2 = int(input("Enter num 2:"))
    num3 = int(input("Enter num 3:"))
    num4 = int(input("Enter num 4:"))
    num5 = int(input("Enter num 5:"))
    num6 = int(input("Enter num 6:"))

    display = (num1, num2, num3, num4, num5)
    display_sort = sorted(display)
    return display_sort

print(list(set(duplicate())))


#2
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Remove the 0th, 4th, and 5th elements using list slicing
modified_list = sample_list[1:4]

# Print the modified list
print(modified_list)

