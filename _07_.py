#check palindrome or not
s3 = input("Enter a string : ")
if s3 == s3[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")