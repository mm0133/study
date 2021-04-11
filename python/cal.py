'''
2016170994 김다민
교수님이 올려주신 exe파일을 토대로 기능적으로 최대한 비슷하게 만들었습니다.
모든 버튼은 정상적으로 작동하고 계산기의 크기를 고정시켰습니다.
def는 말씀하신데로 딱5개로 만들었습니다.
'''

from tkinter import *

window = None
displayLabel = None
equation = None
expression = ''


def clear():
    global expression
    expression=''
    equation.set('')

def result():
    global expression

    try:
        equation.set(eval(expression))

    except:
        equation.set('Error')

    expression = ''


def press(x):
    global expression

    expression=expression+x
    equation.set(expression)

def bs():
    global expression

    expression=expression[0:-1]
    equation.set(expression)



def setupGUI():
    global window
    global displayLabel
    global equation


    window = Tk()
    window.title('MyCal')
    window.resizable(False, False)
    equation = StringVar()
    equation.set('')



    displayLabel = Label(window, textvariable=equation,  relief=RAISED, width=17, anchor=E, font='Arial 20')
    displayLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    btn1 = Button(window, text='1', width=6, height=2, font='Arial 15', command=lambda:press('1'))
    btn2 = Button(window, text='2', width=6, height=2, font='Arial 15', command=lambda:press('2'))
    btn3 = Button(window, text='3', width=6, height=2, font='Arial 15', command=lambda:press('3'))
    btn4 = Button(window, text='4', width=6, height=2, font='Arial 15', command=lambda:press('4'))
    btn5 = Button(window, text='5', width=6, height=2, font='Arial 15', command=lambda:press('5'))
    btn6 = Button(window, text='6', width=6, height=2, font='Arial 15', command=lambda:press('6'))
    btn7 = Button(window, text='7', width=6, height=2, font='Arial 15', command=lambda:press('7'))
    btn8 = Button(window, text='8', width=6, height=2, font='Arial 15', command=lambda:press('8'))
    btn9 = Button(window, text='9', width=6, height=2, font='Arial 15', command=lambda:press('9'))
    btn0 = Button(window, text='0', width=6, height=2, font='Arial 15', command=lambda:press('0'))
    clearBtn = Button(window, text='C', width=6, height=2,fg='red', font='Arial 15', command=clear)
    resultBtn = Button(window, text='=', width=6, height=2,bg='yellow', font='Arial 15', command=result)
    addBtn = Button(window, text='+', width=6, height=2, font='Arial 15', fg='blue', command=lambda:press('+'))
    subBtn = Button(window, text='-', width=6, height=2, font='Arial 15', fg='blue', command=lambda:press('-'))
    mulBtn = Button(window, text='×', width=6, height=2, font='Arial 15', fg='blue', command=lambda:press('*'))
    divBtn = Button(window, text='÷', width=6, height=2, font='Arial 15', fg='blue', command=lambda:press('/'))

    pointbtn=Button(window, text='.', width=6, height=2, font='Arial 15',command=lambda:press('.'))
    bsbtn = Button(window, text='<', width=6, height=2, font='Arial 15', command=bs)
    percenbtn = Button(window, text='%', width=6, height=2, font='Arial 15',fg='blue', command=lambda:press('*0.01'))
    squarebtn = Button(window, text='X²', width=6, height=2, font='Arial 15',fg='blue', command=lambda:press('**2'))



    clearBtn.grid(row=1, column=0)
    bsbtn.grid(row=1, column=1)
    percenbtn.grid(row=1,column=2)

    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)

    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)

    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)

    pointbtn.grid(row=5, column=0)
    btn0.grid(row=5, column=1)
    resultBtn.grid(row=5, column=2)

    squarebtn.grid(row=1, column=3)
    addBtn.grid(row=2, column=3)
    subBtn.grid(row=3, column=3)
    mulBtn.grid(row=4, column=3)
    divBtn.grid(row=5, column=3)


setupGUI()
window.mainloop()