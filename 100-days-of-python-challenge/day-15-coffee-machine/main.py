import machinedata

choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
drink = False

while drink == False:
    if choice == "espresso":
        if machinedata.check_resources(machinedata.coffee_list[0], machinedata.resources) == False:
            break
        print(f"That will be ${machinedata.coffee_list[0]['cost']}.")
        payment = machinedata.get_coffee_coins()
        if payment < machinedata.coffee_list[0]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
            continue
        elif payment > machinedata.coffee_list[0]['cost']:
            change = round(payment - machinedata.coffee_list[0]['cost'], 2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso. ☕️")
            drink = True
    elif choice == "latte":
        if machinedata.check_resources(machinedata.coffee_list[1], machinedata.resources) == False:
            break
        print(f"That will be ${machinedata.coffee_list[1]['cost']}.")
        payment = machinedata.get_coffee_coins()
        if payment < machinedata.coffee_list[1]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
            continue
        elif payment > machinedata.coffee_list[1]['cost']:
            change = round(payment - machinedata.coffee_list[1]['cost'], 2)
            print(f"Here is ${change} in change.")
            print("Here is your latte. ☕️")
            drink = True
    elif choice == "cappuccino":
        if machinedata.check_resources(machinedata.coffee_list[2], machinedata.resources) == False:
            break
        print(f"That will be ${machinedata.coffee_list[2]['cost']}.")
        payment = machinedata.get_coffee_coins()
        if payment < machinedata.coffee_list[2]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
            continue
        elif payment > machinedata.coffee_list[2]['cost']:
            change = round(payment - machinedata.coffee_list[2]['cost'], 2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino. ☕️")
            drink = True
    elif choice == "report":
        print(f"Water: {machinedata.resources['water']}ml")
        print(f"Milk: {machinedata.resources['milk']}ml")
        print(f"Coffee: {machinedata.resources['coffee']}g")
        choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
    elif choice == "off":
        print("Preparing to shut down the machine...")
        break
    else:
        choice = input("Invalid choice. Please choose again (espresso/latte/cappuccino), type report for resource availability: ").lower()
    while drink == True:
        another = input("Would you like to order another drink? (yes/no): ").lower()
        if another == "yes":
            choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
            drink = False
        elif another == "no":
            print("Thank you! Ready for next customer.")
            choice = input("What would you like? (espresso/latte/cappuccino), type report for resource availability: ").lower()
            drink = False
        else:
            print("Invalid input. Please respond with 'yes' or 'no'.")