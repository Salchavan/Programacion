import tkinter as tk
import os

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Contador de 10 segundos")
ventana.geometry("300x150")

# Configuración del contador
contador = 5  # segundos

# Creación de una etiqueta para mostrar el contador
etiqueta_contador = tk.Label(ventana, text=str(contador), font=("Arial", 30))
etiqueta_contador.pack(pady=20)

# Función para actualizar el contador cada segundo
def actualizar_contador():
    global contador
    
    # Actualiza el valor del contador y la etiqueta
    contador -= 1
    etiqueta_contador.config(text=str(contador))
    
    # Si el contador llega a cero, detiene el temporizador y apaga el equipo
    if contador == 0:
        ventana.after_cancel(id_temporizador)
        etiqueta_contador.config(text="¡Apagando el equipo!")
        os.system("shutdown -s -t 0")
        return
    
    # Configura la función para que se llame a sí misma después de 1 segundo
    id_temporizador = ventana.after(1000, actualizar_contador)

# Inicia el temporizador
id_temporizador = ventana.after(1000, actualizar_contador)

# Ejecuta la ventana
ventana.mainloop()
