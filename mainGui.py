import tkinter as tk
from TkColor import *
from GridSetup import *

window = tk.Tk()
window.configure(bg=constColorDict.get("discordLight"))

makeFirstColumn(tk, window)
makeSecondColumn(tk, window)

addReminderButton = tk.Button(
    text="Add Reminder",
    highlightthickness=0,
    borderwidth=0,
    activebackground=constColorDict.get("discordHover"),
    activeforeground="white",
    bg=constColorDict.get("discordDark"),
    fg=constColorDict.get("discordText")
)
addReminderButton.grid(
    row=1,
    column=1,
    sticky="nsew"
)
window.mainloop()
