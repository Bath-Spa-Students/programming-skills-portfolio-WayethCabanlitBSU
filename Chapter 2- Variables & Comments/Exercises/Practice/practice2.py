#Q2
print("Enter marks obtained in subject")

DVD= int(input("DVD: "))
DST= int(input("DST: "))
CD_1= int(input("CD_1: "))
SUB_2= int(input("SUB_4: "))
SUB_3= int(input("SUB_5: "))

sum= DVD+DST+CD_1+SUB_2+SUB_3
Average_sum= sum/5
percentage_average= float(sum/500)*100

print(end="Average Marks in subjects:")
print(Average_sum)

print(end="Percentage Marks in subjects: ")
print(percentage_average)
