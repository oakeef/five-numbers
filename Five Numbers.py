__author__ = 'Evan'

#Enter 5 values

value1 = int(input("Enter value #1: "))
value2 = int(input("Enter value #2: "))
value3 = int(input("Enter value #3: "))
value4 = int(input("Enter value #4: "))
value5 = int(input("Enter value #5: "))

#Store 5 values in list
list = [value1, value2, value3, value4, value5]
print("----------------------------------------")

#display in reverse order
print("Numbers in reverse order")
list.reverse()
#the reverse function reverse the order of the list
#this loop prints the values in the list for the length of the list
for n in list:
    print(n)
print("----------------------------------------")

#display average of all numbers
#calculates the average of all numbers in the list
average = sum(list)/len(list)
print("The average of the number is:",average)
print("----------------------------------------")

#display all numbers greater than average
print("Numbers that are greater than the average")
#create a new list that has all numbers from the other list that are larger than the average found earlier
#this uses a list comprehension
list2 = [n for n in list if n > average]
list2.sort()
#this loop prints the values in the new list of values higher than the average for the length of the list
for n in list2:
    print(n)