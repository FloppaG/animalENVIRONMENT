def gui():
  import tkinter as tk

  win = tk.Tk()
  win.title("GUI")

  apps = tk.Label(win, text="Apps")
  apps.pack()
  exit = tk.Button(win, text="Terminal")
  exit.pack()

  win.mainloop()

