# Read the raw boards data
with open("boards.txt", "r") as file:
    text_data = file.read()

#Split the data into boards by empty lines
board_strings = text_data.strip().split('\n\n')

# Initialize an array of the data
board_data = []

# Loop through each board
for board_string in board_strings:
    
    # Split the board string into rows
    rows = board_string.strip().split('\n')
    
    # Initialize an empty array for the current board
    board = []

    # Split each row in board into array of numbers
    for row in rows:
        number_strings = row.split()
        board_row = list(map(int, number_strings))
        board.append(board_row)

    # Add board to boards
    board_data.append(board)

# Now, board_data contains a list of board arrays
def print_boards():
    for i, board in enumerate(board_data):
        print(f"Board {i + 1}:")
        for row in board:
            print(row)
        print()
        
# Use func if you want to see all the beautiful boards        
# print_boards()


# Aaaaand the draw numbers:    
draw_numbers = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]
