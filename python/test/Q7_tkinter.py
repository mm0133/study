from tkinter import *
from tkinter import messagebox

window = None



def setupGUI():
    global window
    window = Tk()
    window.title('final exam')
    title_label = Label(window, text='Talk Box', font='Arial 12 bold', width='30')
    yesNoButton = Button(window, text="Click me", width='10', font='Arial 14 bold', height='1', command=yesNoDialog)
    title_label.grid(row=0, column=0, padx=10, pady=10)
    yesNoButton.grid(row=1, column=0, padx=10, pady=10)


def yesNoDialog():
    ans = messagebox.askyesno("질문", "당신은 고대인 입니까?")
    if ans == True:
        messagebox.showinfo("와우", "저는 현대인 입니다.")
    else:
        messagebox.showinfo("ㅠㅠ", "저는 고대인 입니다.")





setupGUI()
window.mainloop()
