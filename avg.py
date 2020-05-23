#!/usr/bin/python36
#enter your name

name = input("ente your name")
print("hello" + " " + name)

#how much grade you want to calculate

grade_num = int(input("enter how much grades you want to calculate:"))
grades= []
for i in range(1,grade_num+1):
	grades.append(int(input("grade"+ " " + str(i))))
print(grades)
grades.sort(reverse = True)
print("grades from highest to lowest")
print(grades)
print(name + " " +"your highest grade is:" + "\n" + str(max(grades))+ "\n" +"lowest grade is "+ " " +str(min(grades)))

#loop for calculate average of grades

#declearing sum variable with value 0

sum1 = 0
for i in range(grade_num):
	sum1 += grades[i]
print(sum1)

avg = sum1/grade_num

print(name+ " " + "your average is: " + " " + str(avg) + "\n")

d_avg = int(input("what is your desired average:"))

sum2 = d_avg * (grade_num+1)

more_num = sum2 -sum1


print(name+ " " + "you need " + str(more_num)+ " " + "in your next session")

print("good luck " + " " + name)









