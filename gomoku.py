def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ' ':
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # Horizontal: x changes, y stays the same
    if d_x != 0 and d_y == 0:
        x_initial = x_end - length + 1
        if x_initial-1 >= 0 and x_end+1 < 8:
            if board[y_end][x_initial-1] == ' ':
                if board[y_end][x_end+1] == ' ':
                    return "OPEN"
                elif board[y_end][x_end+1] != ' ' or board[y_end][x_end+1] != board[y_end][x_end]:
                    return "SEMIOPEN"
            elif board[y_end][x_initial-1] != ' ':
                if board[y_end][x_end+1] == ' ':
                    return "SEMIOPEN"
                elif board[y_end][x_initial-1] != board[y_end][x_initial] or board[y_end][x_end+1] != ' ':
                    return "CLOSE"
            elif board[y_end][x_initial-1] != board[y_end][x_initial] and board[y_end][x_end+1] != board[x_initial][y_end]:
                return "CLOSE"

        elif x_initial-1 < 0:
            if board[y_end][x_end+1] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

        elif x_end+1 >= 8:
            if board[y_end][x_initial-1] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

    # Vertical: y changes, x stays the same
    elif d_y != 0 and d_x == 0:
        y_initial = y_end - length + 1
        if y_initial-1 >= 0 and y_end+1 < 8:
            if board[y_initial-1][x_end] == ' ':
                if board[y_end+1][x_end] == ' ':
                    return "OPEN"
                elif board[y_end+1][x_end] != ' ' or board[y_end+1][x_end] != board[y_initial][x_end]:
                    return "SEMIOPEN"
            elif board[y_initial-1][x_end] != ' ':
                if board[y_end+1][x_end] == ' ':
                    return "SEMIOPEN"
                elif board[y_end+1][x_end] != board[y_initial][x_end] or board[y_end+1][x_end] != ' ':
                    return "CLOSE"
            elif board[y_initial-1][x_end] != board[y_initial][x_end] and board[y_end+1][x_end] != board[y_initial][x_end]:
                return "CLOSE"

        elif y_initial-1 < 0:
            if board[y_end+1][x_end] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

        elif y_end+1 >= 8:
            if board[y_initial-1][x_end] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

    # Diagonal
    elif d_x != 0 and d_y != 0:
        x_initial = x_end - length + 1
        y_initial = y_end - length + 1

        if (d_x < 0 and d_y < 0) or (d_x > 0 and d_y > 0):
            if y_initial-1 >= 0 and x_initial-1 >= 0 and y_end+1 < 8 and x_end+1 < 8:
                if board[y_initial-1][x_initial-1] == ' ':
                    if board[y_end+1][x_end+1] == ' ':
                        return "OPEN"
                    elif board[y_end+1][x_end+1] != ' ' or board[y_end+1][x_initial-1] != board[y_initial][x_end]:
                        return "SEMIOPEN"
                elif board[y_initial-1][x_initial-1] != ' ':
                    if board[y_end+1][x_end+1] == ' ':
                        return "SEMIOPEN"
                    elif board[y_end+1][x_end+1] != board[y_initial][x_initial] or board[y_end+1][x_end+1] != ' ':
                        return "CLOSE"
                elif board[y_initial-1][x_initial-1] != board[y_initial][x_initial] and board[y_end+1][x_end+1] != board[y_initial][xinitial]:
                    return "CLOSE"

            elif (y_initial-1 < 0 or x_initial-1 < 0) and (x_end + 1 >= 8 or y_end+1 >= 8):
                return "CLOSE"
            else:
                return "SEMIOPEN"

        elif (d_x < 0 and d_y > 0) or (d_x > 0 and d_y < 0):
            if y_initial-1 >= 0 and x_initial-1 >= 0 and y_end+1 < 8 and x_end+1 < 8:
                if board[y_initial-1][x_end+1] == ' ':
                    if board[y_end+1][x_initial-1] == ' ':
                        return "OPEN"
                    elif board[y_end+1][x_initial-1] != ' ' or board[y_end+1][x_initial-1] != board[y_initial][x_end]:
                        return "SEMIOPEN"
                elif board[y_initial-1][x_end+1] != ' ':
                    if board[y_end+1][x_initial-1] == ' ':
                        return "SEMIOPEN"
                    elif board[y_end+1][x_initial-1] != board[y_initial][x_end] or board[y_end+1][x_initial-1] != ' ':
                        return "CLOSE"
                elif board[y_initial-1][x_end+1] != board[y_initial][x_end] and board[y_end+1][x_initial-1] != board[y_initial][x_end]:
                    return "CLOSE"

            elif (y_initial-1 < 0 or x_initial-1 < 0) and (x_end + 1 >= 8 or y_end+1 >= 8):
                return "CLOSE"
            else:
                return "SEMIOPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    row = []
    open_seq_count = 0
    semi_open_seq_count = 0
    count = 0 # the number of colours in a sequence

    # diagonal case
    if d_x != 0 and d_y != 0:
        for i in range(8):
            while 0 <= x_start <= len(board[0]) - 1 and 0 <= y_start <= len(board[0]) - 1:
                row.append([y_start, x_start])
                y_start += d_y
                x_start += d_x
        for i in range(len(row)):
            y = row[i][0]
            x = row[i][1]
            if board[y][x] == col:
                count += 1
            else:
                count = 0
            if count == length:
                if 0 <= x <= len(board[0]) - 2 and 0 <= y <= len(board[0]) - 2:
                    if board[y+d_y][x+d_x] != col:
                        if is_bounded(board, y, x, length, d_y, d_x) == "OPEN":
                            open_seq_count += 1
                        if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                            semi_open_seq_count += 1
                elif x > len(board[0]) - 2 or y > len(board[0]) - 2:
                    if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1

    # horizontal case
    elif d_x != 0 and d_y == 0:
        for i in range(len(board[0])):
            while x_start <= len(board[0]) - 1:
                row.append([y_start, x_start])
                y_start += d_y
                x_start += d_x
        for i in range(len(row)):
            y = row[i][0]
            x = row[i][1]
            if board[y][x] == col:
                count += 1
            else:
                count = 0
            if count == length:
                if 0 <= x < len(board[0]) - 2: ## checking to make sure it is the end of the sequence
                    if board[y+d_y][x+d_x] != col:
                        if is_bounded(board, y, x, length, d_y, d_x) == "OPEN":
                            open_seq_count += 1
                        if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                            semi_open_seq_count += 1
                elif x >= len(board[0]) - 2 or y >= len(board[0]) - 2:
                    if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1

    # vertical case
    elif d_y != 0 and d_x == 0:
        for i in range(len(board[0])):
            while y_start <= len(board[0]) - 1:
                row.append([y_start, x_start])
                y_start += d_y
                x_start += d_x
        for i in range(len(row)):
            y = row[i][0]
            x = row[i][1]
            if board[y][x] == col:
                count += 1
            else:
                count = 0
            if count == length:
                if 0 <= y < len(board[0]) - 1:
                    if board[y+d_y][x+d_x] != col:
                        if is_bounded(board, y, x, length, d_y, d_x) == "OPEN":
                            open_seq_count += 1
                        if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                            semi_open_seq_count += 1
                elif y >= len(board[0]) - 2:
                    if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):

    open_seq_count = 0
    semi_open_seq_count = 0

    a = []
    b = []
    c = []
    d = []

     #left up to right bot
    for i in range(0, len(board[0])):
        if i == 0:
            a.append(detect_row(board, col, i, 0, length, 1, 1))
        else:
            a.append(detect_row(board, col, i, 0, length, 1, 1))
            a.append(detect_row(board, col, 0, i, length, 1, 1))


    #left bot to right up
    for i in range(0, len(board[0])):
        if i == 0:
            b.append(detect_row(board, col, 0, i, length, 1, -1))
        else:
            b.append(detect_row(board, col, i, 0, length, 1, -1))
            b.append(detect_row(board, col, 0, i, length, 1, -1))

    # horizontal
    for i in range(0, len(board[0])):
        c.append(detect_row(board, col, i, 0, length, 0, 1))

    # vertical
    for i in range(0, len(board[0])):
        d.append(detect_row(board, col, 0, i, length, 1, 0))


    for a1 in range(len(a)):
        open_seq_count += a[a1][0]
        semi_open_seq_count += a[a1][1]
    for b1 in range(len(b)):
        open_seq_count += b[b1][0]
        semi_open_seq_count += b[b1][1]
    for c1 in range(len(c)):
        open_seq_count += c[c1][0]
        semi_open_seq_count += c[c1][1]
    for d1 in range(len(d)):
        open_seq_count += d[d1][0]
        semi_open_seq_count += d[d1][1]

    return open_seq_count, semi_open_seq_count

