from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.config(bg='gray30')
ventana.wm_attributes('-alpha', 0.8)
#Indice
i = 0
#Entrada de texto
e_texto = Entry(ventana, font= ('Roboto 20'))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)


#funciones

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def resultadoZ():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

#Botones para números

boton1 = Button(ventana, text = '1', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = '2', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = '3', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = '4', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = '5', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = '6', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = '7', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = '8', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = '9', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = '0', bg='goldenrod2',  width = 16, height = 2, command = lambda: click_boton(0))

#Botones de texto

boton_borrar = Button(ventana, text = 'AC', bg='goldenrod2',  width = 5, height = 2, command = lambda: borrar())
boton_parentesis1 = Button(ventana, text = '(', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton('('))
boton_parentesis2 = Button(ventana, text = ')', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton(')'))
boton_punto = Button(ventana, text = '.', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton('.'))

#Botones funcionales

boton_div = Button(ventana, text = '/', bg='goldenrod2', width = 5, height = 2, command = lambda: click_boton('/'))
boton_mult = Button(ventana, text = '*', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton('*'))
boton_sum = Button(ventana, text = '+', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton('+'))
boton_rest = Button(ventana, text = '-', bg='goldenrod2',  width = 5, height = 2, command = lambda: click_boton('-'))
boton_igual = Button(ventana, text = '=', bg='DarkGoldenrod4',  width = 5, height = 2, command = lambda: resultadoZ())

#Agregar botones en pantalla.

boton_borrar.grid(row = 1, column= 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column= 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column= 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column= 3, padx = 3, pady = 5)

boton7.grid(row = 2, column= 0, padx = 5, pady = 5)
boton8.grid(row = 2, column= 1, padx = 5, pady = 5)
boton9.grid(row = 2, column= 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column= 3, padx = 5, pady = 5)

boton4.grid(row = 3, column= 0, padx = 5, pady = 5)
boton5.grid(row = 3, column= 1, padx = 5, pady = 5)
boton6.grid(row = 3, column= 2, padx = 5, pady = 5)
boton_sum.grid(row = 3, column= 3, padx = 5, pady = 5)

boton1.grid(row = 4, column= 0, padx = 5, pady = 5)
boton2.grid(row = 4, column= 1, padx = 5, pady = 5)
boton3.grid(row = 4, column= 2, padx = 5, pady = 5)
boton_rest.grid(row = 4, column= 3, padx = 5, pady = 5)

boton0.grid(row = 5, column= 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column= 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column= 3, padx = 5, pady = 5)


ventana.mainloop()