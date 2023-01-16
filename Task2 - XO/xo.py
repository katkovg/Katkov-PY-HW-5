from random import randint, choice
import functions
import intellect

field, players = functions.create_empty_field(), ('бот', 'игрок')

current_player = choice(players)

player_symbol, bot_symbol = '', ''

if current_player == 'игрок': player_symbol, bot_symbol = 'X', 'O'
else: player_symbol, bot_symbol = 'O', 'X'

print(f'\nЖеребьёвка определила, что первым будет ходить {current_player}.\nВаш символ: {player_symbol}.')

while True:

    if current_player == 'игрок':

        functions.print_field(field)

        x, y = functions.player_position_assignment(field)
        
        field[x][y] = player_symbol

        is_victory = functions.victory_check(field)

        if is_victory == True:
            functions.print_field(field)
            print('\nВы победили!')
            break

        current_player = 'бот'

    is_draw = functions.draw_check(field)
    if is_draw == True: 
        functions.print_field(field)
        print('\nВсе позиции заняты. Игра завершена. Ничья.')
        break

    if current_player == 'бот':

        x, y = randint(1,3), randint(1,3)
        while field[x][y] in 'XO': x, y = randint(1,3), randint(1,3)

        x, y = intellect.horizontal_lucky_move(field, bot_symbol, player_symbol, x, y)
        x, y = intellect.vertical_lucky_move(field, bot_symbol, player_symbol, x, y)
        x, y = intellect.diagonal_lucky_move(field, bot_symbol, player_symbol, x, y)

        field[x][y] = bot_symbol

        is_victory = functions.victory_check(field)

        if is_victory == True:
            functions.print_field(field)
            print('\nПобедил бот.')
            break
            
        current_player = 'игрок'

    is_draw = functions.draw_check(field)
    if is_draw == True: 
        functions.print_field(field)
        print('\nВсе позиции заняты. Игра завершена. Ничья.')
        break
