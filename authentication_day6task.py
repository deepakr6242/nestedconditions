# way-->1
username="naresh"
password="p@$$word"
temp=1
while True:
    uname = input("Enter username: ")
    pwd = input("Enter password: ")
    if temp<3:
        if uname == username and pwd == password:
            print("you have successfully logged in")
            print(f"Welcome Mr.{uname}")
            break
        else:
            print("\none of your username and password not matched \nplease try again....\n")
    else:
        print("maximum attempts reached ")
        break
    temp+=1

# way->2

# for i in range(0,3):
#     uname=input('enter username: ')
#     pwd=input('enter password: ')
#     if uname == 'xyz' and pwd == '4589':
#         print("you have logged in")
#         break
#     else:
#         if i == 2:
#             print('exceeded maximum attempts')
#         else:
#             print("enter valid uid and pwd")





