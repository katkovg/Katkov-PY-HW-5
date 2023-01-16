def create_empty_field():

    field = [['.' for row in range(4)] for row in range(4)]
    field[0] = [' ', '1', '2', '3']
    for i in range(1,4): field[i][0] = field[0][i]
    return field

def print_field(field):

    print()
    for row in field: print(*row)

def player_position_assignment(field):

    print('Укажите позицию:')
    x = int(input('- по горизонтали (строку): '))
    y = int(input('- по вертикали (столбец): '))

    while field[x][y] in 'XO':
        print('\nЭта позиция уже занята.\nУкажите другую позицию:')
        x = int(input('- по горизонтали (строку): '))
        y = int(input('- по вертикали (столбец): '))

    return x, y

def victory_check(field):

    for row in field:
        if ''.join(row)[1:] in ('XXX', 'OOO'):
            return True

    for col in range(1,4):
        current_column = []
        for row in range(1,4):
            current_column.append(field[row][col])
        if ''.join(current_column) in ('XXX', 'OOO'):
            return True
    
    main_diag, side_diag = [], []
    for row in range(1,4):
        main_diag.append(field[row][row])
        side_diag.append(field[row][4-row])
    if (''.join(main_diag) in ('XXX', 'OOO')) or (''.join(side_diag) in ('XXX', 'OOO')):
            return True

def draw_check(field):

    for row in range(1,len(field)):
        if '.' in field[row]: return False
        if row == 3: return True