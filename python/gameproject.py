class User:
    def __init__(self):
        self.wang = 0
        self.sang = 0
        self.jang = 0
        self.ja = 0


# team,kind
# 0=빈 1=왕 2=장 3=상 4=자 5=후

Board = [
    [[1, 2], [1, 1], [1, 3]],
    [[0, 0], [1, 4], [0, 0]],
    [[0, 0], [2, 4], [0, 0]],
    [[2, 3], [2, 1], [2, 2]]
]

A = User()
B = User()
turn = 1
aliveA = 0
aliveB = 0
color_end = '\x1b[0m'

#View

To_char = ['  ','１','２','３','４','５','６','７','８','９']
def To_charf(num):
    if 1<=num<=9:
        return To_char[num];
    else:
        return "  "


def VIEW2():
    for i in range(4):
        print("┣━━━━━━━━━━━━━━━━━━━━┫")
        for j in range(3):
            print_row(i, j)
    print("┗━━━━━━━━━━━━━━━━━━━━┛")
    color = '\x1b[1;30;41m'

    print("===%sA의 보유 말%s==="%('\x1b[1;30;41m',color_end))
    print("  장 %d 상 %d 자 %d" % (A.jang, A.sang, A.ja));
    print("===%sB의 보유 말%s==="%('\x1b[1;30;44m',color_end))
    print("  장 %d 상 %d 자 %d" %(B.jang, B.sang, B.ja));


def VIEW_process(turn):
    for i in range(4):
        print("┣━━━━━━━━━━━━━━━━━━━━┫")
        for j in range(3):
            print_row2(i, j, turn)
    print("┗━━━━━━━━━━━━━━━━━━━━┛")
    print("===A의 보유 말===")
    print("  장 %d 상 %d 자 %d" % (A.jang, A.sang, A.ja));
    print("===B의 보유 말===")
    print("  장 %d 상 %d 자 %d" % (B.jang, B.sang, B.ja));
    print()


def print_row(row, small_row):
    for column in range(3):
        if small_row == 0:
            TOP(row,column)
        elif small_row == 1:
            MID(row,column)
            pass
        elif small_row == 2:
            BOT(row,column)
    print("┃")


def print_row2(row, small_row, turn):
    for column in range(3):
        if small_row == 0:
            TOP(row,column)
        elif small_row == 1:
            Num = 0
            if turn ==1:
                Num = 7 - 3*row + column
            else:
                Num = 10 - 3*row + column
            MID2(row,column, Num)
            pass
        elif small_row == 2:
            BOT(row,column)
    print("┃")


def TOP(row,column):
    turn = Board[row][column][0]
    peice = Board[row][column][1]
    if peice == 1:
        print("┃↖∧↗", end="")
    elif peice == 2:
        print("┃  ∧  ", end="")
    elif peice == 3:
        print("┃↖  ↗", end="")
    elif peice == 4 :
        if turn == 1:
            print("┃      ", end="")
        else:
            print("┃  ∧  ", end="")
    elif peice == 5:
        if turn == 1:
            print("┃  ∧  ", end="")
        else:
            print("┃↖∧↗", end="")
    else:
        print("┃      ", end="")

'''
↖ㅣ↗
ㅡ□ㅡ
↙ㅣ↘
'''

def MID(row,column):
    turn = Board[row][column][0]
    peice = Board[row][column][1]
    if turn == 1:
        color = '\x1b[1;30;41m'
    else:
        color = '\x1b[1;30;44m'
    if peice == 1:
        print("┃←-%s왕%s-→"%(color,color_end), end="")#1b 16 + 11 27
    elif peice == 2:
        print("┃←-%s장%s-→"%(color,color_end), end="")
    elif peice == 3:
        print("┃  %s상%s  "%(color,color_end), end="")
    elif peice == 4:
        print("┃  %s자%s  "%(color,color_end), end="")
    elif peice == 5:
        print("┃←-%s후%s-→"%(color,color_end), end="")
    else:
        print("┃      ", end="")

