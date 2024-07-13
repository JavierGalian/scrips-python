import os
import uuid
import shutil
from tkinter import Tk, filedialog, simpledialog

def select_images():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    file_paths = filedialog.askopenfilenames(
        title="Selecciona imágenes",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.avif")]
    )
    return list(file_paths)

def rename_and_save_images(image_paths, output_dir, base_name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_path in image_paths:
        try:
            extension = os.path.splitext(image_path)[1]
            unique_id = uuid.uuid4().hex
            new_name = f"{base_name}-{unique_id}{extension}"
            new_path = os.path.join(output_dir, new_name)
            shutil.copy(image_path, new_path)
            print(f"Guardado en {new_path}")
        except Exception as e:
            print(f"Error al procesar {image_path}: {e}")

def main():
    print("Selecciona las imágenes a procesar.")
    image_paths = select_images()
    if not image_paths:
        print("No se seleccionaron imágenes.")
        return

    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    base_name = simpledialog.askstring("Nombre base", "Ingresa el nombre base para las imágenes:")
    if not base_name:
        print("No se ingresó un nombre base.")
        return

    output_dir = filedialog.askdirectory(title="Selecciona la carpeta de destino")
    if not output_dir:
        print("No se seleccionó una carpeta de destino.")
        return

    rename_and_save_images(image_paths, output_dir, base_name)
    print("Proceso completado.")

if __name__ == "__main__":
    main()