# It seems to work, but if it reaches (0, 0), it just start repetitively returning (0, 0) and make no other move
def search_max(board):
    move = 0
    move_y = -1
    move_x = -1
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]== ' ':
                if move_y == -1 and move_x == -1:
                    move_y = i
                    move_x = j
                    move = score(board)
                    continue

                board[i][j] = 'b'
                move = max(move, score(board))
                if move == score(board):
                    move_y = i
                    move_x = j
                    board[i][j] = ' '
                else:
                    board[i][j]= ' '

    return move_y,move_x



def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_win(board):
    empty = 0

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                empty += 1

    if empty == 0:
        return "DRAW"

    if is_close('b') == True:
        return "Black won"

    if detect_rows(board,'b',5) != (0,0):
        # there is at least 1 open or semiopen sequence of 5
        # problem if closed sequence of 5
        return "Black won"

    if is_close('w') == True:
        return "White won"

    elif detect_rows(board,'w',5) != (0,0):
        return "White won"
    else:
        return "Continue playing"

def is_close(col): # test for sequences of 5 that are closed
    L1 = [[3, 0], [4, 1], [5, 2], [6, 3], [7, 4]]
    n1 = 0
    L2 = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]
    n2 = 0
    L3 = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]]
    n3 = 0
    L4 = [[7, 3], [6, 4], [5, 5], [4, 6], [3, 7]]
    n4 = 0

    for i in range(0,len(L1)):
        y = L1[i][0]
        x = L1[i][1]
        if board[y][x] == col:
            n1 += 1

    for i in range(0,len(L2)):
        y = L2[i][0]
        x = L2[i][1]
        if board[y][x] == col:
            n2 += 1

    for i in range(0,len(L3)):
        y = L3[i][0]
        x = L3[i][1]
        if board[y][x] == col:
            n3 += 1

    for i in range(0,len(L4)):
        y = L4[i][0]
        x = L4[i][1]
        if board[y][x] == col:
            n4 += 1

    if (n1 == 5 or n2 == 5) or (n3 ==5 or n4 ==5):
        return True
    else:
        return False

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE1 for detect_row PASSED")
    else:
        print("TEST CASE1 for detect_row FAILED")

