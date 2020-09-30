#Programming


def years_to_mature():
    years_to_mature_=maturity_target/investment_amount

    
def investment():
    maturity_amount=investment_amount*years_to_mature 

def main():
    investor_name=input("Please enter investor's name:- ")
    investment_amount=int(input("Please enter the investment amount(Min=$20 and Max=$100):- "))
    while investment_amount < 20 or investment_amount > 100:
        print("The amount you have entered is not in the given range")
        investment_amount=int(input("Please enter the investment amount:- "))
    
    maturity_target=int(input("Please enter the target Maturity Amount(Not more than $50000):-"))
    while maturity_target > 50000 or maturity_target <= investment_amount:
        print("The maturity amount should not exceed 50000 and not less or equal to the investment Amount")
        maturity_target=int(input("Please enter the target Maturity Amount(Not more than $50000):-"))

    
           


    print()
    print("Investor Name \t Investment Amount \t Maturity Target \t Years To Mature \t Maturity Amount")
    print("-"*110)
    print(investor_name,"\t",investment_amount,"\t",maturity_target,"\t",years_to_mature_,"\t",maturity_amount)
    # use programme in fullscreen mode 

main()
