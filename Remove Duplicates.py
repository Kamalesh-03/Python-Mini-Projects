numbers = [1,2,2,3,4,9,9,5]

new_list = []

for i in numbers:

    if i not in new_list:
        new_list.append(i)

print(new_list)