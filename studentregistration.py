import registrationfunction
def main():
     while True:
        c=registrationfunction.creat_menu()
        if c==1:
             registrationfunction.registration()
        elif c==2:
             registrationfunction.search_student()
        elif c==3:
             registrationfunction.delete_studentdata()
        elif c==4:
             registrationfunction.showall_data()
        elif c==5:
             print("thank you!")
             exit(0)
        else:
             print("invalide choice!")
main()