dict = {'Rahul':90,'Heet':89,'Bhavya':92,'Dharmil':80}
user = input("Enter a Student's name:")
if user in dict:
    print(dict.get(user))
else:
    print("Student not found.")
