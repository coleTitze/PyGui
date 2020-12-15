from TkColor import *


def makeFirstColumn(tk, window):
    for i in range(14):
        frame1 = tk.Frame(master=window, bg=constColorDict.get("discordBlack"))
        frame1.grid(row=i, column=0, sticky="nsew")
        window.rowconfigure(i, minsize=30)
    window.columnconfigure(0, minsize=70)


def makeSecondColumn(tk, window):
    for i in range(14):
        frame1 = tk.Frame(master=window, bg=constColorDict.get("discordDark"))
        frame1.grid(row=i, column=1, sticky="nsew")
        window.rowconfigure(i, minsize=30)
    window.columnconfigure(1, minsize=240)
