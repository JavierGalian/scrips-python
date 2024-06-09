import argparse
from module_downloads.downloads_videos_youtube import downloads_videos
import os

parser = argparse.ArgumentParser()

"""
Descarga videos de YouTube o convierte a MP3.

Opciones:
    -u URL: Ingresar URL de YouTube (entre comillas dobles).
    -a: Convertir el video a MP3 (no descarga el video, solo guarda el audio.mp3).
    -p PATH: Ingresar ruta donde guardar (entre comillas dobles).
"""

# Función para procesar la ruta de guardado
def process_path(path):
    """
    Procesa la ruta de guardado, la convierte a ruta absoluta y verifica su validez.

    Args:
        path (str): Ruta a procesar.

    Returns:
        str: Ruta absoluta válida.

    Raises:
        ValueError: Si la ruta no es válida.
    """

    try:
        return os.path.abspath(path)  # Convierte la ruta a ruta absoluta
    except FileNotFoundError:
        raise ValueError("Ruta no válida: {}".format(path)) from None  # Re-eleva la excepción original


parser.add_argument("-u", "--url", help="Ingresar url de youtube(Ingresar entre comillas doble)")
parser.add_argument("-a", "--convertir_mp3", action="store_true", help="Convertir el video a mp3(con comando -u URL no descargara el video directamente se guardara el audio.mp3)")
parser.add_argument("-p", "--path_save", help="Ingresar path de ruta donde guardar(ingresar entre comilla doble)")

args = parser.parse_args()
url = args.url
convert_to_mp3 = args.convertir_mp3
path_save = process_path(args.path_save)

# Descarga o conversión del video
try:
    downloads_videos(url, convert_to_mp3, path_save)
except Exception as e:
    print(f"Error: {e}")

