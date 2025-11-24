import createstudentmenu
import studentregistration
import serachstudent
import deletestudent
import showstudent 
def main():
     while True:
        choice=createstudentmenu.create_menu()
        if choice==1:
             studentregistration.registration()
        elif choice==2:
             serachstudent.search_student()
        elif choice==3:
             deletestudent.delete_studentdata()
        elif choice==4:
             showstudent.showall_data()
        elif choice==5:
             print("thank you!")
             exit(0)
main()    