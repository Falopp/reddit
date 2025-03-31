#!/usr/bin/env python3
import os
import requests
import time
import argparse
import logging
import shutil
import yt_dlp

def sanitize_filename(name, max_length=80):
    """Convierte un nombre en uno apto para usarse como nombre de archivo."""
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in name)[:max_length]

def get_posts(subreddit, limit, sort, time_filter, after=None):
    """
    Obtiene posts de un subreddit usando el método de ordenamiento indicado.
    Si se usa 'top', se añade el filtro de tiempo.
    """
    url = f"https://www.reddit.com/r/{subreddit}/{sort}.json?limit={limit}"
    if sort == "top":
        url += f"&t={time_filter}"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "reddit-downloader-script/0.1"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error al obtener posts: {e}")
        return None

def download_video(video_url, output_dir, title):
    """
    Descarga un video usando yt-dlp.
    Se asume que ffmpeg está instalado para fusionar audio y video.
    """
    sanitized_title = sanitize_filename(title)
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, f'{sanitized_title}.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            logging.info(f"Descargado video: {title}")
    except Exception as e:
        logging.error(f"Error al descargar el video '{title}': {e}")

def download_image(image_url, output_dir, title):
    """
    Descarga una imagen de la URL indicada y la guarda en el directorio output.
    """
    # Reemplaza entidades HTML
    image_url = image_url.replace("&amp;", "&")
    ext = os.path.splitext(image_url)[1].split("?")[0]
    if ext.lower() not in ['.jpg', '.jpeg', '.png']:
        ext = ".jpg"  # Valor por defecto si no se detecta extensión adecuada
    filename = f"{sanitize_filename(title)}{ext}"
    filepath = os.path.join(output_dir, filename)
    try:
        r = requests.get(image_url, stream=True, timeout=10)
        r.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        logging.info(f"Descargada imagen: {filename}")
    except requests.RequestException as e:
        logging.error(f"Error al descargar la imagen '{title}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Descargar imágenes y videos (con audio) de un subreddit en máxima calidad.")
    parser.add_argument('-s', '--subreddit', type=str, default="all", help="Subreddit del cual descargar contenido")
    parser.add_argument('-p', '--pages', type=int, default=3, help="Número de páginas a recorrer")
    parser.add_argument('-l', '--limit', type=int, default=100, help="Cantidad de posts por página")
    parser.add_argument('-o', '--output', type=str, default="downloaded_content", help="Directorio de salida")
    parser.add_argument('--sort', type=str, default="hot", choices=["hot", "new", "top", "controversial"], help="Orden de los posts")
    parser.add_argument('-t', '--time', type=str, default="all", help="Intervalo de tiempo para posts 'top' (all, day, week, month, year)")
    args = parser.parse_args()

    # Configuración del logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Se requiere ffmpeg para la fusión de audio y video
    if shutil.which("ffmpeg") is None:
        logging.error("ffmpeg no está instalado. Instálalo para poder descargar videos con audio.")
        exit(1)

    os.makedirs(args.output, exist_ok=True)
    after = None
    video_hosts = ["v.redd.it", "youtube", "youtu.be", "streamable", "gfycat"]

    for page in range(args.pages):
        logging.info(f"Procesando página {page+1} de {args.pages}")
        data = get_posts(args.subreddit, args.limit, args.sort, args.time, after)
        if data is None:
            logging.error("No se pudieron obtener datos de Reddit. Abortando.")
            break

        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after", None)

        if not posts:
            logging.info("No se encontraron más posts.")
            break

        for post in posts:
            post_data = post.get("data", {})
            title = post_data.get("title", "post")
            url = post_data.get("url", "")
            is_video = post_data.get("is_video", False)

            # Prioridad a videos: si el post es video o la URL indica video
            if is_video or any(host in url for host in video_hosts):
                logging.info(f"Descargando video: {title}")
                download_video(url, args.output, title)
            # Si hay preview con imagen, se usa esa versión (alta calidad)
            elif "preview" in post_data and "images" in post_data["preview"]:
                image_info = post_data["preview"]["images"][0].get("source")
                if image_info:
                    image_url = image_info.get("url", "")
                    if image_url:
                        logging.info(f"Descargando imagen: {title}")
                        download_image(image_url, args.output, title)
                    else:
                        logging.info(f"Omitido (imagen no válida): {title}")
                else:
                    logging.info(f"Omitido (no se encontró fuente de imagen): {title}")
            # Si no hay preview, revisamos si la URL termina en extensión de imagen
            elif url.lower().endswith(('.jpg', '.jpeg', '.png')):
                logging.info(f"Descargando imagen: {title}")
                download_image(url, args.output, title)
            else:
                logging.info(f"Omitido (tipo de contenido no soportado): {title}")

        # Pausa para respetar la API de Reddit
        time.sleep(2)

if __name__ == '__main__':
    main()
