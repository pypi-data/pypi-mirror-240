#    Copyright 2023 Rushikesh Kundkar

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from operator import is_
import os
import random,sys
import tkinter as tk
from .config import *

# Suppress pygame welcome prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
cwd = os.getcwd()

# parse command arguments
def parse_args():
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--dim"):
                if(int(sys.argv[2]) > 2):
                    return int(sys.argv[2])
    return dimension

# game status
is_game_over = False
dimension = parse_args() 

# Inheriting Game Class from tk.Frame
class Game(tk.Frame):
    # Application start
    def __init__(self):
        tk.Frame.__init__(self)
        # Grid layout
        self.grid()

        # Window title
        self.master.title("2048")
        # Creating main Frame
        self.main_grid = tk.Frame(
            self, bg=GRID_COLOR, bd=3, width=100*(dimension+1), height=100*(dimension+1))  
        # Setting the frame layout to grid
        self.main_grid.grid(pady=(80, 0))

        # Make_GUI and StartGame
        self.make_GUI()
        self.start_game()

        # Binding keydown events
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    # UI related functions 
    
    # Construct main_grid cells,assign data to them,create a score label
    def make_GUI(self):
        # Game matrix
        self.cells = []
        for i in range(dimension):
            row = []
            for j in range(dimension):
                # Creating cell frames
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=EMPTY_CELL_COLOR,
                    width=100,
                    height=100
                )
                # set position and padding of cell
                cell_frame.grid(row=i, column=j, padx=5, pady=5)

                # label for value inside cell
                cell_number = tk.Label(self.main_grid, bg=EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)

                # The contents of cell
                cell_data = {"frame": cell_frame, "number": cell_number}
                # Insert the cell_data into the 4 x 4 matrix 
                row.append(cell_data)
            # append that matrix into the cells
            self.cells.append(row)  

        # Score header
        score_frame = tk.Frame(self)
        # Placing the score frame
        score_frame.place(relx=0.5, x=0,y=40, anchor="center")
        # Title label
        tk.Label(
            score_frame,
            text="Score",
            font=SCORE_LABEL_FONT
        ).grid(row=0)

        # Score Label
        self.score_label = tk.Label(score_frame, text="0", font=SCORE_FONT)
        self.score_label.grid(row=1)



    # Sets value of any two random cells to 2,initializes score and logical matrix  
    def start_game(self):
        # Create matrix of zeroes
        self.matrix = [[0] * dimension for _ in range(dimension)]

        # Placing the first '2' in random place in matrix
        row = random.randint(0, dimension - 1)  
        col = random.randint(0, dimension - 1)
        self.matrix[row][col] = 2

        # Configuring the cell color
        self.cells[row][col]["frame"].configure(bg=CELL_COLORS[2])
        
        # Configuring the content,color,font and background
        self.cells[row][col]["number"].configure(
            bg=CELL_COLORS[2],
            fg=CELL_NUMBER_COLORS[2],
            font=CELL_NUMBER_FONTS[2],
            text="2")

        # Check for another unfilled cell
        while (self.matrix[row][col] != 0):
            row = random.randint(0, dimension - 1)
            col = random.randint(0, dimension - 1)

        # Placing the another two
        self.matrix[row][col] = 2
        # Configuring the cell color
        self.cells[row][col]["frame"].configure(bg=CELL_COLORS[2])
        # Configuring the content,color,font and background
        self.cells[row][col]["number"].configure(
            bg=CELL_COLORS[2],
            fg=CELL_NUMBER_COLORS[2],
            font=CELL_NUMBER_FONTS[2],
            text="2")

        # Setting the initial score to 0
        self.score = 0


    # Matrix Manipulation Functions

    # Compress the non zero numbers into the one side of the board or matrix
    def stack(self):  
        new_matrix = [[0] * dimension for _ in range(dimension)]  # The Zero Matrix
        # Pushing all the elements to one side of the board
        for i in range(dimension):
            fill_position = 0
            for j in range(dimension):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        # Setting the new matrix
        self.matrix = new_matrix

    # Fuse two adjacent cells of same value
    def combine(self): 
        for i in range(dimension):
            for j in range(dimension - 1):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]


    # Reverse every row of matrix
    def reverse(self):
        new_matrix = []
        for i in range(dimension):
            new_matrix.append([])
            for j in range(dimension):
                # reverse the order
                new_matrix[i].append(self.matrix[i][dimension - 1 - j])

        # Setting the new matrix as self.matrix
        self.matrix = new_matrix

    # Transpose the existing matrix
    def transpose(self):
        new_matrix = [[0] * dimension for _ in range(dimension)]
        for i in range(dimension):
            for j in range(dimension):
                new_matrix[i][j] = self.matrix[j][i]
        
        # Setting the new matrix as self.matrix
        self.matrix = new_matrix


    # Add a new tile randomly to an empty cell
    def add_new_tile(self):
        if any(0 in row for row in self.matrix):
            row = random.randint(0, dimension - 1)
            col = random.randint(0, dimension - 1)
            # randomly searching for an empty cell
            while (self.matrix[row][col] != 0):
                row = random.randint(0, dimension - 1)
                col = random.randint(0, dimension - 1)
            # assigning any value from 2,4,8...1024 at that random cell
            self.matrix[row][col] = random.choice([2**i for i in range(1,10)])  

    # Update the GUI to match the logical matrix
    def update_GUI(self):
        for i in range(dimension):
            for j in range(dimension):
                cell_value = self.matrix[i][j]
                # If cell_value is 0 --> Add the GUI of an empty cell
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(
                        bg=EMPTY_CELL_COLOR, text="")

                # Else --> Add the GUI of respective value cell
                else:
                    # giving the background according to the cell value
                    self.cells[i][j]["frame"].configure(
                        bg=CELL_COLORS[cell_value])
                    # giving the foreground according to the cell value
                    self.cells[i][j]["number"].configure(
                        bg=CELL_COLORS[cell_value],
                        fg=CELL_NUMBER_COLORS[cell_value],  
                        font=CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value))

        # Updating the Score Label in GUI
        self.score_label.configure(text=self.score)
        # Updating the MainWindow GUI
        self.update_idletasks()


    # KeyDown events

    # left keydown
    def left(self, event):
        self.stack()    # to compress the non zero number into the left size
        self.combine()  # to combine the horizontal same cell into the one
        self.stack()    # to eliminate the newly created zero value cell
        self.add_new_tile() # To add a new tile to Window
        self.update_GUI()   # To update the GUI accordingly
        self.game_over()    # To check if the Game is Over

    # right keydown
    def right(self, event):
        # compress rightwards
        self.reverse()
        self.stack()

        self.combine() # combine tiles
        self.stack() # eliminate zero valued cells
        self.reverse() # restore the original order of matrix
        self.add_new_tile() # add a new tile
        self.update_GUI() # update GUI
        self.game_over() # To check if the Game is Over

    # up keydown
    def up(self, event):
        # compress upwards  
        self.transpose()
        self.stack()

        self.combine() # combine tiles
        self.stack() # eliminate zero valued cells
        self.transpose() # restore the original order of matrix
        self.add_new_tile() # add a new tile
        self.update_GUI() # update GUI
        self.game_over() # To check if the Game is Over


    # down keydown
    def down(self,event):
        # compress downwards
        self.transpose()
        self.reverse()
        self.stack()

        self.combine() # combine tiles
        self.stack() # eliminate zero valued cells

        # restore the original order of matrix
        self.reverse() 
        self.transpose() 
        
        self.add_new_tile() # add a new tile
        self.update_GUI() # update GUI
        self.game_over() # To check if the Game is Over


    # Check for Game_Over

    # check whether horizontal move exists
    def horizontal_move_exists(self):
        for i in range(dimension):
            for j in range(dimension - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    # check whether vertical move exists
    def vertical_move_exists(self):
        for i in range(dimension - 1):
            for j in range(dimension):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    # check if game is over (Win/Lose)
    def game_over(self):
        global is_game_over
        # Check any 2048 in row if yes display YOU WIN
        if any(2048 in row for row in self.matrix):
            # Creating a GameOver Frame
            game_over_frame = tk.Frame(self.main_grid, borderwidth=1)
            # Placing the GameOver Frame
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            # Creating and Rendering the Label inside Game Over Frame
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=WINNER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT).pack()                

        # Else if no move exist --> Show Game Over
        elif not any(0 in row for row in
                     self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            # Creating a GameOver Frame
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            # Placing the GameOver Frame
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            # Creating and Rendering the Label inside Game Over Frame
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=LOSER_BG,
                fg=GAME_OVER_FONT_COLOR,
                font=GAME_OVER_FONT).pack()
        
# Display the copyright text
def copyright():
    print(COPYRIGHT)

# Driver Code
def main():
    Game()