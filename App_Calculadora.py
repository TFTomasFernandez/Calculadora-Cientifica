import tkinter as tk
import math

# Función que procesa las operaciones matemáticas
def click_boton(valor):
    # Obtener el valor actual de la entrada
    actual = entrada.get()
    # Borrar el contenido actual de la entrada
    entrada.delete(0, tk.END)
    # Insertar el nuevo valor concatenado con el valor actual
    entrada.insert(tk.END, actual + valor)

# Función para calcular el resultado de la expresión en la entrada
def calcular():
    try:
        # Evaluar la expresión matemática en la entrada
        resultado = eval(entrada.get())
        # Borrar el contenido actual de la entrada
        entrada.delete(0, tk.END)
        # Insertar el resultado en la entrada
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        # En caso de error, mostrar "Error" en la entrada
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Función para aplicar una función científica a la entrada
def aplicar_funcion(funcion):
    try:
        # Convertir el valor de la entrada a float
        valor = float(entrada.get())
        # Aplicar la función científica al valor
        resultado = funcion(valor)
        # Borrar el contenido actual de la entrada
        entrada.delete(0, tk.END)
        # Insertar el resultado en la entrada
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        # En caso de error, mostrar "Error" en la entrada
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("400x600")
ventana.config(bg="#2C3E50")

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=('Arial', 24), width=16, borderwidth=5, bg="#ECF0F1", fg="#2C3E50", justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Estilos para los botones
button_config = {
    'font': ('Arial', 18),
    'width': 5,
    'height': 2,
    'bd': 1,
    'relief': 'ridge',
    'fg': '#ECF0F1',
    'bg': '#34495E',
    'activebackground': '#1ABC9C'
}

button_scientific_config = {
    'font': ('Arial', 15),
    'width': 5,
    'height': 2,
    'bd': 1,
    'relief': 'ridge',
    'fg': '#ECF0F1',
    'bg': '#16A085',
    'activebackground': '#1ABC9C'
}

# Crear botones para la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

fila = 1
columna = 0

# Crear y colocar los botones en la ventana
for boton in botones:
    tk.Button(ventana, text=boton, command=lambda b=boton: click_boton(b), **button_config).grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botones científicos
botones_cientificos = [
    ('sin', math.sin), ('cos', math.cos), ('tan', math.tan),
    ('sqrt', math.sqrt), ('log', math.log), ('exp', math.exp)
]

# Crear y colocar los botones científicos en la ventana
for i, (text, func) in enumerate(botones_cientificos):
    tk.Button(ventana, text=text, command=lambda f=func: aplicar_funcion(f), **button_scientific_config).grid(row=fila, column=i % 4, padx=5, pady=5)
    if i % 4 == 3:
        fila += 1

# Botón para calcular el resultado
tk.Button(ventana, text='=', command=calcular, **button_config).grid(row=fila, column=2, padx=5, pady=5)
# Botón para limpiar la entrada
tk.Button(ventana, text='C', command=limpiar, **button_config).grid(row=fila, column=3, padx=5, pady=5)

# Iniciar la aplicación
ventana.mainloop()
