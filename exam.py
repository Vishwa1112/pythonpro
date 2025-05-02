medical_cause=input("do you have medical cause y for yes and n for no ")
if medical_cause=="Y" or medical_cause=="y":
    print("student is allowed for exam")
else:
    check_attendence=int(input("enter your attendence "))
    if check_attendence>75:
        print("you are allowed for exam")
    else:
        print("you are not allowed for the exam")
