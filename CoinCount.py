accepted = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]

coin = {
        #  coin \  Bag \  Bag \ coin
        #  value \ value\ weight\ weight
    "£2": [200, 2000, 120, 12.00],
    "£1": [100, 2000, 175, 8.75],
    "50p": [50, 1000, 160, 8.00],
    "20p": [20, 1000, 250, 5.00],
    "10p": [10, 500, 325, 6.50],
    "5p": [5, 500, 325, 3.25],
    "2p": [2, 100, 356, 7.12],
    "1p": [1, 100, 356, 356]


}

finished = False

print(f"Valid coins are {accepted}. 200 = £2 and 100 = £1")

option = input("Do you want to look at the number of bags checked and their values or count coins(for number of bags put 1 and to use the coin count feature put 2): " )


if option == "2":
    while finished == False:
        name = input("Enter your name: ").title()
        coin_type = input("Enter the type of coin you are using: ")

    while coin_type not in accepted:
        print("Invalid coin, please try again")
        coin_type = input("Enter the type of coin you are using: ")

    weight = int(input("Enter weight of the bag: "))

    # Validating the weight
    if weight != coin[coin_type][2]:
        if weight > coin[coin_type][2]:
            remaining = weight - coin[coin_type][2]
            coin_num = remaining / coin[coin_type][3]
            print(f"You need to remove {coin_num} more coins")
        else:    
            remaining = coin[coin_type][2] - weight
            coin_num = remaining / coin[coin_type][3]
            print(f"You need to add {coin_num} more coins")

    done = input("Are you finished?: ")
    if done == "yes" or done == "Yes":
        finished = True





















