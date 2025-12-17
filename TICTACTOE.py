import random; 
def playervsplayer():
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = ' ' ; 
    current_player = 'X'; 

    while True:
        print("  " + p1 + " | " + p2 + " | " + p3 ); 
        print(" ------------"); 
        print("  " + p4 + " | " + p5 + " | " + p6 ); 
        print(" ------------"); 
        print("  " + p7 + " | " + p8 + " | " + p9 ); 
        try:
            move = int(input(f"Enter your move, Player {current_player} " " : ")); 
        except ValueError:
            print("An error occured");  

    # If our board is empty 
        if move == 1 and p1 == ' ':
            p1 = current_player; 
        elif move == 2 and p2 == ' ':
            p2 = current_player; 
        elif move == 3 and p3 == ' ':
            p3 = current_player; 
        elif move == 4 and p4 == ' ':
            p4 = current_player; 
        elif move == 5 and p5 == ' ':
            p5 = current_player; 
        elif move == 6 and p6 == ' ':
            p6 = current_player; 
        elif move == 7 and p7 == ' ':
            p7 = current_player; 
        elif move == 8 and p8 == ' ':
            p8 = current_player; 
        elif move == 9 and p9 == ' ':
            p9 = current_player;      
        else:
            continue; 

        if((p1 == current_player and p2 == current_player and p3 == current_player)or
        (p4 == current_player and p5 == current_player and p6 == current_player)or
        (p7 == current_player and p8 == current_player and p9 == current_player)or 
        (p1 == current_player and p4 == current_player and p7 == current_player)or 
        (p2 == current_player and p5 == current_player and p8 == current_player)or 
        (p3 == current_player and p6 == current_player and p9 == current_player)or 
        (p1 == current_player and p5 == current_player and p9 == current_player)or 
        (p3 == current_player and p5 == current_player and p7 == current_player)):
            print(f" Player {current_player} " " has won the game!"); 
            break; 

        if(p1 != ' ' and p2 != ' ' and p3 != ' ' and
        p4 != ' ' and p5 != ' ' and p6 != ' ' and 
        p7 != ' ' and p8 != ' ' and p9 != ' '):
            print("It is draw"); 
            break; 

        current_player = 'O' if(current_player == 'X') else 'X'; 
            

def playervscomputer():
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = ' ' ; 
    current_player = 'X'; 
    computer_player = 'O'; 
    while True:
        print("  " + p1 + " | " + p2 + " | " + p3 ); 
        print(" ------------"); 
        print("  " + p4 + " | " + p5 + " | " + p6 ); 
        print(" ------------"); 
        print("  " + p7 + " | " + p8 + " | " + p9 ); 
        try:
            move = int(input(f"Enter your move, Player {current_player} " " : ")); 
        except ValueError:
            print("An error occured");  

    # If our board is empty 
        if move == 1 and p1 == ' ':
            p1 = current_player; 
        elif move == 2 and p2 == ' ':
            p2 = current_player; 
        elif move == 3 and p3 == ' ':
            p3 = current_player; 
        elif move == 4 and p4 == ' ':
            p4 = current_player; 
        elif move == 5 and p5 == ' ':
            p5 = current_player; 
        elif move == 6 and p6 == ' ':
            p6 = current_player; 
        elif move == 7 and p7 == ' ':
            p7 = current_player; 
        elif move == 8 and p8 == ' ':
            p8 = current_player; 
        elif move == 9 and p9 == ' ':
            p9 = current_player;      
        else:
            continue; 

        if((p1 == current_player and p2 == current_player and p3 == current_player)or
        (p4 == current_player and p5 == current_player and p6 == current_player)or
        (p7 == current_player and p8 == current_player and p9 == current_player)or 
        (p1 == current_player and p4 == current_player and p7 == current_player)or 
        (p2 == current_player and p5 == current_player and p8 == current_player)or 
        (p3 == current_player and p6 == current_player and p9 == current_player)or 
        (p1 == current_player and p5 == current_player and p9 == current_player)or 
        (p3 == current_player and p5 == current_player and p7 == current_player)):
            print(f" Player {current_player} " " has won the game!"); 
            break; 

# computer player
       
        try:
                myMove = random.randint(1,9); 
                computer_move = print(f"Enter your move, Computer {computer_player} " " : ", myMove); 
        except ValueError:
                print("An error occured");  

        # If our board is empty 
        if  computer_move == 1 and p1 == ' ':
                p1 =  computer_player; 
        elif  computer_move == 2 and p2 == ' ':
                p2 =  computer_player; 
        elif  computer_move == 3 and p3 == ' ':
                p3 =  computer_player; 
        elif  computer_move == 4 and p4 == ' ':
                p4 =  computer_player; 
        elif  computer_move == 5 and p5 == ' ':
                p5 =  computer_player; 
        elif  computer_move == 6 and p6 == ' ':
                p6 =  computer_player; 
        elif  computer_move == 7 and p7 == ' ':
                p7 =  computer_player; 
        elif  computer_move == 8 and p8 == ' ':
                p8 =  computer_player; 
        elif  computer_move == 9 and p9 == ' ':
                p9 =  computer_player;      
        else:
                continue; 

        if((p1 ==  computer_player and p2 ==  computer_player and p3 ==  computer_player)or
            (p4 ==  computer_player and p5 ==  computer_player and p6 ==  computer_player)or
            (p7 ==  computer_player and p8 ==  computer_player and p9 ==  computer_player)or 
            (p1 ==  computer_player and p4 ==  computer_player and p7 ==  computer_player)or 
            (p2 ==  computer_player and p5 ==  computer_player and p8 == computer_player)or 
            (p3 ==  computer_player and p6 ==  computer_player and p9 ==  computer_player)or 
            (p1 ==  computer_player and p5 ==  computer_player and p9 ==  computer_player)or 
            (p3 ==  computer_player and p5 ==  computer_player and p7 ==  computer_player)):
                print(f" Computer {computer_player} " " has won the game!"); 
                break; 

        if(p1 != ' ' and p2 != ' ' and p3 != ' ' and
            p4 != ' ' and p5 != ' ' and p6 != ' ' and 
            p7 != ' ' and p8 != ' ' and p9 != ' '):
                print("It is draw"); 
                break; 
        if(move == computer_move):
             print("Play Again"); 
             break; 


while True: 

    print("\n- TIC TAC TOE -"); 
    print("- 1. Player vs Player -"); 
    print("- 2. Player vs Computer -"); 
    print('- 3. Exit -\n'); 
    try:
            choose = int(input("Enter your choice here : ")); 
    except ValueError:
            print("An error occurred");  

    if choose == 1:
            print("Palyer choose option : 1. Player vs Player "); 
            playervsplayer(); 
    elif choose == 2:
            print("Palyer choose option : 2. Player vs Computer "); 
            playervscomputer(); 
    elif choose == 3:
            print("Thank you for playing the game....!"); 
            break; 
    else:
            print("Option doesn't exist"); 
            break; 