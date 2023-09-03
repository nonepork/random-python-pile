import random
from sys import exit # because python's exit doesn't work, it will still run the whole thing after exit
from time import sleep # yeah

door_emoji_list = ["\U0001F6AA","\U0001F6AA","\U0001F6AA"]
thatdoor = [1,2,3]
listafterexpose = [1,2,3]
# Door Emoji U0001F6AA
# Goat Emoji U0001F410
# Racing Car Emoji U0001F3CE
car = random.randint(1,3) # generates a (pseudorandom) number from 1 to 3
thatdoor.remove(car)


def check_if_correct(inteee):
    if int(inteee) == car:
        door_emoji_list[int(inteee)-1] = "\U0001F6AA\U0001F3CE"
        for i in door_emoji_list: print(i, end=" ")
        print("\n"+"Congrats, you picked the right door.")
        sleep(5)
        exit()
    else:
        pass

for i in door_emoji_list: print(i, end=" ")
print("\n"+"There are 3 doors, one of them has a super car, the other two is sheeps.")
the_number_you_chose = int(input("Choose a door(1~3):"))
    
check_if_correct(the_number_you_chose)
    
thatdoor.remove(the_number_you_chose)
thatdoor = int(thatdoor[0])

listafterexpose.remove(thatdoor)
door_emoji_list[thatdoor-1] = "\U0001F6AA\U0001F410"
    
if int(the_number_you_chose) != car:
    for i in door_emoji_list: print(i, end=" ")
    print("\n" + f"Lemme give ya a hint: behind door {thatdoor} is a sheep")
    the_number_you_chose = input("Choose a door("+str(listafterexpose[0])+"~"+str(listafterexpose[1])+"):")
    check_if_correct(the_number_you_chose)
    door_emoji_list[int(the_number_you_chose)-1] = "\U0001F6AA\U0001F410"
    for i in door_emoji_list: print(i, end=" ")
    print("\n"+"Wrong choice, you got le sheep")
    sleep(5)
    exit()