def test_detect_row2():
    board = make_empty_board(8)
    x = 5; y = 5; d_x = 1; d_y = 0; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y,0,length,d_y,d_x) == (0,1):
        print("TEST CASE2 for detect_row PASSED")
    else:
        print("TEST CASE2 for detect_row FAILED")

def test_detect_row3():
    board = make_empty_board(8)
    x = 1; y = 5; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y,x,length,d_y,d_x) == (0,1):
        print("TEST CASE3 for detect_row PASSED")
    else:
        print("TEST CASE3 for detect_row FAILED")

def test_detect_row4():
    board = make_empty_board(8)
    x = 1; y = 5; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y,x,length,d_y,d_x) == (0,1):
        print("TEST CASE4 for detect_row PASSED")
    else:
        print("TEST CASE4 for detect_row FAILED")

def test_detect_row5():
    board = make_empty_board(8)
    x = 5; y = 5; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y,x,length,d_y,d_x) == (0, 1):
        print("TEST CASE5 for detect_row PASSED")
    else:
        print("TEST CASE5 for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE1 for detect_rows PASSED")
    else:
        print("TEST CASE1 for detect_rows FAILED")

def test_detect_rows2():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 1; d_y = 0; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (0,1):
        print("TEST CASE2 for detect_rows PASSED")
    else:
        print("TEST CASE2 for detect_rows FAILED")

def test_detect_rows3():
    board = make_empty_board(8)
    x = 3; y = 1; d_x = 1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1, 0):
        print("TEST CASE3 for detect_rows PASSED")
    else:
        print("TEST CASE3 for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


if __name__ == "__main__":
    board = make_empty_board(8)
    print(some_tests())
    # x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    # x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    # print_board(board)
    # print(detect_row(board,"b",0,6,4,1,0))
    # print(detect_rows(board,"b",4))
    # print(score(board))
    # print(easy_testset_for_main_functions())
    # print(search_max(board))
    #
    # print(is_bounded(board, 3, 5, 3, 1, 0))
    # print(test_is_bounded())
    # print(is_empty(board))
    # print(test_detect_row())
    # print(test_detect_row2())
    # print(test_detect_row3())
    # print(test_detect_row4())
    print(test_detect_row5())
    # print(detect_rows(board, 'w', 3))
    # print(test_detect_rows())
    # print(test_detect_rows2())
    # print(test_detect_rows3())
    # print(test_search_max())
    # print(search_max(board)) # (5, 5)
    # print(is_win(board))
    board[3][0] ="w"
    board[4][1] ="w"
    board[5][2] ="w"
    board[6][3] ="w"
    board[7][4] ="w"
    print(is_close("w"))
    #is_win(board)
    some_tests()
