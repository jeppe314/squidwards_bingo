from data import board_data, draw_numbers

# These are all the winners
bingo_winners = []

# Let's make a class
class BingoBoard:
    def __init__(self, board_data):
        self.grid = [[{"number": 0, "selected": False} for _ in range(5)] for _ in range(5)]
        self.initialize_board(board_data)

    def initialize_board(self, board_data):
        # Initialize the board
        for i in range(5):
            for j in range(5):
                self.grid[i][j]["number"] = board_data[i][j]
        
    def mark_number(self, number):
        # Marks the drawn number on the bingoboard
        for row in range(5):
            for col in range(5):
                if self.grid[row][col]["number"] == number:
                    self.grid[row][col]["selected"] = True

    def has_bingo(self):
        #Checks if the board has bingo
        # Checks horizontally
        for row in self.grid:
            if all(cell["selected"] for cell in row):
                return True

        # Check vertically
        for col in range(5):
            if all(self.grid[row][col]["selected"] for row in range(5)):
                return True
        return False
    
    #Calculates the score of a board when bingo
    def bingo_score(self, last_num):
        not_selected_numbers = 0
        for row in self.grid:
            for cell in row:
                if not cell["selected"]:
                    not_selected_numbers += cell["number"]
        score = last_num * not_selected_numbers
        print("Score: ", last_num, " * ", not_selected_numbers, " = ", score, "\n")
        return score


    # Defines the string
    def __str__(self):
        border = "█" * 23  # Border made of solid blocks
        text = "Bingolotto".center(19)  # Centered text
        board_str = f"\033[44m{border}\033[0m\n"  # ANSI escape code for background color
        board_str += f"\033[44m█ {text} █\033[0m\n"  # Top border with centered text
        board_str += f"\033[44m{border}\033[0m\n"  # ANSI escape code for background color
        for row in self.grid:
            board_str += "█ "  # Left border
            for cell in row:
                number = cell["number"]
                selected = cell["selected"]
                if selected:
                    # ANSI escape code for red text on blue background
                    colored_number = f"\033[91;44m{number:^3}\033[0m"
                else:
                    colored_number = f"{number:^3}"
                board_str += colored_number + " "
            board_str += "█\n"  # Right border
        board_str += f"\033[44m{border}\033[0m\n"  # ANSI escape code for background color
        return board_str


# Create BingoBoards from the data
bingo_boards = [BingoBoard(board_data) for board_data in board_data]
        
    
### PLAY BALL ###

def playBingo():
    print("Starting the game...")
    for drawnNumber in draw_numbers:
        for board in bingo_boards:
            # If the board already has bingo we do nothing
            if not board.has_bingo():
                #If it doesnt have bingo we mark the number and see if that gave us bingo
                board.mark_number(drawnNumber)
                if(board.has_bingo()):
                    print(board)
                    board.bingo_score(drawnNumber)
                    bingo_winners.append(board)
        
playBingo()