def MID2(row,column, Num):
    turn = Board[row][column][0]
    peice = Board[row][column][1]
    if turn == 1:
        color = '\x1b[1;30;41m'
    else:
        color = '\x1b[1;30;44m'
    color_end = '\x1b[0m'

    if not 1<=Num<=9:
        Num = 0;
    if peice == 1:
        print("┃←-%s왕%s-→"%(color,color_end), end="")
    elif peice == 2:
        print("┃←-%s장%s-→"%(color,color_end), end="")
    elif peice == 3:
        print("┃  %s상%s  "%(color,color_end), end="")
    elif peice == 4:
        print("┃  %s자%s  "%(color,color_end), end="")
    elif peice == 5:
        print("┃←-%s후%s-→"%(color,color_end), end="")
    else:
        if Num:
            color = '\x1b[1;30;43m'
        else :
            color = ""
        print("┃  %s%s%s  " % (color,To_char[Num],color_end), end="")

'''
↖ㅣ↗
─□─
↙ㅣ↘
'''
#２ㅁ2
def BOT(row,column):
    turn = Board[row][column][0]
    peice = Board[row][column][1]
    if peice == 1:
        print("┃↙∨↘", end="")
    elif peice == 2:
        print("┃  ∨  ", end="")
        pass
    elif peice == 3:
        print("┃↙  ↘", end="")
        pass
    elif peice == 4 :
        if turn == 1:
            print("┃  ∨  ", end="")
            pass
        else:
            print("┃      ", end="")
            pass
    elif peice == 5:
        if turn == 1:
            print("┃↙∨↘", end="")
            pass
        else:
            print("┃  ∨  ", end="")
            pass
    else:
        print("┃      ", end="")
        pass


def print_repeat(count, char):
    for i in range(count):
        print(char, end='')
#
# def print_row(type, row):
#     if type==0:
#         for i in range(3):
#             print("│", end='')
#             print_repeat(3,'□')
#         print("│", end='')
#     elif type==1:
#         for i in range(3):
#             print("│", end='')
#             print_repeat(1, '□')
#             print(Board[row][i][1], end='')
#             print_repeat(1, '□')
#
#         print("│", end='')
#     print()

def INPUT(turn):
    input("인풋: ")

def PROCESS_PUT(turn, piece, row, column):
    user_name = None
    piece_code = 0
    if turn == 2:
        user_name = B
    elif turn == 1:
        user_name = A

    if piece == '장':
        piece_code = 2;
        user_name.jang -= 1
    elif piece == '상':
        piece_code = 3;
        user_name.sang -= 1
    elif piece == '자':
        piece_code = 4;
        user_name.ja -= 1

    Board[row][column] = [turn, piece_code] #입력 필터링 가정

'''
빈 공간에 사용자(turn)의
말(piece)를 놓음 -> user클래스의 해당(piece_code) 말 하나 감소!
Board 배열 좌표(coordi)에 [사용자, 말] 대입!
턴을 마친다
'''






