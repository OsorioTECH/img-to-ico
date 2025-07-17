# filename: conversor_ico.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os

class IcoConverterApp:
    """
    Una aplicación de escritorio para convertir archivos de imagen a formato .ico.
    """
    def __init__(self, root):
        """
        Inicializa la aplicación, configurando la ventana principal y los widgets.
        """
        self.root = root
        self.root.title("Conversor de Imagen a .ICO")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        # Variables para almacenar las rutas
        self.image_path = tk.StringVar()
        self.output_folder = tk.StringVar()
        
        # Estilo para los widgets
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=('Helvetica', 10), padding=5)
        style.configure('TLabel', font=('Helvetica', 10))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))

        # --- Creación de la Interfaz ---
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill="both")

        header_label = ttk.Label(main_frame, text="Convertidor de Imagen a Icono (.ico)", style='Header.TLabel')
        header_label.pack(pady=(0, 20))

        # --- Sección de Carga de Imagen ---
        load_frame = ttk.Frame(main_frame)
        load_frame.pack(fill='x', pady=5)
        
        load_button = ttk.Button(load_frame, text="1. Cargar Imagen", command=self.select_image)
        load_button.pack(side='left', padx=(0, 10))
        
        # Etiqueta para mostrar la ruta de la imagen seleccionada
        self.image_label = ttk.Label(load_frame, textvariable=self.image_path, wraplength=350, foreground="gray")
        self.image_path.set("Ninguna imagen seleccionada...")
        self.image_label.pack(side='left')

        # --- Sección de Selección de Carpeta de Salida ---
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill='x', pady=15)
        
        output_button = ttk.Button(output_frame, text="2. Seleccionar Carpeta", command=self.select_output_folder)
        output_button.pack(side='left', padx=(0, 10))
        
        # Etiqueta para mostrar la ruta de la carpeta de salida
        self.output_label = ttk.Label(output_frame, textvariable=self.output_folder, wraplength=350, foreground="gray")
        self.output_folder.set("Ninguna carpeta seleccionada...")
        self.output_label.pack(side='left')

        # --- Sección de Conversión ---
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill='x', pady=20)
        
        convert_button = ttk.Button(main_frame, text="¡Convertir a .ICO!", command=self.convert_to_ico)
        convert_button.pack(pady=10)

    def select_image(self):
        """
        Abre un diálogo para que el usuario seleccione un archivo de imagen.
        """
        # Tipos de archivo permitidos
        file_types = [
            ('Archivos de Imagen', '*.png *.jpg *.jpeg *.bmp *.gif'),
            ('Todos los archivos', '*.*')
        ]
        path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=file_types)
        
        if path:
            self.image_path.set(path)
            self.image_label.config(foreground="black")

    def select_output_folder(self):
        """
        Abre un diálogo para que el usuario seleccione una carpeta de destino.
        """
        path = filedialog.askdirectory(title="Selecciona la carpeta para guardar el icono")
        
        if path:
            self.output_folder.set(path)
            self.output_label.config(foreground="black")

    def convert_to_ico(self):
        """
        Realiza la conversión de la imagen al formato .ico si las rutas son válidas.
        """
        # Validar que se hayan seleccionado la imagen y la carpeta
        if not self.image_path.get() or "Ninguna" in self.image_path.get():
            messagebox.showwarning("Falta Información", "Por favor, selecciona primero una imagen.")
            return
            
        if not self.output_folder.get() or "Ninguna" in self.output_folder.get():
            messagebox.showwarning("Falta Información", "Por favor, selecciona una carpeta de destino.")
            return

        try:
            # Abrir la imagen con Pillow
            img = Image.open(self.image_path.get())
            
            # Obtener el nombre del archivo original sin la extensión
            filename = os.path.basename(self.image_path.get())
            name_without_ext, _ = os.path.splitext(filename)
            
            # Construir la ruta de salida completa para el archivo .ico
            ico_path = os.path.join(self.output_folder.get(), f"{name_without_ext}.ico")
            
            # Guardar la imagen en formato ICO.
            # Se pueden especificar varios tamaños para mayor compatibilidad.
            icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            img.save(ico_path, format='ICO', sizes=icon_sizes)
            
            messagebox.showinfo("Éxito", f"¡Conversión exitosa!\n\nIcono guardado en:\n{ico_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la conversión:\n\n{e}")

if __name__ == "__main__":
    # Crear la ventana principal y la aplicación
    root_window = tk.Tk()
    app = IcoConverterApp(root_window)
    root_window.mainloop()

