# python script
name = input("Enter your name : ")
roll = int(input("Enter your roll number : "))
marks = int(input("Enter your marks : \n"))
grade = 0
remarks = ""

if(marks>=90):
    grade = 10
    remarks = "Outstanding"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)

elif(marks>=80):
    grade = 9
    remarks = "Very Good"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)
    
elif(marks>=70):
    grade = 8
    remarks = "Good"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)
    
elif(marks>=60):
    grade = 7
    remarks = "Average"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)
    
elif(marks>=50):
    grade = 6
    remarks = "Pass"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)
    
else:
    grade = 0
    remarks = "Fail"
    print("Name : ",name)
    print("Roll number : ",roll)
    print("Marks : ",marks)
    print("Grade : ",grade)
    print("Remarks : ",remarks)