# input
def Input(turn):
    s_x = -1
    s_y = -1
    print('[이동할 말]')
    count = 1
    choice = []
    if turn == 1:
        user = A
    elif turn == 2:
        user = B
    for row in range(4):
        for col in range(3):
            if Board[row][col][0] == turn:
                if Board[row][col][1] == 1:
                    choice.append([row, col, Board[row][col][1]])
                    print(count, ":", '왕')
                elif Board[row][col][1] == 2:
                    choice.append([row, col, Board[row][col][1]])
                    print(count, ":", '장')
                elif Board[row][col][1] == 3:
                    choice.append([row, col, Board[row][col][1]])
                    print(count, ":", '상')
                elif Board[row][col][1] == 4:
                    choice.append([row, col,Board[row][col][1]])
                    print(count, ":", '자')
                elif Board[row][col][1] == 5:
                    choice.append([row, col, Board[row][col][1]])
                    print(count, ":", '후')
                count += 1
    print('[새로 놓을 말]')
    if user.sang > 0:
        print('상 : ', user.sang, '개')
    if user.jang > 0:
        print('장 : ', user.jang, '개')
    if user.ja > 0:
        print('자 : ', user.ja, '개')

    while 1:
        user_input = input('원하는 동작을 선택하세요: ')
        if user_input =='장' or user_input =='상' or user_input =='자':
            process = 1
            VIEW_process(turn)
            try:
                position = int(input('놓을 위치를 선택하세요'))
            except:
                print('숫자를 입력하세요')
                continue
            if turn ==1:
                if position==1:
                    d_x = 0
                    d_y = 2
                if position==2:
                    d_x = 1
                    d_y = 2
                if position==3:
                    d_x = 2
                    d_y = 2
                if position==4:
                    d_x = 0
                    d_y = 1
                if position==5:
                    d_x = 1
                    d_y = 1
                if position==6:
                    d_x = 2
                    d_y = 1
                if position==7:
                    d_x = 0
                    d_y = 0
                if position==8:
                    d_x = 1
                    d_y = 0
                if position==9:
                    d_x = 2
                    d_y = 0
            elif turn == 2:
                if position == 1:
                    d_x = 0
                    d_y = 3
                if position == 2:
                    d_x = 1
                    d_y = 3
                if position == 3:
                    d_x = 2
                    d_y = 3
                if position == 4:
                    d_x = 0
                    d_y = 2
                if position == 5:
                    d_x = 1
                    d_y = 2
                if position == 6:
                    d_x = 2
                    d_y = 2
                if position == 7:
                    d_x = 0
                    d_y = 1
                if position == 8:
                    d_x = 1
                    d_y = 1
                if position == 9:
                    d_x = 2
                    d_y = 1
            if user_input == '장' and user.jang > 0:
                kind = 2
                break
            elif user_input == '상' and user.sang > 0:
                kind = 3
                break
            elif user_input == '자' and user.ja > 0:
                kind = 4
                break
        else:
            try:
                if 0 < int(user_input) <= len(choice):
                    process = 2
                    s_y = choice[int(user_input) - 1][0]
                    s_x = choice[int(user_input) - 1][1]
                    kind = choice[int(user_input) - 1][2]
                    while 1:
                        try:
                            direction = int(input('이동할 방향을 선택하세요:(1~9, 5제외)'))
                        except:
                            print('숫자를 입력하세요')
                            continue
                        if 1<=direction<=9 and direction !=5:
                            if direction == 1:
                                d_y = s_y + 1
                                d_x = s_x - 1
                            elif direction == 2:
                                d_y = s_y + 1
                                d_x = s_x
                            elif direction == 3:
                                d_y = s_y + 1
                                d_x = s_x + 1
                            elif direction == 4:
                                d_y = s_y
                                d_x = s_x - 1
                            elif direction == 6:
                                d_y = s_y
                                d_x = s_x + 1
                            elif direction == 7:
                                d_y = s_y - 1
                                d_x = s_x - 1
                            elif direction == 8:
                                d_y = s_y - 1
                                d_x = s_x
                            elif direction == 9:
                                d_y = s_y - 1
                                d_x = s_x + 1
                            break
                        print('잘못된 입력값입니다.')
                    break
            except:
                print('올바른 값을 입력하세요')
                continue
    return process, kind, s_x, s_y, d_x, d_y


# process

def change_turn():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1


def put_permitted1(d_x, d_y, kind):
    Board[d_y][d_x][0] = 1
    Board[d_y][d_x][1] = kind
    change_turn()
def put_permitted2(d_x,d_y,kind):
    Board[d_y][d_x][0] = 2
    Board[d_y][d_x][1] = kind
    change_turn()


