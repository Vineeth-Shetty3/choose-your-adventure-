name = input("type your name: ")
print("Welcome", name, "to this adventure.")

answer = input(" YOu are on a dirt road, it has come to an end and you can go left or right. Whic way would you like to go ? : ").lower()

#For Left
if answer=="left":
    answer=input("you have come to a river . You can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()

    if answer== "swim":
        print("You dont know how to swim and you drowned and died.")

    elif answer== "walk":
        print("It's a river stoopid , you cant walk around it as there's no bridge and u somehow died LOL!")

    else:
        print("not a valid option. You lose")

#For Right
elif answer=="right":
    answer= input("you have ariived at a cliff. Do you want to Kratos jump or turn around.(Kratos jump/turn around)? : ").lower()
    if answer== "kratos jump":
        print(" YOU WIN!!! You landed on a sea of gold and you passed the test . Congratulations! you can buy the world")

    elif answer== "turn around":
        print("You were attacked by a pack of dire wolves and killed cos they smelled weakness in you.")

    else:
        print("not a valid option. You lose")
    

#For Wrong Option
else :
    print("not a valid option. You lose")

print("Thank you for playing",name," . If you won congratulations on your Bravery , if you lost PLEASE GO BACK TO THE GYM ! YOU LOSER!!!")