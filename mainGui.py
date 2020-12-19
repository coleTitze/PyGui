import tkinter as tk
from TkColor import *
from GridSetup import *

mainGrid = GridSetup(tk, tk.Tk())

mainGrid.makeFirstColumn()
mainGrid.makeSecondColumn()
mainGrid.makeAddGroupButton()
mainGrid.makeAddReminderButton()

mainGrid.getWindow().mainloop()