def put(d_x, d_y, kind):
    if turn == 1:

        if not (0 <= d_x <= 2 and 0 <= d_y <= 3 and type(d_x) == int and type(d_y) == int and Board[d_y][d_x][0] == 0):
            print("올바른 곳에 놓아주세요")
            return
        elif A.jang != 0 and kind == 2:
            A.jang -= 1
            put_permitted1(d_x, d_y, kind)

        elif A.sang != 0 and kind == 3:
            A.sang -= 1
            put_permitted1(d_x, d_y, kind)
        elif A.ja != 0 and kind == 4:
            A.ja -= 1
            put_permitted1(d_x, d_y, kind)
        else:
            print("놓을 말을 가지고 있지 않습니다.")

    else:
        if not (0 <= d_x <= 2 and 0 <= d_y <= 3 and type(d_x) == int and type(d_y) == int and Board[d_y][d_x][0] == 0):
            print("올바른 좌표를 입력하세요")

        elif B.jang != 0 and kind == 2:
            B.jang -= 1
            put_permitted2(d_x, d_y, kind)

        elif B.sang != 0 and kind == 3:
            B.sang -= 1
            put_permitted2(d_x, d_y, kind)
        elif B.ja != 0 and kind == 4:
            B.ja -= 1
            put_permitted2(d_x, d_y, kind)
        else:
            print("놓을 말을 가지고 있지 않습니다.")


def catch(s_x, s_y, d_x, d_y):
    if Board[d_y][d_x][0] != Board[s_y][s_x][0]:
        if Board[d_y][d_x][0] == 1:
            if Board[d_y][d_x][1] == 2:
                B.jang += 1
            elif Board[d_y][d_x][1] == 3:
                B.sang += 1
            elif Board[d_y][d_x][1] == 4 or Board[d_y][d_x][1] == 5:
                B.ja += 1

        elif Board[d_y][d_x][0] == 2:
            if Board[d_y][d_x][1] == 2:
                A.jang += 1
            elif Board[d_y][d_x][1] == 3:
                A.sang += 1
            elif Board[d_y][d_x][1] == 4 or Board[d_y][d_x][1] == 5:
                A.ja += 1


def move_permitted(s_x, s_y, d_x, d_y):
    catch(s_x, s_y, d_x, d_y)
    Board[d_y][d_x][0] = Board[s_y][s_x][0]
    Board[d_y][d_x][1] = Board[s_y][s_x][1]
    Board[s_y][s_x] = [0, 0]
    change_turn()


def move(s_x, s_y, d_x, d_y):
    if not (0 <= s_x <= 2) or not (0 <= d_x <= 2) or not (0 <= s_y <= 3) or not (0 <= d_y <= 3) \
            or type(d_x) != int or type(d_y) != int or type(s_x) != int or type(s_y) != int or (
            d_x == s_x and d_y == s_y):
        print('올바른 좌표를 입력하세요')
        return

    if Board[d_y][d_x][0] == Board[s_y][s_x][0] and Board[d_y][d_x][0] != 0:
        print("같은 팀이 있는 곳으로 움직일 수 없습니다.")
        return

    # 왕
    if Board[s_y][s_x][1] == 1:
        if -1 <= d_x - s_x <= 1 and -1 <= d_y - s_y <= 1:
            move_permitted(s_x, s_y, d_x, d_y)
        else:
            print("그 곳으로 움직일 수 없습니다")



    # 장
    elif Board[s_y][s_x][1] == 2:
        if (abs(d_x - s_x) == 1 and d_y - s_y == 0) or (d_x - s_x == 0 and abs(d_y - s_y) == 1):
            move_permitted(s_x, s_y, d_x, d_y)
        else:
            print("그 곳으로 움직일 수 없습니다")

    # 상
    elif Board[s_y][s_x][1] == 3:
        if abs(d_x - s_x) == 1 and abs(d_y - s_y) == 1:
            move_permitted(s_x, s_y, d_x, d_y)
        else:
            print("그 곳으로 움직일 수 없습니다")

    # 자
    elif Board[s_y][s_x][1] == 4:

        if Board[s_y][s_x][0] == 1:
            if d_y - s_y == 1:
                if d_y == 3:
                    catch(s_x, s_y, d_x, d_y)
                    Board[d_y][d_x][0] = Board[s_y][s_x][0]
                    Board[s_y][s_x] = [0, 0]
                    Board[d_y][d_x][1] = 5
                    change_turn()

                else:
                    move_permitted(s_x, s_y, d_x, d_y)

        elif Board[s_y][s_x][0] == 2:
            if d_y - s_y == -1:
                if d_y == 0:
                    catch(s_x, s_y, d_x, d_y)
                    Board[d_y][d_x][0] = Board[s_y][s_x][0]
                    Board[s_y][s_x] = [0, 0]
                    Board[d_y][d_x][1] = 5
                    change_turn()

                else:
                    move_permitted(s_x, s_y, d_x, d_y)
        else:
            print("그 곳으로 움직일 수 없습니다")


    # 후
    elif Board[s_y][s_x][1] == 5:
        if Board[s_y][s_x][0] == 1:
            if abs(d_x - s_x) <= 1 and abs(d_y - s_y) <= 1 and not (abs(d_x - s_x) == 1 and d_y - s_y == 1):
                move_permitted(s_x, s_y, d_x, d_y)

        elif Board[s_y][s_x][0] == 2:
            if abs(d_x - s_x) <= 1 and abs(d_y - s_y) <= 1 and not (abs(d_x - s_x) == 1 and d_y - s_y == -1):
                move_permitted(s_x, s_y, d_x, d_y)
        else:
            print("그 곳으로 움직일 수 없습니다")


