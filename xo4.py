def show_field(f):
    if user == 'x':
        print ("Ходит игрок " + player1 +" (x):")
    else:
        print ("Ходит игрок " + player2 +" (o):")
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))

def users_input(f):
    while True:
        place=input('Введите координаты y x: ').split()
        if len(place)!=2:
            if place[0] == "ex":
                print ('выход')
                quit()
            else:
                print('Введите две координаты')
                continue
        if not(place[0].isdigit() or place[1].isdigit()):
            print('Введите числа')
            continue
        x,y= map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

def win_combo(f, user):
    f_list=[]
    for l in f:
        f_list+=l
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False

field=[['-']*3 for _ in range(3)]
count = 0
print ('Крестики - нолики. Введите "ex" для выхода')
player1=input('Введите имя первого игрока ')
player2=input('Введите имя второго игрока ')
while True:
    if count%2==0:
        user='x'
    else:
        user='o'
    show_field(field)
    x,y=users_input(field)
    field[x][y]=user
    if count==9:
        print('Ничья')
    if win_combo(field,user):
        if user == 'x':
            print(f"Выиграл {user} " + player1)
        else:
            print(f"Выиграл {user} " + player2)
        show_field(field)
        break
    count+=1
