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

f = open("CoinCount.txt", "w")
f.close()


records = {
        # name: [bags checked, accuracy, value]
    }



f = open("CoinCount.txt", "r")
lines = f.readlines()
f.close()
print(lines)

print(records)

accuracy = 0
bagschecked = 0
bagscheckedcorrect = 0

percentage = 0

finished = False

print(f"Valid coins are {accepted}. 200 = £2 and 100 = £1")

option = input("Do you want to look at the number of bags checked and their values or count coins(for number of bags put 1 and to use the coin count feature put 2): " )

while finished == False:
    name = ""

    if option == "2":
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
            coin_num = remaining // coin[coin_type][3]
            print(f"You need to remove {coin_num} more coins")
            if name in records:
                bagschecked += 1
            else:
                bagschecked = 1
        elif coin[coin_type][2] > weight:    
            remaining = coin[coin_type][2] - weight
            coin_num = remaining // coin[coin_type][3]
            print(f"You need to add {coin_num} more coins")
            if name in records:
                bagschecked += 1
            else:
                bagschecked = 1
    else:
        print("Correct weight of the bag.")
        if name in records:
            bagschecked += 1
            bagscheckedcorrect += 1
        else:
            bagschecked = 1
            bagscheckedcorrect = 1
    if bagschecked > 0 and bagscheckedcorrect > 0:
        percentage = (bagscheckedcorrect / bagschecked) * 100

    
    if name in records:
        records[name] = [bagschecked, percentage / bagscheckedcorrect] 
    else:
        records[name] = [bagschecked, percentage]
    
    


    f = open("CoinCount.txt", "r")
    for line in lines:
        part = line.strip("\n").split(",")
        records[part[0]] = [part[1].strip(), part[2].strip()]
    
    
    if name in open("CoinCount.txt", "r"):
        f = open("CoinCount.txt", "a")
        for record in records:
            f.write(f"{name} {str(records[record])}\n")
        f.close()
    else:
        f = open("CoinCount.txt", "w")
        for record in records:
            f.write(f"{record} {str(records[record])}\n")
        f.close()

    print(records)

    done = input("Are you finished?: ")
    if done == "yes" or done == "Yes":
        finished = True


'''
f = open("CoinCount.txt", "w")
  f = open("CoinCount.txt", "w")
    if name in f.readlines():
        f.write(name, count + 1 )
    else:
        f.write(name, count)
'''















