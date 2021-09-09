print("Welcome to the bank")
restart = 'y'
balance = 150
chances = 3

while chances >= 0:
    pincode = int(input('please enter your 4 digit pin'))
    if pincode == (2250):
        print("Access Granted\n")
        while restart not in ('n','N','no','NO','No'):
            print("Select 1 for Balance\n")
            print("Select 2 for withdrawal\n")
            print("Select 3 to Pay in\n")
            print("Select 4 for returning card\n")

            option = int(input('What do you want to do?\n'))
            if option == 1:
                print("your Balance is Rupees",balance)

                restart = input('would you like to go back?')
                if restart in ('n','N','no','NO','No'):
                    print("Thank yo for using Service!")
                    exit

                    

            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much wuld you like to withdraw?'))
                if withdrawl < balance:
                    balance = balance - withdrawl
                    print("\nremaining balance is ",balance)
                else :
                        print("insufficient balance\n")
                        exit
                       
                    

                restart = input('would you like to go back?')
                if restart in ('n','N','no','NO','No'):
                        print("Thank yo for using Service!")
                        

            elif option == 3:
                pay_in = float(input('how much would you like to add?'))

                balance = balance + pay_in 
                print("\n Current balance is",balance)  

                restart = input('would you like to go back?')
                if restart in ('n','N','no','NO','No'):
                     print("Thank yo for using Service!")
                     exit
                        

            elif option == 4:
                print("Wait while your card is returned......")
                print("Thank yo for using Service!")
                exit

                
    elif pincode != ('2250'):
        print("Incorrect password")
        chances = chances - 1

        if chances == 0:
            print("\nyour card has been blocked for 24 hours, please try later")
            exit


                    




             



