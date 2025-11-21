student=[]
num=int(input("please enter the registration number="))
print(f"=======Please Enter {num} Student Record=========")
for i in range(num):
    data={}
    education=[]
    data["name"]=input("\nenter your name=")
    data["contact"]=int(input("enter your contact="))
    data["address"]=input("enter your address=")

    tell="yes"
    for item in range(10):
        if(tell=="yes"):
            qualifications={}
            qualifications["qualification"]=input("enter your qualification=")
            qualifications["year"]=int(input("enter your passing year="))
            education.append(qualifications)

            tell=input("you want to enter more qualifiction enter yes/no: ").lower()
        else:
            break
    data["qualifictions"]=education
    student.append(data)

print("\n======= Students Record =======")
for stu in student:                
    for key, value in stu.items():

        if key == "qualifictions":
            print("qualifications:")
            for q in value:
                for key, value in q.items():
                    print(f"  {key} = {value}")
            print("\n")
        else:
            print(f"{key} = {value}")


print("**********Report***************") 
print("1. Search student by contact: ")
print("2. Search student by Qualification: ")
print("3.exit: ")
while True:
    c = int(input("enter your choice="))

    if c == 1:  
        contact = int(input("enter the contact number = "))
        found = 0

        for stu in student:              
            if stu["contact"] == contact:    
                print("\n--- Student Found ---")
                for k in stu:                
                    if k == "qualifications":
                        print("Qualifications:")
                        for key,value in stu["qualifications"]:
                             print(f"  {key} = {value}")
                            
                    else:
                        print(k, "=", stu[k])
                found = 1

        if found == 0:
            print("No student found with this contact")

    elif c == 2:   
        qname = input("enter qualification to search = ").lower()
        found = 0

        for stu in student:
            for q in stu["qualifictions"]:
                if q["qualification"].lower() == qname:
                    print("\n--- Student Found ---")
                    for key, value in stu.items():
                        if key == "qualifictions":
                            print("Qualifications:")
                            for q2 in value:
                                for k, v in q2.items():
                                    print(f"  {k} = {v}")
                        else:
                            print(f"{key} = {value}")
                    found = 1

        if found == 0:
            print("No student found with this qualification")

    elif c == 3:
        print("Exit...")
        break

    else:
        print("Invalid choice")




