# 비바라기 시전
    # 비구름 생성 -> create_cloud("init")
    # 구름 이동 -> move_cloud()

# 구름 이동 num_move만큼
    # 1. d(i) 방향으로 s(i)칸 이동 -> move() board 1,1과 n,n 이어서 처리
    # 2. 구름 칸에 비내리기해서 물의 양 증가 -> rain() -> add_water()
    # 3. 구름 사라지기 -> remove_cloud()
    # 4. 물이 증가한 칸에 물복사버그 마법 시전 -> water_copy_bug() -> get_diagonal(): board 잇지 않고 처리 -> add_water()
    # 5. 물이 2 이상인 칸에 구름 생성 후 물의 양 -2 -> create_cloud("새로운 구름") -> add_water()

# count_water()

import sys
input = sys.stdin.readline

def skill():
    create_cloud("init", [])
    move_cloud()


def create_cloud(when, visit_cloud):
    global cloud, board_size, init_cloud

    if when == "init":
        for r, c in init_cloud:
            cloud[r][c] = 1
    else:
        # 물이 2 이상인 칸에 구름 생성
        for i in range(board_size):
            for j in range(board_size):
                if not visit_cloud[i][j]:
                    if board[i][j] >= 2:
                        cloud[i][j] = 1
                        add_water(i, j, -2) # 물의 양 -2


def move_cloud():
    global board, move_info, num_move
    for i in range(num_move):
        direct, dist = move_info[i]
        move(dist, direct) # 1
        add_water_list, visit_cloud = rain() # 2,3
        water_copy_bug(add_water_list) # 4
        create_cloud("step_five", visit_cloud)

def move(distance, direction):
    global cloud, board_size, direction_key

    move_list = []
    for i in range(board_size):
        for j in range(board_size):
            if cloud[i][j]:
                row = (i + direction_key[direction - 1][0]*distance) % board_size
                col = (j + direction_key[direction - 1][1]*distance) % board_size
                cloud[i][j] = 0
                move_list.append((row, col))
    for r,c in move_list:
        cloud[r][c] = 1

def rain():
    global cloud, board_size
    add_water_list = []
    visit_cloud = [[0]*board_size for _ in range(board_size)]
    for i in range(board_size):
        for j in range(board_size):
            if cloud[i][j]:
                cloud[i][j] = 0 # 구름 사라지기
                add_water(i, j, 1)
                add_water_list.append((i,j))
                visit_cloud[i][j] = 1

    return add_water_list, visit_cloud


def add_water(row, col, num):
    global board
    board[row][col] += num


def water_copy_bug(add_water_list):
    global board_size, board

    for r, c in add_water_list:
        count_bucket = 0
        for i in range(4):
            row = r + direction_key[i*2+1][0]
            col = c + direction_key[i*2+1][1]
            if (0 <= row < board_size) and (0 <= col < board_size):
                if board[row][col]:
                    count_bucket += 1
        add_water(r, c, count_bucket)

def count_water():
    global board, board_size, amount_water

    for row in board:
        for water in row:
            amount_water += water


# 입력: n(보드 크기),m(이동 횟수)
    # 보드: A[r][c]는 물의 양
board_size, num_move = map(int, input().split())
direction_key = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]] # 0부터여서 홀수가 대각선
init_cloud = [(board_size-1, 0), (board_size-1, 1), (board_size-2, 0), (board_size-2, 1)]
board, move_info, cloud = [], [], [[0]*board_size for _ in range(board_size)]

amount_water = 0
for _ in range(board_size):
    board.append(list(map(int, input().split())))
for _ in range(num_move):
    distance, direction = map(int, input().split())
    move_info.append((distance, direction)) # tuple

skill()
count_water()
print(amount_water)