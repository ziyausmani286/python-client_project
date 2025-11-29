import registrationfunction
def main():
     while True:
        choice=registrationfunction.create_menu()
        if choice==1:
             registrationfunction.registration()
        elif choice==2:
             registrationfunction.search_student()
        elif choice==3:
             registrationfunction.delete_studentdata()
        elif choice==4:
             registrationfunction.showall_data()
        elif choice==5:
             print("thank you!")
             exit(0)
main()    