# importing tkinter gui module
import tkinter

#initialize gui
window = tkinter.Tk()
window.minsize(width = 500, height = 300)

#label
my_lable = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_lable.pack(side="left")






window.mainloop()
