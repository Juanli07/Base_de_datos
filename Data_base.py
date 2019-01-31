from Tkinter import *
def PrincipalWindow():
    window = Tk()
    window.geometry('900x700')
    window.configure(bg = 'beige')
    window.title('Data base')
    Button(window, text = 'Alta', command = quit).place(x= 100, y =600)
    Button(window, text = 'Baja', command = quit).place(x= 150, y =600)
    Button(window, text = 'Administrar', command = quit).place(x= 200, y =600)
    window.mainloop()

def Login():
    window = Tk()
    window.geometry('200x150')
    window.configure(bg = 'beige')
    window.title('Inicia Sesion')
    Label(window, text = 'Usuario :').pack()
    name = StringVar()
    Entry(window, justify = CENTER, textvariable = name).pack()
    Label(window, text = 'Contrasena :').place(x=60, y=50)
    password = StringVar()
    Entry(window, show = '*', justify = CENTER, textvariable = password).place(x = 17, y = 70)
    Button(window, text = 'Entrar', command = PrincipalWindow).place(x = 65, y = 100)
    window.mainloop()

Login()

#Campo de texto
#n1 = StringVar()
#Entry(window, justify = CENTER, textvariable=n1).pack()