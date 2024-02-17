
print(
'''
[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]
[------------Cyber Easy-------------]
[___________________________________]
''')

pass_1 = input('''
[Enter "easy" for recovration]
Enter the password :''')
rec_1 = "easy"
if pass_1 == "yash" :
    print (" password are successfull")
elif pass_1 == "easy":
    cap_1 = input(" Are you ready for human identification ? yes or not ")
    if cap_1 == "no" :
            print( " okey sir :( ")
            exit()
    elif cap_1 == "yes" : 
        cap_2 = input(" How many fingers have human hand ? - ")
        if cap_2 == "8" :
            print("thanku sir welcome :) ")
        else :
            print("sorry sir")
            exit()
    else :
        print("sorry sir")
        exit()
    print("-------------------------------------")
    rec_2 = input("Enter the recovery key: ")
    if rec_2 == "1234567890" :
        print("Your password id 'yash'")
        print("Thankyou sir :)")
    else: 
        print ( " sorry sir ")
else:
    print('wrong password')   
    yas