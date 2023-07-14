##Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually)

def inpt():
#####Intrest rate
    while True:
        intrest_rate = input("INTREST RATE(in %): ")
        if intrest_rate.isnumeric():
            intrest_rate = int(intrest_rate)
            break
        else:
            print("Please enter a valid input!!")

####COMPOUNDING INTERVAL
    while True:
        compounding_interval = input("Compounding Interval \n(Monthly:1, \n Weekly:2,\n Daily:3, \nContinually:4 ): ")

        if compounding_interval in ('1','2','3','4'):
            if compounding_interval == '1':
                compounding_interval = 'Monthly'
                break
            if compounding_interval == '2':
                compounding_interval = 'Weekly'
                break 
            if compounding_interval == '3':
                compounding_interval = 'Daily'
                break
            if compounding_interval == '4':
                print("Not Available yet")
                
            

        else:
            print("Please enter a numeric value!!")        


###Payments
    while True:
        payment = input("PAYMENT(in Numericals): ")

        if payment.isnumeric():
            payment = int(payment)
            break
        
        else:
            print("Please enter a valid input!!")

    return intrest_rate,compounding_interval,payment


def calculation():
    interest_rate,interval,payment = inpt()

    if interval == 'Monthly':
        intrest = (payment * interest_rate)/100
        print(f"The monthly intrest is {round(intrest)} and TOTAL payment this year will be {round(payment + (intrest * 12))}")

    if interval == 'Weekly':
        intrest = (payment * interest_rate)/100
        print(f"The Weekly intrest is {round(intrest)}, Monthly intrest will be {round(intrest * 4)} and TOTAL payment this year will be {round(intrest * 52)}")

    if interval == 'Daily':
        intrest = (payment * interest_rate)/100
        print(f"The Daily intrest is {round(intrest)}, Monthly intrest will be {round(intrest * 28)} and TOTAL payment will be {round*365}\nNOTE:Number of Days in a Month is counted as 28")


if __name__ == '__main__':
    calculation()
