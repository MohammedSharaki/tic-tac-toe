#---------glopal varibles-------------


#game board 
board=[
        "-","-","-",
        "-","-","-",
        "-","-","-",
    ] 
#فوق احنا عملنا اللعبه والبنيه الاساسيه 



#if game still going
game_stil_going=True

#who won ? or tie ?
winner=None



#who turn is it 
currect_player="x"

#display board
def board_display(): # دي احنا عملنا موقع كل رقم 
    print(board[0]+" | " +board[1]+ " | "+ board[2]) 
    print(board[3]+" | " +board[4]+ " | "+ board[5])
    print(board[6]+" | " +board[7]+ " | "+ board[8])
#play the game is tic tac toe
def play_game():


    board_display()

    #while the game is still going
    while game_stil_going:

        #handel a single turn of an arbitrary player
        handel_game(currect_player) #علشان احنا هنا حطينا حاجات جوا الفانكشن لازم نحطها تحت


        #chek if the game has ended
        chek_if_game_over()


        #flip to the other player
        flip_player()


    # the game is ended 
    if winner =="x" or winner=="o":
        print( winner +" won. ")
    elif winner == None:
        print("tie. ")

#handel asingle turn of an arabitrary palyer       
def handel_game(player):
    print(player+" is play now")
    
    position = input("enter aposition from 1-9: ") #هنا احنا قولنا يدخل رقم من واحد الي 9 
    
    
    valid=False
    if not valid:
    # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
    
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] != "-":

        print("You can't go there. Go again.")
    board[position] =player #board [index in board] يعني لو ضغط رقم فوق يذهب الي الانديكس
    board_display() #ودي علشان يطبع

def chek_if_game_over():
    chek_for_winner()
    chek_tie()


def chek_for_winner():


    #set up glopal varibles
    global winner

    #chek rows
    row_winner=chek_rows()


    #chek culumn
    column_winner=chek_column()



    #chek diagonals
    diagnolas_winner=chek_diagonals()


    if row_winner:
        #there was winner
        winner=row_winner


    elif diagnolas_winner:
        #there was winner
        winner=diagnolas_winner


    elif column_winner:
        #there was winner
        winner=column_winner


    else:
        #there is no winner
        winner=None


    
def chek_rows(): 
    global game_stil_going
    #chek if row is currect
    row_1= board[0]==board[1]==board[2] !="-"
    row_2= board[3]==board[4]==board[5]!="-"
    row_3= board[6]==board[7]==board[8]!="-"
    if row_1 or row_2 or row_3:
        game_stil_going = False
    #retun the winner(X,O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return



def chek_column():
    global game_stil_going
    #chek if row is currect
    column_1= board[0]==board[3]==board[6] != "-"
    column_2= board[1]==board[4]==board[7] != "-"
    column_3= board[2]==board[5]==board[8] != "-"
    if column_1 or column_2 or column_3:
        game_stil_going = False
    #retun the winner(X,O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return




def chek_diagonals():
    global game_stil_going
    #chek if row is currect
    diagonals_1= board[0]==board[4]==board[8] !="-"
    diagonals_2= board[6]==board[4]==board[2]!="-"

    if diagonals_1 or diagonals_2 :
        game_stil_going = False
    #retun the winner(X,O)
    if diagonals_1:
        return board[0]
    if diagonals_2:
        return board[6]

    return

def chek_tie():
    global game_stil_going
    if "-" not in board:
        game_stil_going=False
    return


def flip_player():
    global currect_player
    #global varibles
    if currect_player=="x": #if current player = x ,chang  to o
        currect_player="o"
    elif currect_player =="o": #if current player = p ,chane to x
        currect_player="x"
        
    return


play_game()
