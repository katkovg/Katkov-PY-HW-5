from random import randint

def horizontal_lucky_move(field, bot_symbol, player_symbol, x, y):

    def bot_position_assignment(to_check_count, to_check_presence, x, y, field):

        for row in range(4):
            if ''.join(field[row]).count(to_check_count) == 2 and to_check_presence in ''.join(field[row]):
                x, y = row, randint(1,3)
                while field[x][y] in 'XO':
                    x, y = row, randint(1,3)
                return True, x, y
        return False, x, y
    
    is_lucky_move, x, y = bot_position_assignment(bot_symbol, '.', x, y, field)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment(player_symbol, '.', x, y, field)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment('.', bot_symbol, x, y, field)
    if is_lucky_move == True: return x, y
    
    return x, y
    
def vertical_lucky_move(field, bot_symbol, player_symbol, x, y):

    def bot_position_assignment(to_check_count, to_check_presence, x, y, field):

        for col in range(1,4):
            current_column = []
            for row in range(1,4):
                current_column.append(field[row][col])
            if ''.join(current_column).count(to_check_count) == 2 and to_check_presence in ''.join(current_column):
                x, y = randint(1,3), col
                while field[x][y] in 'XO':
                    x, y = randint(1,3), col
                return True, x, y
        return False, x, y

    is_lucky_move, x, y = bot_position_assignment(bot_symbol, '.', x, y, field)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment(player_symbol, '.', x, y, field)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment('.', bot_symbol, x, y, field)
    if is_lucky_move == True: return x, y
    
    return x, y

def diagonal_lucky_move(field, bot_symbol, player_symbol, x, y):

    def bot_position_assignment(diagonal, to_check_count, to_check_presence, x, y, field, col_number):

        if ''.join(diagonal).count(to_check_count) == 2 and to_check_presence in ''.join(main_diag):
            for row in range(1,4):
                if field[row][row] not in 'XO':
                    x, y = row, col_number
                    return True, x, y
        return False, x, y
        
    main_diag, side_diag = [], []
    for row in range(1,4):
        main_diag.append(field[row][row])
        side_diag.append(field[row][4-row])

    is_lucky_move, x, y = bot_position_assignment(main_diag, bot_symbol, '.', x, y, field, row)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment(side_diag, bot_symbol, '.', x, y, field, 4-row)
    if is_lucky_move == True: return x, y

    is_lucky_move, x, y = bot_position_assignment(main_diag, player_symbol, '.', x, y, field, row)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment(side_diag, player_symbol, '.', x, y, field, 4-row)
    if is_lucky_move == True: return x, y

    is_lucky_move, x, y = bot_position_assignment(main_diag, '.', bot_symbol, x, y, field, row)
    if is_lucky_move == True: return x, y
    is_lucky_move, x, y = bot_position_assignment(side_diag, '.', bot_symbol, x, y, field, 4-row)
    if is_lucky_move == True: return x, y

    return x, y