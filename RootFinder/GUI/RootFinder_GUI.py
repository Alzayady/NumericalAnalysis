from tkinter import *

# Gui handler events
from RootFinder.GUI import Choosing_Interval_GUI
from RootFinder.GUI import Choosing_Method_GUI
from RootFinder.GUI.Plot import draw


def warn_error():
    global error_label
    error_label.pack()

def solve_equation(function_string):
    print(function_string)



def get_equation():
    eqn = equation_entry.get()
    print(eqn)
    if not eqn:
        warn_error()
        return None

    return str(equation_entry.get())


def solve_button_handler():
    eqn = get_equation()
    equation = equation_entry.get()
    solve_equation(equation)


def custom_solve_handler():
    methodsGUI = Tk()
    methodsGUI.title('choose the method type')
    Choosing_Method_GUI.Methods(methodsGUI,get_equation())
    methodsGUI.mainloop()
    return None

def draw_button_handler():
    draw(get_equation())




# Gui elements
window = Tk()
window.title("Root Finding")
window.geometry('500x500')
window.configure(bg= 'blue')


upFrame = Frame(window,bd = 1,bg= 'black')
upFrame.pack(fill = X,padx = 5, pady = 5)


# label
label = Label(upFrame, text="Enter your function")
label.pack(fill = X)

# the space where we put the equation
large_font = ('Verdana',20)
equation_entry = Entry(upFrame,font=large_font)
equation_entry.pack(fill = X)

error_label = Label(upFrame, text='check you entered valid function!', bg='black', fg='red')


buttonsframe = Frame(window, pady = '10',bg= 'blue')
buttonsframe.pack()

# solve button
solve_btn = Button(buttonsframe, text="Solve", command=solve_button_handler,bg= 'black',fg = 'orange', pady = '10')
# solve_btn.place(side =CENTER)
solve_btn.pack(fill = X)

# custom solve button (in case that the user want to choose a technique to solve the equation )
custom_solve_btn = Button(buttonsframe, text="custom Solve", command=custom_solve_handler,bg= 'black',fg = 'orange', pady = '10')
# custom_solve_btn.place(side =CENTER)
custom_solve_btn.pack(fill = X)

# drawing button
draw_btn = Button(buttonsframe, text="Plot", command=draw_button_handler,bg= 'black',fg = 'orange', pady = '10')
draw_btn.pack(fill = X)


# list box to show steps
step_list = Listbox(window, height = 200)
step_list.pack(side = 'bottom',fill = X)

# showing Gui elements in the window
window.mainloop()


