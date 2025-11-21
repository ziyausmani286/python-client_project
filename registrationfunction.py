import json
studentdata=[]
def registration():
    data={}
    education=[]
    data["name"]=input("\nEnter your name =")
    data["id"]=int(input("Enter your id ="))
    data["address"]=input("Enter your address =")

    tell="yes"
    for item in range(10):
        if(tell=="yes"):
            qualifications={}
            qualifications["qualification"]=input("Enter your qualification=")
            qualifications["year"]=int(input("Enter your passing year="))
            education.append(qualifications)

            tell=input("You want to enter more qualifiction enter yes/no: ").lower()
        else:
            break
    data["qualifictions"]=education
    studentdata.append(data)

def search_student():
    
        id = int(input("Enter the id number = "))
        found = 0

        for stu in studentdata:   
            if(stu["id"]==id):
           
                for key, value in stu.items():
                    if key == "qualifictions":
                        print("qualifications:")
                        for q in value:
                            for key, value in q.items():
                                print(f"  {key} = {value}")
                    else:
                        print(f"{key} = {value}")

                found = 1
                break

        if found == 0:
            print("No student found with this id")

def delete_studentdata():
     id = int(input("Enter the id number = "))
     found = 0
     for stu in studentdata:   
            if(stu["id"]==id):
                studentdata.remove(stu)
                print(f"the student {stu["name"]} data is deleted")
                found = 1
                break
     if found == 0:
            print("No student found with this id")

def showall_data():
    print("========All student data=======")
    print(json.dumps(studentdata, indent=3))
    
def creat_menu():
    print("""\n*+*+*+*+*+*+*+*+ STUDENT REGISTRATION MENU +*+*+*+*+*+*+*+*
1. REGISTRATION
2. SEARCH STUDENT DATA
3. DELETE STUDENT DATA
4. SHOW ALL STUDENT DATA
5. EXIT
*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*""")   
    choice=int(input("Enter the choice:")) 
    return choice

