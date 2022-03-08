# num1=1
# num2=10
# num3=1000
# sum_of_all_numbers=num1+num2+num3
# print("Sum is {}0:n".format(sum_of_all_numbers))
# list_of_numbers=[1,10,1000]
# print(sum(list_of_numbers))

# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)



# list_of_numbers2=[3, 10, 5]
# list_of_number3= list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers)

# l1=[1,32,4]
# l2=[100, 200, 300]
# l3=[l1+l2]
# print(l3)

# team=["Seahawks",2014, "CenturyLink Field"]
# nums=[5, 10, 4, 5]
# words=["spam","ni"]

# words=["Spam", "Wink","Hi"]
# words.insert(1,"Hello")
# print("Words======>", words)

grades=[]
num=float(input("Enter the first grade"))
grades.append(num)
num=float(input("Enter the second grade"))
grades.append(num)
num=float(input("Enter the third grade"))
grades.append(num)
num=float(input("Enter the fourth grade"))
grades.append(num)


grades.append(num)
minimum_grade=min(grades)
grades.remove(minimum_grade)
minimum_grade=min(grades)
grades.remove(minimum_grade)
average=sum(grades)/len(grades)
print("Average Grade: {0:.2f}".format(average))
