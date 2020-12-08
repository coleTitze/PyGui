import tkinter as tk

window = tk.Tk()
window.configure(bg='#36393f')
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

addReminderButton = tk.Button(
    text="Add Reminder"
    width=10
    height=5
    
)
window.mainloop()