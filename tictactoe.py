gamePos = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def printCurrentPosition(matrix):  # выводит таблицу с поставленными крестиками-ноликами
    i = 0
    print(' ', 0, 1, 2)
    for row in matrix:
        print(i, *row)
        i += 1


def someoneWon(matrix):  # проверяет игру на наличие победителя
    # победа заполнив строку
    for row in range(3):
        if len(set(matrix[row])) == 1 and matrix[row][0] != '-':
            return True

    #  победа заполнив столбец
    for column in range(3):
        if matrix[0][column] != '-':
            if matrix[0][column] == matrix[1][column] == matrix[2][column]:
                return True

    # победа заполнив одну из диагоналей
    if matrix[1][1] != '-':
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            return True
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            return True
    return False


turns = 0
while not someoneWon(gamePos):
    #  Ход крестиком
    cross = input('Enter x position in format row,column: ').split(',')
    gamePos[int(cross[0])][int(cross[1])] = 'x'
    printCurrentPosition(gamePos)
    turns += 1

    if someoneWon(gamePos):
        print('x won!')
        break
    #  игра завершается ничьёй после 9 ходов и отсутсвия побелителя
    if turns == 9:
        print('draw!')
        break

    # ход ноликом
    zero = input('Enter o position in format row,column: ').split(',')
    gamePos[int(zero[0])][int(zero[1])] = 'o'
    printCurrentPosition(gamePos)
    turns += 1

    if someoneWon(gamePos):
        print('o won!')
        break
