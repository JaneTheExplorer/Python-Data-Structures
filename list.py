# 1. create an emty list caled my_list
my_list =[]

#2. append the following elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending elements:", my_list)

#3. insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("List after inserting 15at the second position:", my_list)

#4. extend my_list with another list
my_list.extend([50, 60, 70])
print("List after extending:", my_list)

#5. remove the last element form my_list
my_list.pop()
print("List after removing the last element:", my_list)

#6. sort my list in ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)

#7. Find and print the index of the value 30 in my_list
index_of_30= my_list.index(30)
print("Index of 30 in my_list:", index_of_30)