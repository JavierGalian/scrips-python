import tkinter as tk
from moviepy.editor import *
from tkinter import filedialog 

#Funcion para obtener la ruta del video
def get_video_file():
    root = tk.Tk()
    root.withdraw()
    filename = tk.filedialog.askopenfilename(title="Selecciona un video", filetypes=[("Archivos de video", "*.mp4")])
    return filename

def coverter_video_mp3(video_path=False, path_save_user=False):
    
    if (video_path):
        video_file = video_path
    else:
        #ruta del archivo del video
        video_file = get_video_file()

    #crea un clip del video
    video_clip = VideoFileClip(video_file)

    #extrae el audio del video
    audio_clip = video_clip.audio

    # Obtiene el nombre del archivo de video sin la extensión
    video_filename, _ = os.path.splitext(os.path.basename(video_file))

    if (path_save_user):
        default_download_path = path_save_user
    else:
        # Ruta de la carpeta de descarga predeterminada
        default_download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    os.chdir(default_download_path)

    # Escribe el audio en un archivo MP3, especificando la extensión
    audio_clip.write_audiofile(os.path.join(default_download_path, f"{video_filename}.mp3"), codec="libmp3lame")

    print(f"¡Conversión completada! Archivo: {default_download_path}")