def printBoard(Board):
    print(Board[0])
    print(Board[1])
    print(Board[2])
    print(Board[3])


def printuser():
    print('A.wang:' + str(A.wang) + '    B.wang:' + str(B.wang))
    print('A.jang:' + str(A.jang) + '    B.jang:' + str(B.jang))
    print('A.sang:' + str(A.sang) + '    B.sang:' + str(B.sang))
    print('A.ja:' + str(A.ja) + '      B.ja:' + str(B.ja))


def process(process_kind, kind, s_x, s_y, d_x, d_y):
    if process_kind == 1:
        put(d_x, d_y, kind)

    else:
        move(s_x, s_y, d_x, d_y)


# 0 반복 1 게임 끝

def judge():
    global aliveA
    global aliveB
    global countA
    global countB
    for i in Board:
        for j in i:
            if j == [2, 1]:
                countB = 1
    if countB != 1:
        print('플레이어2의 왕이 죽었습니다.')
        print('플레이어1 승리!')
        return 1

    for i in Board:
        for j in i:
            if j == [1, 1]:
                countA = 1
    if countB != 1:
        print('플레이어1의 왕이 죽었습니다.')
        print('플레이어2 승리!')
        return 1

    countB = 0
    countA = 0

    for i in Board[0]:
        if i == [2, 1]:
            if aliveA == 1:
                print("플레이어2의 왕이 적진에서 생존했습니다.")
                print("플레이어2 승리!")
                return 1
            else:
                aliveA = 1

    for i in Board[3]:
        if i == [1, 1]:
            if aliveB == 1:
                print("플레이어1의 왕이 적진에서 생존했습니다.")
                print("플레이어1 승리!")
                return 1
            else:
                aliveB = 1
    return 0


# while 1:
#     print (turn)
#     process(*Input(turn))
#     printBoard(Board)
#     printuser()
#     if judge():
#         break

while True:
    print("───────────────────")
    print("1: 게임 시작\n2: 게임 종료")
    a_1 = int(input())
    if a_1 == 2:
        break;
    else:
        while True:
            VIEW2();
            if turn==2:
                color = '\x1b[1;30;44m'
                color_end = '\x1b[0m'
                print("++++++++%sB의 턴%s++++++++"%(color,color_end))
            else:
                color = '\x1b[1;30;41m'
                color_end = '\x1b[0m'
                print("++++++++%sA의 턴%s++++++++"%(color,color_end))
            process(*Input(turn))
            if judge():
                break

