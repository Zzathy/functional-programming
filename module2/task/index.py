import random

create_board = lambda width : [['_' for _ in range(width)] for _ in range(width)]

def generate_random_position(width):
    return random.randint(0, width - 1), random.randint(0, width - 1)

def initialize_board(width):
    board = create_board(width)
    player_x, player_y = generate_random_position(width)
    goal_x, goal_y = generate_random_position(width)
    while (player_x == goal_x and player_y == goal_y):
        goal_x, goal_y = generate_random_position(width)
    board[player_x][player_y] = 'A'
    board[goal_x][goal_y] = 'O'
    return board, player_x, player_y, goal_x, goal_y

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def main():
    width = int(input("Input board width: "))
    board, player_x, player_y, goal_x, goal_y = initialize_board(width)
    print("Welcome! To Move, use 'w' (up), 's' (down), 'a' (left), dan 'd' (right).")
    print_board(board)
    
    while True:
        move = input("Input move (w/a/s/d): ").lower()
        
        if move == 'w' and player_x > 0:
            board[player_x][player_y], board[player_x - 1][player_y] = board[player_x - 1][player_y], board[player_x][player_y]
            player_x -= 1
        elif move == 's' and player_x < width - 1:
            board[player_x][player_y], board[player_x + 1][player_y] = board[player_x + 1][player_y], board[player_x][player_y]
            player_x += 1
        elif move == 'a' and player_y > 0:
            board[player_x][player_y], board[player_x][player_y - 1] = board[player_x][player_y - 1], board[player_x][player_y]
            player_y -= 1
        elif move == 'd' and player_y < width - 1:
            board[player_x][player_y], board[player_x][player_y + 1] = board[player_x][player_y + 1], board[player_x][player_y]
            player_y += 1
        
        print_board(board)
        
        if player_x == goal_x and player_y == goal_y:
            print("Congrats, You win!")
            break

if __name__ == "__main__":
    main()
