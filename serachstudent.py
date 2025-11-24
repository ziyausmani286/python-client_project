import checkvalidation
import studentregistration
student = studentregistration.get_studentdata()
def search_studentid():
     id = input("enter the id number = ")
     id=checkvalidation.id_chcek(id)
     found = 0
   

     for student in student:              
         if student["id"] == id:    
            print("\n--- Student Found ---")
            for key, value in student.items():
                if key == "qualifictions":
                    print("Qualifications:")
                    for q in value:
                        for key, value in q.items():
                            print(f"  {key} = {value}")
                                
                else:
                    print(f"{key} = {value}")
            found = 1

     if found == 0:
            print("No student found with this id")

def search_studentqualification():
    
    qualification = input("enter the qualification = ").lower()
    qualification=checkvalidation.qualification_chcek(qualification)
    found = 0

    for student in student:
        for qual in student["qualifictions"]:
            if qual["qualification"].lower() == qualification:
                print("\n--- Student Found ---")
                for key, value in student.items():
                    if key == "qualifictions":
                        print("Qualifications:")
                        for q in value:
                            for k, v in q.items():
                                print(f"  {k} = {v}")
                    else:
                        print(f"{key} = {value}")
                found = 1
                break

    if found == 0:
        print("No student found with this qualification.")

def search_student():
     if len(student) == 0:
        print("No student registered yet.")
     else:
        print("**********search student***************")
        print("1. Search student by id: ")
        print("2. Search student by Qualification: ")
        print("3. Back: ")
        print("****************************************")
        while True:
            try:
                choice = int(input("Enter your choice = "))
                if choice == 1:
                    search_studentid()
                elif choice == 2:
                    search_studentqualification()
                elif choice == 3:
                    break
                else:
                    print("Invalid choice! Please select between 1 to 3.")
            except:
                print("Invalid input! Only numbers are allowed.")


