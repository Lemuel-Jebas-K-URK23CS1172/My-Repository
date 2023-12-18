mark=int(input("Enter Marks of student:"))
if(mark>90):
    grade='A'
elif(mark>79 and mark<90):
    grade='B'
elif(mark>69 and mark<80):
    grade='C'
else:
    grade='F'
print("Grade is:",grade)