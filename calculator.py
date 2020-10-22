from tkinter import *

expression = ""

def input_number(number,equation):
   global expression
   expression = expression + number
   equation.set(expression)

def evaluate(equation):
   global expression
   result = str(eval(expression))
   equation.set(result)

def clear_all(equation):
   global expression
   expression = ''
   equation.set(expression)

def delete(equation):
   global expression
   expression = expression[:-1]
   equation.set(expression)


def main():
   root = Tk()
   root.title("Calculator")
   root.grid()
   equation = StringVar()
   equation.set(0)
   output_field = Label(root,textvariable = equation)
   output_field.grid(row = 0,columnspan = 4)
	# OutputLabel = Label(root,text = 'Output')
	# OutputLabel.grid(column = 0,row = 0)
   _CE = Button(root,text='CE',fg = 'white',bg = 'black',bd = '2',command = lambda:clear_all(equation),height= 2,width=6)
   _CE.grid(row=1,column = 0)
   _C = Button(root,text='C',fg = 'white',bg = 'black',bd = '2',command = lambda:clear_all(equation),height=2,width=6)
   _C.grid(row=1,column=1)
   _DEL = Button(root,text='DEL',fg = 'white',bg = 'black',bd = '2',command = lambda:delete(equation),height= 2,width=6)
   _DEL.grid(row = 1,column = 2)
   _DIV = Button(root,text='/',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('/',equation),height= 2,width=6)
   _DIV.grid(row = 1,column = 3)
   _7 = Button(root,text='7',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('7',equation),height= 2,width=6)
   _7.grid(row = 2,column = 0)
   _8 = Button(root,text='8',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('8',equation),height= 2,width=6)
   _8.grid(row = 2,column = 1)
   _9 = Button(root,text='9',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('9',equation),height= 2,width=6)
   _9.grid(row = 2,column = 2)
   _X = Button(root,text='X',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('*',equation),height= 2,width=6)
   _X.grid(row = 2,column = 3)   
   _4 = Button(root,text='4',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('4',equation),height= 2,width=6)
   _4.grid(row = 3,column = 0)
   _5 = Button(root,text='5',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('5',equation),height= 2,width=6)
   _5.grid(row = 3,column = 1)
   _6 = Button(root,text='6',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('6',equation),height= 2,width=6)
   _6.grid(row = 3,column = 2)
   _MIN = Button(root,text='-',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('-',equation),height= 2,width=6)
   _MIN.grid(row = 3,column = 3)
   _1 = Button(root,text='1',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('1',equation),height= 2,width=6)
   _1.grid(row = 4,column = 0)
   _2 = Button(root,text='2',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('2',equation),height= 2,width=6)
   _2.grid(row = 4,column = 1)
   _3 = Button(root,text='3',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('3',equation),height= 2,width=6)
   _3.grid(row = 4,column = 2)
   _PLUS = Button(root,text='+',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('+',equation),height= 2,width=6)
   _PLUS.grid(row = 4,column = 3)
   _0 = Button(root,text='0',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('0',equation),height= 2,width=6)
   _0.grid(row = 5,column = 1)
   _DOT = Button(root,text='.',fg = 'white',bg = 'black',bd = '2',command = lambda:input_number('.',equation),height= 2,width=6)
   _DOT.grid(row = 5,column = 2)
   _RES = Button(root,text='=',fg = 'white',bg = 'black',bd = '2',command = lambda:evaluate(equation),height= 2,width=6)
   _RES.grid(row = 5,column = 3)
   root.mainloop()
main()