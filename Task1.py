import random

players = ['бот', 'игрок']

print('\nДобро пожаловать!\n')

print('''Для игры необходимо будет задать изначальное количество конфет, 
а затем забирать их по очереди с ботом. Забирать можно не более 28-ми конфет за ход.
Выиграет и заберёт все конфеты тот из вас, кто совершит последний ход. Удачи!\n''')

sweets_count = int(input('* Задайте изначальное количество конфет: '))

draw_result = random.choice(players)
current_player = draw_result

print(f'Первый ход в результате жеребьёвки совершает {current_player}.')

while True:
    
    if current_player == 'игрок':

        player_turn = int(input('\n>>>>>>> Сколько конфет возьмёте? Укажите: '))

        while player_turn > 28 or player_turn < 1:
            print(':( Вы либо хотите взять больше 28-ми конфет, либо не взяли ни одной. Так нельзя. :(')
            player_turn = int(input('\n>>>>>>> Сколько конфет возьмёте? Укажите: '))

        sweets_count -= player_turn

        if sweets_count == 0 or sweets_count < 0:
            break

        print(f'__Конфет осталось: {sweets_count}__')

        current_player = 'бот'

    if current_player == 'бот':

        bot_turn = random.randint(1,28)

        if sweets_count > 29 and sweets_count - 29 <= 28 and sweets_count - (sweets_count - 29) == 29:

            print(f'\n!! | Бот забрал: {sweets_count - 29} | !!')
            sweets_count -= (sweets_count - 29)

        elif sweets_count <= 28:

            print(f'\n!! Бот забрал оставшиеся конфеты !!')
            break

        else:

            print(f'\n!! | Бот забрал: {bot_turn} | !!')
            sweets_count -= bot_turn

        print(f'__Конфет осталось: {sweets_count}__')

        current_player = 'игрок'

if current_player == 'игрок':
    print('\nПоздравляем, Вы победили!')
else:
    print('\nПобедил бот.')