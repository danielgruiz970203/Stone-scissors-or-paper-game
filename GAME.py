#GAME rock, scissors or paper

import random
def welcome():
    print(" ")
    print("         WELCOME TO 'stone, scissors or paper' GAME            ")
    print(" ")
    user_start_option = 1
    while user_start_option != 0:
        user_start_option = int(start_game ())
                                                                                                                                                                                                                                                                                   
    
        

def start_game():
    print(" ")
    print("Would you like to play?")
    print("PRESS 1 TO START THE GAME")
    print("PRESS 0 TO QUIT")
    print(" ")
    user_start_option = input ("Choose the option ==> ")
    if user_start_option == "1":
        print (" ")
        print("------------------------------------------------------------")
        print (" ")
        print("The GAME has been started")
        print (" ")
        print (" __________________________________________________________")
        print ("| The first who wins two in sequence will be The champions |")
        print ("|__________________________________________________________|")
        start_scores = [0,0,0]
        while (start_scores[1]-start_scores[2])**2 <= 1:
            print(" ")
            print(f"GAME # {start_scores[0]+1}")
            games_count, computer_wins, user_wins = main(start_scores)
            start_scores[0]= games_count
            start_scores[1]= computer_wins
            start_scores[2]= user_wins 
            print(" ")
            print(f"Scores are {start_scores[1]}/{start_scores[0]} to computer and {start_scores[2]}/{start_scores[0]} for you")   
            print("------------------------------------------------------------")
        if start_scores[1] > start_scores[2]:
            print("                    | You LOSE |                    ")
            print(" ")
            print(" ")  
        else:
            print("                    | You WIN |                    ")  
            print(" ")
            print(" ")   
        return user_start_option     
    elif user_start_option == "0":
        print (" ")
        print("------------------------------------------------------------")
        print (" ")
        print("             GAME OVER               ")
        print (" ")
        return user_start_option
    else:
        print (" ")
        print("------------------------------------------------------------")
        print (" ")
        print("The choosen options is not  in our game, PLEASE TRAY AGAIN")
        print (" ")
        welcome()


def main(start_scores):
    options = ["STONE", "SCISSORS", "PAPER","STONE"]
    user_option = input("Insert your option (stone, scissors or paper) ==> ").upper()
    print(" ")
    print (" ___________________________________")
    print(f"| your choice was ==> {user_option} ")
    print ("|___________________________________")
    
    while   user_option not in options :
        print (" There is not an option like that, try again")
        user_option = input("Insert your option (stone, scissors or paper) ==> ").upper()
        print (" ___________________________________")
        print(f"| your choice was ==> {user_option} ")
        print ("|___________________________________")
    computer_option = random.choice(options[:-1])
    print(" ")
    print (" _______________________________________________")
    print(f"| The computer choice was ==> {computer_option} ")
    print ("|_______________________________________________")
    print(" ")
    print(" ")

    games_count = start_scores[0]
    computer_wins = start_scores[1]
    user_wins = start_scores[2]
       
    if computer_option == user_option:
        print (f"it was the same, we have a tied" )
        games_count += 1
    else:
        for idx,i in enumerate(options[:-1]):
            if computer_option == i:
                if user_option == options[idx+1]:
                    print(f"The {computer_option} get the {user_option} so, ")
                    print(f"You Lose")
                    print(" ")
                    games_count += 1
                    computer_wins += 1
                else:
                    print(f"The {computer_option} is gotten by the {user_option} so, ")
                    print(f"You Win")
                    print(" ")
                    games_count += 1
                    user_wins += 1
    return games_count, computer_wins, user_wins
    
    



if __name__ == "__main__":
    welcome()
    
    