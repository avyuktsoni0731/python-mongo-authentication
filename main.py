from auth import store_user, verify_user, delete_user
from encryptorDb import client

def interface():
    if client is not None:
        print("\n \U0001F7E2 Connection to MongoDB server is open.")

    option = int(input(
        '''
------------------------------------
          Choose an Option
------------------------------------
1) Create a User
2) Verify a User
3) Delete a User
0) Exit
\u2192 '''))

    while True:
        if option == 1:
            username = input("Enter the Username: ")
            password = input("Enter the Password: ")
            store_user(username, password)
            
            restart = int(input('''
------------------------------------
      Do you want to continue?
------------------------------------
1) Yes
2) No
\u2192 '''))
            if restart == 1:
                interface()
            elif restart == 2:
                print("--------Goodbye!--------")
                break
            else:
                print("--------Invalid Input!--------")
                break
            break
            
        elif option == 2:
            username = input("Enter the Username: ")
            password = input("Enter the Password: ")
            verify_user(username, password)
            
            restart = int(input('''
------------------------------------
      Do you want to continue?
------------------------------------
1) Yes
2) No
\u2192 '''))
            if restart == 1:
                interface()
            elif restart == 2:
                print("--------Goodbye!--------")
                break
            else:
                print("--------Invalid Input!--------")
                break
            break

        elif option == 3:
            username = input("Enter the Username: ")
            password = input("Enter the Password: ")
            delete_user(username, password)

            restart = int(input('''
------------------------------------
      Do you want to continue?
------------------------------------
1) Yes
2) No
\u2192 '''))
            if restart == 1:
                interface()
            elif restart == 2:
                print("--------Goodbye!--------")
                break
            else:
                print("--------Invalid Input!--------")
                break
            break

        elif option == 0:
            print("--------Goodbye!--------")
            break
        else:
            print("--------Invalid Input!--------")
            interface()
            break
        
    
        

if __name__ == '__main__':
    interface()
    
    client.close()
    client = None

    if client is not None:
        print("\n \U0001F7E2 Connection to MongoDB server is open.")
    else:
        print("\n \U0001F534 Connection to MongoDB server is closed.")