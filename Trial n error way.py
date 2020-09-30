# Herasma Karim DATE-05/19/2020 multble.py
def main():
    multipication_table = True
    while multipication_table :
        
        print()
        while 1:
            multiplier_value= int(input("Enter a multiplier value: "))
            if multiplier_value < 2 or multiplier_value > 12:
                print("The multiplier value must be between 2 to 12! Please try Again")
            else:
                  break
            
        # read start value from user
        while 1:
            start_value = int(input("Enter a start value: "))
            if start_value<2 or start_value>12:
                print("The start value must be between 2 to 12! Please try Again")
            else:
                break


        # read stop value from user
        while 1:
            stop_value = int(input("Enter a stop value: "))
            if stop_value<2 or stop_value>12 :
                print("The stop Value must be between 2 to 12! Please try Again")
            elif stop_value <start_value:
                print("The stop value can't be less than the start value ! Please try Again ")
            else:
                break
        


        # print multipication table
        else:
                print("\nMultipication Table")
                print("---------------------")
        
        # for loop starts from start value and interate upto stopvalue
        for number in range (start_value,stop_value+1):

        # print table
            print(multiplier_value," * ",number," = ", multiplier_value* number)

        # ask user whether user wants to continue or stop
        Multipication = int(input("\nEnter 1 to continue or 0 to stop: "))



main()
