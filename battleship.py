import random

# Skapa brädet
def create_board(size):
    return [["O"] * size for _ in range(size)]

# Funktion för att printa brädet
def print_board(board):
    for row in board:
        print(" ".join(row))

# Funktion för en slumpmässig rad
def random_row(board):
    return random.randint(0, len(board) - 1)

# Funktion för en slumpmässig kolumn
def random_col(board):
    return random.randint(0, len(board[0]) - 1)

# Skapa brädet
board_size = 5
board = create_board(board_size)

# Slumpa plats för skeppet
ship_row = random_row(board)
ship_col = random_col(board)

# Printa var skeppet är placerat
print("Ship is at:", ship_row, ship_col)

# Steg 6-11: Användarens gissningar
attempts = 5
for attempt in range(attempts):
    print(f"\nFörsök {attempt + 1} av {attempts}")

    try:
        guess_row = int(input("Guess row (0-4): "))
        guess_col = int(input("Guess col (0-4): "))

        if guess_row not in range(board_size) or guess_col not in range(board_size):
            print("That is not even in the ocean!")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that already.")
        elif board[guess_row][guess_col] == "S":
            print("Congratulations, you sank the ship!")
            break
        else:
            print("Sorry, you missed!")
            board[guess_row][guess_col] = "X"
            print_board(board)
    except ValueError:
        print("Please enter a valid integer.")

    if attempt == attempts - 1:
        print("Sorry you lost!")
        board[ship_row][ship_col] = "S"
        print_board(board)

# Printa det slutliga brädet
print("\nSpelet är slut. Här är det slutliga brädet:")
print_board(board)