
def show_field(f):
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i), *f[i])

def users_input(f,user):
    while True:
        place = input(f"Ходит '{user}'. Введите координаты: два числа от 0 до 2 - сначала строка, затем столбец - через пробел: ").split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Необходимо ввести числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<=2 and y>=0 and  y<=2):
            print('Вы ввели недопустимые координаты')
            continue
        if f[x][y] in 'XO':
            print('Клетка занята')
            continue
        break
    return x,y

def win_position(f, user):
    def win_line(i1, i2, i3, user):
        if i1 == i2 == i3 == user:
            return True
    for n in range(3):
        if win_line(f[n][0], f[n][1], f[n][2], user) or \
            win_line(f[0][n], f[1][n], f[2][n], user) or \
            win_line(f[0][0], f[1][1], f[2][2], user) or \
            win_line(f[2][0], f[1][1], f[0][2], user):
            return True
        return False

field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    show_field(field)
    if count%2 == 0:
        user = 'X'
    else:
        user = 'O'
    if count < 9:
        x, y = users_input(field, user)
        field[x][y] = user
    elif count == 9:
        print('Игра окончена! Ничья.')
        break
    if win_position(field, user):
        show_field(field)
        print(f"Победа игрока {user}. Поздравляем!")
        break
    count += 1





