import pytube
import os

from .convert_videos_to_mp3 import coverter_video_mp3

def downloads_videos(url, convert_to_mp3=False, path_save_user=False):

    video_youtube = pytube.YouTube(url)
    streams = video_youtube.streams.filter(progressive=True)

    if (convert_to_mp3):
        resolution_video_youtube = streams[-1]
    else:
        #Lsta de resolucion
        for stream in streams:
            print (f'[>]Resolucion: {stream.resolution}')

        resolution_video_youtube = input('[>] Ingresar resolucion del video: ')

    stream = streams.filter(resolution=resolution_video_youtube).first()

    
    if (path_save_user):
        default_download_path = path_save_user
    else:
        # Ruta de la carpeta de descarga predeterminada
        default_download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
    os.chdir(default_download_path)

    # Eliminar espacios del nombre del archivo
    filename_without_spaces = stream.default_filename.replace(" ", "-")

    # Descargar el video
    stream.download(filename=filename_without_spaces)

    if (convert_to_mp3):
        # Crear la ruta completa
        ruta_completa = os.path.join(default_download_path, filename_without_spaces)  # Usa os.path.join para generar la ruta correctamente
        coverter_video_mp3(ruta_completa, path_save_user)
    else:
        print(f'[-]Descarga completa:  {stream.default_filename}')


