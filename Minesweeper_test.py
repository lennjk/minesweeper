import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
        NavigationToolbar2Tk  # alter Name : NavigationToolbar2TkAgg
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
from tkinter import ttk
import random
from PIL import ImageTk, Image

class sudoku:

    def __init__(self, master=None):
        self.master = master
        self.introframe = tk.Frame(self.master, bg='gray15')
        self.displayframe1 = tk.Frame(self.master, bg='gray15')
        self.resultframe = tk.Frame(self.master, bg='gray15')

        self.setstage()


    def setstage(self):
        self.introframe.grid(row=0, column=0)
        self.label = tk.Label(self.introframe, text=f"Ayo waddup?!", bg="gray15", fg="gray85",
                              borderwidth=8,
                              height=0, font="bold")
        self.label.grid(row=0, column=0, ipadx=10)
        self.label = tk.Label(self.introframe, text=f" ", bg="gray15", fg="gray85",
                              borderwidth=8,
                              height=0, font="bold")
        self.label.grid(row=1, column=0, ipadx=10, pady=2)

        vlist = ["easy", "medium", "hard",
                 "expert"]
        vlist2 = ["5x10", "7x14", "10x20",
                 "12x24"]
        self.Combo = ttk.Combobox(self.introframe, values=vlist)
        self.Combo.set("Pick a Difficulty")
        self.Combo.grid(row=2, column=0, padx=50, pady=50)
        self.Combo2 = ttk.Combobox(self.introframe, values=vlist2)
        self.Combo2.set("Pick a map size")
        self.Combo2.grid(row=3, column=0, padx=50, pady=50)
        self.label = tk.Label(self.introframe, text=f" ", bg="gray15", fg="gray85",
                              borderwidth=8,
                              height=0, font="bold")
        self.label.grid(row=8, column=0, ipadx=10, pady=2)
        # print(self.Combo.get())
        self.butteingabe = tk.Button(self.introframe, text="Create Mine Field", command=self.createfield,
                                     relief=tk.RAISED, bd=6, font="bold")
        self.butteingabe.grid(row=9, column=0, columnspan=3, sticky="nsew")

        self.buttquit = tk.Button(self.introframe, text="Quit", command=self.master.quit, relief=tk.RAISED, bd=6,
                                  font="bold")
        self.buttquit.grid(row=10, column=0, columnspan=3, sticky="nsew")

    def createfield(self):

        global gridx
        global gridy

        if self.Combo2.get() == "5x10":
            gridx = 10
            gridy = 5
        elif self.Combo2.get() == "7x14":
            gridx = 14
            gridy = 7
        elif self.Combo2.get() == "10x20":
            gridx = 20
            gridy = 10
        elif self.Combo2.get() == "12x24":
            gridx = 24
            gridy = 12

        global numbofmines
        if self.Combo.get() == "easy":
            numbofmines = int(gridx * gridy * 0.1)
        elif self.Combo.get() == "medium":
            numbofmines = int(gridx * gridy * 0.15)
        elif self.Combo.get() == "hard":
            numbofmines = int(gridx * gridy * 0.2)
        elif self.Combo.get() == "expert":
            numbofmines = int(gridx * gridy * 0.25)

        gridsizearray = np.zeros([gridy, gridx], dtype=int)
        print(gridsizearray)
        minearray = gridsizearray
        global buttonarray
        buttonarray = gridsizearray

        j = 0
        while j != numbofmines:
            x = np.random.randint(0, gridy)
            y = np.random.randint(0, gridx)
            minearray[x][y] = -99
            j += 1

        global completearray
        completearray = minearray

        def create_completearray():
            for i in range(gridy):
                for j in range(gridx):
                    if completearray[i][j] < 0:
                        if i == 0:
                            completearray[i][j - 1] = completearray[i][j - 1] + 1
                            completearray[i][j + 1] = completearray[i][j + 1] + 1

                            completearray[i + 1][j - 1] = completearray[i + 1][j - 1] + 1
                            completearray[i + 1][j] = completearray[i + 1][j] + 1
                            completearray[i + 1][j + 1] = completearray[i + 1][j + 1] + 1

                        elif i == 0 and j == 0:
                            completearray[i][j + 1] = completearray[i][j + 1] + 1
                            completearray[i + 1][j] = completearray[i + 1][j] + 1
                            completearray[i + 1][j + 1] = completearray[i + 1][j + 1] + 1

                        elif i == gridy-1 and j == 0:
                            completearray[i - 1][j + 1] = completearray[i - 1][j + 1] + 1
                            completearray[i - 1][j] = completearray[i - 1][j] + 1

                            completearray[i][j + 1] = completearray[i][j + 1] + 1

                        elif j == 0:
                            completearray[i - 1][j] = completearray[i - 1][j] + 1
                            completearray[i - 1][j + 1] = completearray[i - 1][j + 1] + 1

                            completearray[i][j + 1] = completearray[i][j + 1] + 1

                            completearray[i + 1][j] = completearray[i + 1][j] + 1
                            completearray[i + 1][j + 1] = completearray[i + 1][j + 1] + 1

                        elif i == gridy-1:
                            completearray[i - 1][j - 1] = completearray[i - 1][j - 1] + 1
                            completearray[i - 1][j] = completearray[i - 1][j] + 1
                            completearray[i - 1][j + 1] = completearray[i - 1][j + 1] + 1

                            completearray[i][j - 1] = completearray[i][j - 1] + 1
                            completearray[i][j + 1] = completearray[i][j + 1] + 1

                        elif j == gridx-1:
                            completearray[i - 1][j - 1] = completearray[i - 1][j - 1] + 1
                            completearray[i - 1][j] = completearray[i - 1][j] + 1

                            completearray[i][j - 1] = completearray[i][j - 1] + 1

                            completearray[i + 1][j - 1] = completearray[i + 1][j - 1] + 1
                            completearray[i + 1][j] = completearray[i + 1][j] + 1

                        elif i == 0 and j == gridx-1:
                            completearray[i][j - 1] = completearray[i][j - 1] + 1

                            completearray[i + 1][j - 1] = completearray[i + 1][j - 1] + 1
                            completearray[i + 1][j] = completearray[i + 1][j] + 1

                        elif i == gridy-1 and j == gridx-1:
                            completearray[i - 1][j - 1] = completearray[i - 1][j - 1] + 1
                            completearray[i - 1][j] = completearray[i - 1][j] + 1

                            completearray[i][j - 1] = completearray[i][j - 1] + 1

                        else:

                            completearray[i - 1][j - 1] = completearray[i - 1][j - 1] + 1
                            completearray[i - 1][j] = completearray[i - 1][j] + 1
                            completearray[i - 1][j + 1] = completearray[i - 1][j + 1] + 1

                            completearray[i][j - 1] = completearray[i][j - 1] + 1
                            completearray[i][j + 1] = completearray[i][j + 1] + 1

                            completearray[i + 1][j - 1] = completearray[i + 1][j - 1] + 1
                            completearray[i + 1][j] = completearray[i + 1][j] + 1
                            completearray[i + 1][j + 1] = completearray[i + 1][j + 1] + 1

        create_completearray()

        # print(completearray)
        print(minearray)
        global victoryarray
        victoryarray = np.full([gridy, gridx], -99, dtype=int)
        print("Victory array \n", victoryarray)
        self.display()

    def display(self):
        self.resultframe.grid_remove()
        self.displayframe1.grid(row=0, column=1)

        for i in range(gridy):
            for j in range(gridx):
                self.placeholder = tk.Button(self.displayframe1,
                                             command=lambda row=i, column=j: self.checker(row, column),
                                             text=f" ", bg="gray15",
                                             fg="gray90", borderwidth=1, height=0, font="bold", width=3)
                self.placeholder.grid(row=i, column=j, padx=1, pady=1)

        self.displayframe1.focus_set()
        """
        def callback(event, row, column):
            print(row, column)

        self.displayframe1.bind("<Return>",
               lambda event, row=self.placeholder.grid_info()['row'], column=self.placeholder.grid_info()['column']: callback(event, row, column))
        """

        def mark(event):

            # Here retrieving the size of the parent
            # widget relative to master widget
            x = event.x_root - self.displayframe1.winfo_rootx()
            y = event.y_root - self.displayframe1.winfo_rooty()

            # Here grid_location() method is used to
            # retrieve the relative position on the
            # parent widget
            posy, posx = self.displayframe1.grid_location(x, y)

            # printing position
            print(posx, posy)
            iconforbutton = tk.PhotoImage(file="skull3.png")
            self.placeholder = tk.Button(self.displayframe1,
                                         command=lambda row=posx, column=posy: self.checker(row, column),
                                         image=iconforbutton, bg="gray15",
                                         fg="gray90", borderwidth=1, height=30, font="bold", width=30)
            self.placeholder.grid(row=posx, column=posy, padx=1, pady=1)

        self.displayframe1.bind("<space>", mark)

    def checker(self, row, column):
        print(row, column)

        def check_right_down():
            if completearray[row][column] == 0:
                for i in range(row, gridy):
                    if completearray[i][column] < 0:
                        break
                    elif completearray[i][column] == 0:
                        self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                    elif completearray[i][column] == 1:
                        self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 2:
                        self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 3:
                        self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed2", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 4:
                        self.label = tk.Label(self.displayframe1, text=f"4", bg="IndianRed3", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    for j in range(column, gridx):
                        if completearray[i][j] < 0:
                            break
                        elif completearray[i][j] == 0:
                            self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                        elif completearray[i][j] == 1:
                            self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 2:
                            self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 3:
                            self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed3", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        else:
                            self.label = tk.Label(self.displayframe1, text=f"{completearray[i][j]}", bg="gray35",
                                                  fg="gray90", borderwidth=1,
                                                  height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
        def check_right_up():
            xlist = list(range(0,row))
            xlist = reversed(xlist)
            if completearray[row][column] == 0:
                for i in xlist:
                    if completearray[i][column] < 0:
                        break
                    elif completearray[i][column] == 0:
                        self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                    elif completearray[i][column] == 1:
                        self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 2:
                        self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 3:
                        self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed2", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 4:
                        self.label = tk.Label(self.displayframe1, text=f"4", bg="IndianRed3", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    for j in range(column, gridx):
                        if completearray[i][j] < 0:
                            break
                        elif completearray[i][j] == 0:
                            self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                        elif completearray[i][j] == 1:
                            self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 2:
                            self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 3:
                            self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed3", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        else:
                            self.label = tk.Label(self.displayframe1, text=f"{completearray[i][j]}", bg="gray35",
                                                  fg="gray90", borderwidth=1,
                                                  height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
        def check_left_up():
            xlist = list(range(0,row))
            xlist = reversed(xlist)
            ylist = list(range(0, column+1))
            ylist = reversed(ylist)
            if completearray[row][column] == 0:
                for i in xlist:
                    if completearray[i][column] < 0:
                        break
                    elif completearray[i][column] == 0:
                        self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                    elif completearray[i][column] == 1:
                        self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 2:
                        self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 3:
                        self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed2", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 4:
                        self.label = tk.Label(self.displayframe1, text=f"4", bg="IndianRed3", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    for j in ylist:
                        if completearray[i][j] < 0:
                            break
                        elif completearray[i][j] == 0:
                            self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                        elif completearray[i][j] == 1:
                            self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 2:
                            self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 3:
                            self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed3", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        else:
                            self.label = tk.Label(self.displayframe1, text=f"{completearray[i][j]}", bg="gray35",
                                                  fg="gray90", borderwidth=1,
                                                  height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
        def check_left_down():
            ylist = list(range(0, column+1))
            ylist = reversed(ylist)
            if completearray[row][column] == 0:
                for i in range(row, gridy):
                    if completearray[i][column] < 0:
                        break
                    elif completearray[i][column] == 0:
                        self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                    elif completearray[i][column] == 1:
                        self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 2:
                        self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 3:
                        self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed2", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    elif completearray[i][column] == 4:
                        self.label = tk.Label(self.displayframe1, text=f"4", bg="IndianRed3", fg="gray90",
                                              borderwidth=1, height=0, font="bold", width=3)
                        self.label.grid(row=i, column=column, padx=1, pady=1)
                        victoryarray[i][column] = completearray[i][column]
                        break
                    for j in ylist:
                        if completearray[i][j] < 0:
                            break
                        elif completearray[i][j] == 0:
                            self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                        elif completearray[i][j] == 1:
                            self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 2:
                            self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        elif completearray[i][j] == 3:
                            self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed3", fg="gray90",
                                                  borderwidth=1, height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break
                        else:
                            self.label = tk.Label(self.displayframe1, text=f"{completearray[i][j]}", bg="gray35",
                                                  fg="gray90", borderwidth=1,
                                                  height=0, font="bold", width=3)
                            self.label.grid(row=i, column=j, padx=1, pady=1)
                            victoryarray[i][j] = completearray[i][j]
                            break

        check_right_down()
        check_right_up()
        check_left_up()
        check_left_down()

        if completearray[row][column] < 0:
            self.lose()
        elif completearray[row][column] == 0:
            self.label = tk.Label(self.displayframe1, text=f" ", bg="gray35", fg="gray90",
                                  borderwidth=1, height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]
        elif completearray[row][column] == 1:
            self.label = tk.Label(self.displayframe1, text=f"1", bg="yellow4", fg="gray90",
                                  borderwidth=1, height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]
        elif completearray[row][column] == 2:
            self.label = tk.Label(self.displayframe1, text=f"2", bg="dark orange", fg="gray90",
                                  borderwidth=1, height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]
        elif completearray[row][column] == 3:
            self.label = tk.Label(self.displayframe1, text=f"3", bg="IndianRed2", fg="gray90",
                                  borderwidth=1, height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]
        elif completearray[row][column] == 4:
            self.label = tk.Label(self.displayframe1, text=f"4", bg="IndianRed2", fg="gray90",
                                  borderwidth=1, height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]
        else:
            self.label = tk.Label(self.displayframe1, text=f"{completearray[row][column]}", bg="gray35",
                                  fg="gray90", borderwidth=1,
                                  height=0, font="bold", width=3)
            self.label.grid(row=row, column=column, padx=1, pady=1)
            victoryarray[row][column] = completearray[row][column]

        # print("Victory array \n", victoryarray)

        def check_victory():
            a = np.where(completearray < 0, -99, completearray)

            if (a == victoryarray).all() == True:
                self.victory()
            else:
                return

        check_victory()

    def lose(self):

        self.resultframe.grid(row=0, column = 1)
        self.my_image = ImageTk.PhotoImage(Image.open("blastlul2.png"))
        self.my_image_label = tk.Label(self.resultframe, image=self.my_image)
        self.my_image_label.grid(row=0, column=0, sticky="nsew")
        self.w = tk.Label(self.resultframe, text = "ah damn, well guess you died in a horrific explosion, unlucky...",
                          bg="IndianRed3", font="bold", fg="gray90")
        self.w.grid(row = 1, column = 0, sticky="nsew", ipady=20)

    def victory(self):

        self.resultframe.grid(row=0, column=1)
        self.my_image = ImageTk.PhotoImage(Image.open("catlul.png"))
        self.my_image_label = tk.Label(self.resultframe, image=self.my_image, bg="gray15")
        self.my_image_label.grid(row=0, column=0, sticky="nsew")
        self.w = tk.Label(self.resultframe, text="too damn easy",
                          bg="PaleGreen3", font="bold", fg="gray90")
        self.w.grid(row=1, column=0, sticky="nsew", ipady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background='gray15')
    root.wm_title("Minesweeper by Lenni")
    initialize = sudoku(master=root)
    root.geometry()
    root.mainloop()