#game_list=[0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

def position_choice():
    list_valid_index = [0, 1, 2]
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice=input("Pick a position[0,1,2]:")
        if choice not in ['0','1','2']:
            print("Sorry Invalid Position choice")
    return int(choice)


def replacement_value(game_list,position):
    user_placement=input("Type a string replacement value:")
    game_list[position]=user_placement
    return game_list

def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("Keep Playing? (Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry ,Please choose Y/N")
    if choice=='Y':
        return True
    else:
        return False

game_list=[0,1,2]
game_on=True
while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replacement_value(game_list,position)
    display_game(game_list)
    game_on=gameon_choice()
