```markdown
# Reddit Downloader

Una herramienta en Python para descargar imágenes y videos (con audio) de un subreddit.

## Características

- Descarga imágenes y videos de un subreddit.
- Soporta videos de varias plataformas (v.redd.it, YouTube, youtu.be, streamable, gfycat).
- Utiliza [yt-dlp](https://github.com/yt-dlp/yt-dlp) para la descarga de videos.
- Respeta las limitaciones de la API de Reddit con pausas entre páginas.
- Permite filtrar posts por orden y por intervalo de tiempo.

## Requisitos

- **Python 3.6+**
- **ffmpeg**  
  Es necesario para fusionar audio y video en los videos descargados.  
  Puedes instalarlo mediante tu gestor de paquetes o descargarlo desde [ffmpeg.org](https://ffmpeg.org/).

- **Librerías de Python:**  
  Puedes instalar las dependencias necesarias utilizando el siguiente archivo `requirements.txt`:

  ```text
  requests
  yt-dlp
  ```

  Luego, instala las dependencias ejecutando:

  ```bash
  pip install -r requirements.txt
  ```

## Uso

Ejecuta el script desde la línea de comandos con los siguientes argumentos:

```bash
python app.py -s <subreddit> -p <pages> -l <limit> -o <output_directory> --sort <order> -t <time_filter>
```

### Ejemplo

Para descargar contenido del subreddit `cats`, recorriendo 10 páginas con 100 posts por página, usando el orden `top` con filtro de tiempo `all`, ejecuta:

```bash
python app.py -s cats -p 10 -l 100 -o mi_directorio --sort top -t all
```

## Parámetros

- `-s`, `--subreddit`: Nombre del subreddit desde el cual se descargará el contenido (por defecto: `all`).
- `-p`, `--pages`: Número de páginas a recorrer (por defecto: `3`).
- `-l`, `--limit`: Número de posts por página (por defecto: `100`).
- `-o`, `--output`: Directorio donde se guardará el contenido descargado (por defecto: `downloaded_content`).
- `--sort`: Orden de los posts. Opciones disponibles: `hot`, `new`, `top`, `controversial` (por defecto: `hot`).
- `-t`, `--time`: Intervalo de tiempo para posts en orden `top`. Opciones: `all`, `day`, `week`, `month`, `year` (por defecto: `all`).

## Consideraciones

- Asegúrate de tener instalado `ffmpeg` para poder descargar videos con audio.
- El script respeta las políticas de la API de Reddit haciendo una pausa de 2 segundos entre cada página.
- En caso de errores durante la descarga, se mostrarán mensajes de log para facilitar la depuración.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un "issue" o envía un "pull request".

## Licencia

Este proyecto está bajo la Licencia MIT.
``` 

Guarda este contenido en un archivo llamado `README.md` en tu repositorio de GitHub.
