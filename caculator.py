import tkinter as tk
from tkinter.constants import *
from tkinter import *



def operation(input):
    global result
    result += str(input)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,result)

def clear_num():
    global result
    result = ""
    text_result.delete(1.0, "end")


def equal():
    global result
    print(type(eval(result)))
    result = str(eval(result))     # 'eval' function is used for evaluating the string expressions directly
    text_result.delete(1.0,"end")     # clear the content from the text_result widget and 1.0 is the standart index of beginning 
    text_result.insert(1.0, result)


window = tk.Tk()
window.title("Calculator")
window.resizable(False,False)
window.geometry('380x275')
window.iconbitmap('icon.ico')

result = ""

# input_frame = tk.Frame(window,height = 50, width= 30, )
# input_frame.pack(side=TOP)

# input_entry=Entry(input_frame, width= 50 ,bg = "white",bd = 0,justify= RIGHT, textvariable= input_text, font = ('arial', 18, 'bold'))
# input_entry.grid(row= 0, column= 0 )
# input_entry.pack(ipady=10)

text_result = tk.Text(window, width= 100, height= 2, font=('arial', 18, 'bold'))
text_result.grid()
text_result.pack()

button_frame= tk.Frame(window, height=200,width=350, bg = "")
button_frame.pack()


# first raw
btn_AC = Button(button_frame,bg="grey",text= "AC", width= 2, height=2, command=lambda : clear_num())
btn_AC.grid(row=0,column=0)
btn_divide = Button(button_frame,bg="grey",text= "/", width= 2, height=2, command= lambda : operation("/"))
btn_divide.grid(row=0,column=3)

#second raw
btn_7 = Button(button_frame,bg="grey",text= "7", width= 2, height=2,command= lambda : operation(7))
btn_7.grid(row=1,column=0)
btn_8 = Button(button_frame,bg="grey",text= "8", width= 2, height=2,command= lambda : operation(8))
btn_8.grid(row=1,column=1)
btn_9 = Button(button_frame,bg="grey",text= "9", width= 2, height=2,command= lambda : operation(9))
btn_9.grid(row=1,column=2)
btn_multi = Button(button_frame,bg="grey",text= "*", width= 2, height=2,command= lambda : operation("*"))
btn_multi.grid(row=1,column=3)

# third raw
btn_4 = Button(button_frame,bg="grey",text= "4", width= 2, height=2,command= lambda : operation(4))
btn_4.grid(row=2,column=0)
btn_5 = Button(button_frame,bg="grey",text= "5", width= 2, height=2,command= lambda : operation(5))
btn_5.grid(row=2,column=1)
btn_6 = Button(button_frame,bg="grey",text= "6", width= 2, height=2,command= lambda : operation(6))
btn_6.grid(row=2,column=2)
btn_minus = Button(button_frame,bg="grey",text= "-", width= 2, height=2,command= lambda : operation("-"))
btn_minus.grid(row=2,column=3)


# fourth raw
btn_1 = Button(button_frame,bg="grey",text= "1", width= 2, height=2,command= lambda : operation(1))
btn_1.grid(row=3,column=0)
btn_2 = Button(button_frame,bg="grey",text= "2", width= 2, height=2,command= lambda : operation(2))
btn_2.grid(row=3,column=1)
btn_3 = Button(button_frame,bg="grey",text= "3", width= 2, height=2,command= lambda : operation(3))
btn_3.grid(row=3,column=2)
btn_plus = Button(button_frame,bg="grey",text= "+", width= 2, height=2,command= lambda : operation("+"))
btn_plus.grid(row=3,column=3)

# fifth raw
btn_0 = Button(button_frame,bg="grey",text= "0", width= 2, height=2,command=lambda : operation(0))
btn_0.grid(row=4,column=0)
btn_dot = Button(button_frame,bg="grey",text= ".", width= 2, height=2,command=lambda : operation("."))
btn_dot.grid(row=4,column=1)
btn_equal = Button(button_frame,bg="grey",text= "=", width= 2, height=2,command= lambda: equal())
btn_equal.grid(row=4,column=3)

window.mainloop()



