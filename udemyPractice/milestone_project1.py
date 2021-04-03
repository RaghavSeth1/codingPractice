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

def which_player_you_are():
    choice='wrong'
    while choice not in ['O','X']:
        choice=input("Which player you want to be O or X?:")
        if choice not in ['O','X']:
            print("Sorry , Please choose between O or X")
    return int(choice)

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

which_player_you_are()