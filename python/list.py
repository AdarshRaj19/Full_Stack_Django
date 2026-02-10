#wap to create a list of marks < 30 from a given list of marks
marks=[12,15,48,98,12,26,87,50,30,60,29]
less_than_30 = [m for m in marks if m < 30]
print("Marks less than 30:", less_than_30)

#wap to increase a marks list by 10%  by without creating a new list
for i in range(len(marks)):
    marks[i] = marks[i] + (marks[i] * 0.10)
print("Marks after increasing by 10%:", marks)

