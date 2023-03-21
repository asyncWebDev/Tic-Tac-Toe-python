import numpy as np
# 1) Matrix
# 2) Players
# 4) Select space (if player selects one of numbers from 1 to 9, function put the player on the space)

x = "-"
matrix = np.array([[x, x, x],
                   [x, x, x],
                   [x, x, x]])


class Player:
    def __init__(self, shape, moves):
        self.shape = shape
        self.moves = moves

game_play = True
player_1 = Player("O", [])
player_2 = Player("X", [])
active_player = player_1

def get_answer():
    answer = int(input("Put "))
    return answer

def operate_on_matrix(matrix):
    copied_matrix = matrix.copy()
    flatted_matrix = copied_matrix.flatten()
    return flatted_matrix


def put_the_player(answer, actual_matrix):
    flatted_matrix = operate_on_matrix(actual_matrix)
    if answer in range(len(flatted_matrix) + 1) and answer != 0:
        for i, __ in enumerate(flatted_matrix):
            if(i == answer):
                flatted_matrix[i - 1] = active_player.shape if flatted_matrix[i - 1] != player_1.shape  and flatted_matrix[i - 1] != player_2.shape else put_the_player(get_answer(), actual_matrix)
            if(answer == len(flatted_matrix)):
                flatted_matrix[-1] = active_player.shape if flatted_matrix[-1] != player_1.shape  and flatted_matrix[i - 1] != player_2.shape else put_the_player(get_answer(), actual_matrix)
        active_player.moves.append(answer)
    else: 
        print(f"Please put the number between 1 and {len(flatted_matrix)}")
        return put_the_player(get_answer(), actual_matrix)

    return flatted_matrix

def create_new_matrix(prev_flatted_matrix):
    counter = 0
    new_matrix = []
    for i, __ in enumerate(prev_flatted_matrix):
        if(i == counter):
            new_matrix.append(prev_flatted_matrix[counter:counter+3])
            counter = counter + 3
    return np.array(new_matrix)
    
def switch_the_player(player):
    global active_player
    active_player = player_2 if player == player_1 else player_1

def check_win(player):
    win_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9],
                    [1,5,9], [3,5,7]]
    for i in win_combinations:
        global game_play
        if (str(player.moves) == str(i)):
            print("winner")
            game_play = False
    print(player.moves)

def game(matrix):
    if (game_play == True):
        print(matrix)
        answer = get_answer()
        new_flatted_matrix = put_the_player(answer, matrix)
        new_matrix = create_new_matrix(new_flatted_matrix)
        check_win(active_player)
        switch_the_player(active_player)
        game(new_matrix)

game(matrix)

