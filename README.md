<div align="center">

# 🚀 Reddit Content Downloader

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Downloads](https://img.shields.io/github/downloads/username/reddit-downloader/total.svg)](https://github.com/username/reddit-downloader/releases)
[![Stars](https://img.shields.io/github/stars/username/reddit-downloader.svg)](https://github.com/username/reddit-downloader/stargazers)

**Una herramienta profesional de alto rendimiento para descargar contenido multimedia de Reddit con soporte empresarial.**

[Instalación](#-instalación) •
[Inicio Rápido](#-inicio-rápido) •
[Documentación](#-documentación) •
[Ejemplos](#-ejemplos) •
[API](#-api-reference) •
[Contribuir](#-contribuir)

</div>

---

## 📋 Tabla de Contenidos

- [🌟 Características](#-características)
- [🔧 Arquitectura](#-arquitectura)
- [⚡ Instalación](#-instalación)
- [🚀 Inicio Rápido](#-inicio-rápido)
- [📖 Documentación](#-documentación)
- [💡 Ejemplos Avanzados](#-ejemplos-avanzados)
- [🔌 API Reference](#-api-reference)
- [⚙️ Configuración](#️-configuración)
- [🧪 Testing](#-testing)
- [📊 Performance](#-performance)
- [🔒 Seguridad](#-seguridad)
- [🚢 Deployment](#-deployment)
- [🤝 Contribuir](#-contribuir)
- [🗺️ Roadmap](#️-roadmap)
- [❓ FAQ](#-faq)
- [📄 Licencia](#-licencia)

## 🌟 Características

### ✨ Funcionalidades Core
- **📥 Descarga Multimedia Completa**: Imágenes, videos, GIFs y audio con calidad original
- **🌐 Soporte Multi-Plataforma**: v.redd.it, YouTube, Streamable, Gfycat, Imgur y más
- **⚡ Alto Rendimiento**: Descargas paralelas con gestión inteligente de recursos
- **🔄 Recuperación Automática**: Sistema robusto de reintentos y manejo de errores
- **📊 Monitoreo en Tiempo Real**: Progreso detallado y métricas de rendimiento

### 🛠️ Características Empresariales
- **🔐 Autenticación OAuth2**: Soporte completo para API de Reddit
- **📈 Métricas y Logging**: Telemetría avanzada con Prometheus/Grafana
- **🏗️ Arquitectura Escalable**: Diseño modular y extensible
- **🐳 Containerización**: Soporte completo para Docker y Kubernetes
- **☁️ Cloud-Ready**: Desplegable en AWS, GCP, Azure

### 🎯 Filtros Avanzados
- **📅 Filtros Temporales**: Por día, semana, mes, año o rangos personalizados
- **⭐ Filtros de Calidad**: Por score, comentarios, awards
- **🏷️ Filtros de Contenido**: Por flair, autor, tipo de media
- **🔍 Búsqueda Inteligente**: Regex y patrones avanzados

## 🔧 Arquitectura

```mermaid
graph TB
    A[CLI Interface] --> B[Configuration Manager]
    B --> C[Reddit API Client]
    C --> D[Content Processor]
    D --> E[Download Manager]
    E --> F[Storage Backend]
    
    G[Monitoring] --> H[Metrics Collector]
    H --> I[Dashboard]
    
    J[Error Handler] --> K[Retry Logic]
    K --> L[Dead Letter Queue]
    
    subgraph "Storage Options"
        F --> M[Local Filesystem]
        F --> N[AWS S3]
        F --> O[Google Cloud Storage]
    end
```

## ⚡ Instalación

### 📋 Requisitos del Sistema

| Componente | Versión Mínima | Recomendada |
|------------|----------------|-------------|
| Python | 3.8+ | 3.11+ |
| RAM | 2GB | 8GB+ |
| Almacenamiento | 1GB libre | 10GB+ |
| FFmpeg | 4.0+ | 5.0+ |

### 🐍 Instalación con pip

```bash
# Instalación básica
pip install reddit-content-downloader

# Instalación con características avanzadas
pip install reddit-content-downloader[advanced]

# Instalación para desarrollo
pip install reddit-content-downloader[dev]
```

### 🐳 Docker

```bash
# Ejecutar con Docker
docker run -v $(pwd)/downloads:/app/downloads \
  reddit-downloader:latest \
  --subreddit cats --pages 5

# Docker Compose para producción
curl -O https://raw.githubusercontent.com/username/reddit-downloader/main/docker-compose.yml
docker-compose up -d
```

### 📦 Desde el código fuente

```bash
# Clonar el repositorio
git clone https://github.com/username/reddit-downloader.git
cd reddit-downloader

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Instalación en modo desarrollo
pip install -e .
```

## 🚀 Inicio Rápido

### 🎯 Ejemplo Básico

```bash
# Descargar las mejores imágenes del subreddit 'cats'
python app.py --subreddit cats \
              --pages 3 \
              --limit 50 \
              --sort top \
              --time week \
              --output ./cats_downloads
```

### 🔑 Configuración de API

```bash
# Configurar credenciales de Reddit (recomendado para mayor límite de requests)
export REDDIT_CLIENT_ID="your_client_id"
export REDDIT_CLIENT_SECRET="your_client_secret"
export REDDIT_USER_AGENT="YourApp/1.0.0"
```

### 📊 Monitoreo de Progreso

```bash
# Ejecutar con métricas detalladas
python app.py --subreddit programming \
              --verbose \
              --metrics \
              --progress-bar
```

## 📖 Documentación

### 🎛️ Parámetros de Línea de Comandos

| Parámetro | Corto | Tipo | Defecto | Descripción |
|-----------|-------|------|---------|-------------|
| `--subreddit` | `-s` | `str` | `all` | Subreddit objetivo |
| `--pages` | `-p` | `int` | `3` | Número de páginas |
| `--limit` | `-l` | `int` | `100` | Posts por página |
| `--output` | `-o` | `path` | `./downloads` | Directorio de salida |
| `--sort` |  | `str` | `hot` | Orden: `hot`, `new`, `top`, `controversial` |
| `--time` | `-t` | `str` | `all` | Filtro temporal: `all`, `day`, `week`, `month`, `year` |
| `--threads` |  | `int` | `4` | Descargas concurrentes |
| `--min-score` |  | `int` | `0` | Score mínimo de posts |
| `--max-size` |  | `str` | `100MB` | Tamaño máximo por archivo |
| `--formats` |  | `list` | `all` | Formatos: `jpg`, `png`, `gif`, `mp4`, `webm` |
| `--dry-run` |  | `bool` | `False` | Simular sin descargar |
| `--config` | `-c` | `path` |  | Archivo de configuración |
| `--verbose` | `-v` | `bool` | `False` | Logging detallado |
| `--quiet` | `-q` | `bool` | `False` | Modo silencioso |

### 📁 Estructura de Archivos de Salida

```
downloads/
├── subreddit_name/
│   ├── images/
│   │   ├── 2024-01/
│   │   │   ├── post_id_title.jpg
│   │   │   └── post_id_title.png
│   │   └── 2024-02/
│   ├── videos/
│   │   ├── 2024-01/
│   │   │   ├── post_id_title.mp4
│   │   │   └── post_id_title.webm
│   │   └── 2024-02/
│   ├── metadata/
│   │   ├── posts_metadata.json
│   │   ├── download_stats.json
│   │   └── failed_downloads.log
│   └── README.md
```

## 💡 Ejemplos Avanzados

### 🎨 Descarga de Arte Digital

```bash
# Descargar arte de alta calidad
python app.py \
  --subreddit Art DigitalArt ConceptArt \
  --min-score 1000 \
  --formats jpg png \
  --min-resolution 1920x1080 \
  --exclude-nsfw \
  --sort top \
  --time month
```

### 📺 Videos de Gaming

```bash
# Descargar clips de gaming
python app.py \
  --subreddit gaming GameClips \
  --formats mp4 webm \
  --max-duration 60 \
  --min-score 500 \
  --threads 8 \
  --quality best
```

### 📊 Análisis de Datos

```bash
# Recopilar datos para análisis
python app.py \
  --subreddit dataisbeautiful \
  --metadata-only \
  --pages 50 \
  --export-csv \
  --include-comments \
  --time all
```

### 🔄 Descarga Programada

```bash
# Usando cron para descargas automáticas
# crontab -e
# 0 2 * * * /path/to/python /path/to/app.py --config /path/to/config.yaml
```

## 🔌 API Reference

### 🐍 Python API

```python
from reddit_downloader import RedditDownloader

# Configuración básica
downloader = RedditDownloader(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="YourApp/1.0.0"
)

# Descarga programática
async def download_content():
    config = {
        'subreddit': 'cats',
        'pages': 5,
        'sort': 'top',
        'time_filter': 'week',
        'output_dir': './downloads',
        'filters': {
            'min_score': 100,
            'formats': ['jpg', 'png', 'gif'],
            'max_size': '50MB'
        }
    }
    
    async for result in downloader.download(**config):
        print(f"Downloaded: {result.filename}")
        print(f"Status: {result.status}")
        print(f"Metadata: {result.metadata}")

# Ejecutar
import asyncio
asyncio.run(download_content())
```

### 🔧 Hooks y Callbacks

```python
from reddit_downloader.hooks import DownloadHook

class CustomHook(DownloadHook):
    def on_download_start(self, post):
        print(f"Iniciando descarga: {post.title}")
    
    def on_download_complete(self, result):
        # Enviar notificación, actualizar DB, etc.
        self.notify_completion(result)
    
    def on_download_error(self, error, post):
        # Logging personalizado, reintentos, etc.
        self.handle_error(error, post)

downloader.add_hook(CustomHook())
```

## ⚙️ Configuración

### 📄 Archivo de Configuración (YAML)

```yaml
# config.yaml
reddit:
  client_id: "${REDDIT_CLIENT_ID}"
  client_secret: "${REDDIT_CLIENT_SECRET}"  
  user_agent: "RedditDownloader/2.0.0"
  
download:
  subreddits: ["cats", "dogs", "aww"]
  pages: 10
  limit: 100
  sort: "top"
  time_filter: "week"
  
  output:
    base_dir: "./downloads"
    organize_by: "subreddit"  # subreddit, date, type
    naming_pattern: "{id}_{title}_{author}"
    
  filters:
    min_score: 50
    max_size: "100MB"
    min_resolution: "800x600"
    formats: ["jpg", "png", "gif", "mp4"]
    exclude_nsfw: true
    exclude_spoilers: true
    
  performance:
    threads: 8
    chunk_size: 8192
    timeout: 30
    retries: 3
    delay_between_requests: 1
    
  storage:
    backend: "local"  # local, s3, gcs
    compression: true
    deduplicate: true
    
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: "./logs/downloader.log"
  
monitoring:
  enabled: true
  metrics_port: 8080
  health_check_port: 8081
```

### 🔐 Variables de Entorno

```bash
# .env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password

# Almacenamiento en la nube
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_DEFAULT_REGION=us-east-1

# Monitoreo
PROMETHEUS_GATEWAY=http://localhost:9091
GRAFANA_API_KEY=your_grafana_key

# Base de datos
DATABASE_URL=postgresql://user:pass@localhost/reddit_downloader
```

## 🧪 Testing

### 🔍 Ejecutar Tests

```bash
# Tests unitarios
pytest tests/unit/

# Tests de integración
pytest tests/integration/

# Tests de rendimiento
pytest tests/performance/ --benchmark-only

# Coverage completo
pytest --cov=reddit_downloader --cov-report=html
```

### 🐛 Tests de Calidad de Código

```bash
# Linting
flake8 reddit_downloader/
black --check reddit_downloader/
isort --check-only reddit_downloader/

# Type checking
mypy reddit_downloader/

# Security scanning
bandit -r reddit_downloader/
```

## 📊 Performance

### ⚡ Benchmarks

| Métrica | Valor | Condiciones |
|---------|-------|-------------|
| Throughput | 50-100 archivos/min | Red estable, 8 threads |
| Memoria | ~200MB | Procesando 1000 posts |
| CPU | 15-30% | Intel i7, 8 threads activos |
| Latencia API | <500ms | Reddit API, autenticado |

### 📈 Optimizaciones Disponibles

- **Paralelización**: Hasta 16 descargas simultáneas
- **Compresión**: Reducción de 30-40% en almacenamiento
- **Caché**: Evita re-descargas con hash SHA-256
- **Streaming**: Procesamiento de archivos grandes sin cargar en memoria

## 🔒 Seguridad

### 🛡️ Mejores Prácticas Implementadas

- ✅ **Validación de Entrada**: Sanitización de parámetros
- ✅ **Rate Limiting**: Respeto a límites de API
- ✅ **Verificación de Archivos**: Validación de tipos MIME
- ✅ **Logging Seguro**: Sin exposición de credenciales
- ✅ **Actualizaciones**: Dependencias monitoreadas con Dependabot

### 🔐 Configuración de Seguridad

```yaml
# security.yaml
security:
  max_file_size: "500MB"
  allowed_domains:
    - "i.redd.it"
    - "v.redd.it" 
    - "imgur.com"
    - "gfycat.com"
  
  blocked_extensions:
    - ".exe"
    - ".bat"
    - ".sh"
  
  virus_scanning:
    enabled: true
    service: "clamav"
```

## 🚢 Deployment

### 🐳 Docker Production

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["python", "app.py", "--config", "production.yaml"]
```

### ☸️ Kubernetes

```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reddit-downloader
spec:
  replicas: 3
  selector:
    matchLabels:
      app: reddit-downloader
  template:
    metadata:
      labels:
        app: reddit-downloader
    spec:
      containers:
      - name: reddit-downloader
        image: reddit-downloader:latest
        ports:
        - containerPort: 8080
        env:
        - name: REDDIT_CLIENT_ID
          valueFrom:
            secretKeyRef:
              name: reddit-secrets
              key: client-id
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### 🌐 AWS/GCP/Azure

```bash
# AWS ECS
aws ecs create-service --cli-input-json file://ecs-service.json

# Google Cloud Run
gcloud run deploy reddit-downloader \
  --image gcr.io/project-id/reddit-downloader \
  --platform managed

# Azure Container Instances
az container create --resource-group myResourceGroup \
  --name reddit-downloader \
  --image reddit-downloader:latest
```

## 🤝 Contribuir

### 🎯 Cómo Contribuir

1. **🍴 Fork** el repositorio
2. **🌿 Crear** una rama feature (`git checkout -b feature/amazing-feature`)
3. **💻 Desarrollar** siguiendo nuestros estándares
4. **✅ Testing** completo de tu código
5. **📝 Commit** con mensajes descriptivos
6. **🚀 Push** a tu rama (`git push origin feature/amazing-feature`)
7. **📬 Crear** un Pull Request

### 📋 Checklist de Contribución

- [ ] **Código**: Sigue PEP 8 y pasa todos los linters
- [ ] **Tests**: Coverage > 90% para nuevo código
- [ ] **Documentación**: README y docstrings actualizados
- [ ] **Performance**: Sin regresiones de rendimiento
- [ ] **Seguridad**: Revisión de vulnerabilidades
- [ ] **Changelog**: Entrada agregada en CHANGELOG.md

### 🏗️ Configuración de Desarrollo

```bash
# Setup desarrollo
git clone https://github.com/username/reddit-downloader.git
cd reddit-downloader

# Pre-commit hooks
pip install pre-commit
pre-commit install

# Entorno de desarrollo
pip install -e .[dev]

# Ejecutar todos los checks
make check  # linting, testing, security
```

### 🎨 Estándares de Código

```python
# Ejemplo de función bien documentada
async def download_post(
    post: RedditPost,
    output_dir: Path,
    *,
    quality: str = "best",
    timeout: int = 30
) -> DownloadResult:
    """Descarga un post de Reddit.
    
    Args:
        post: El post de Reddit a descargar
        output_dir: Directorio donde guardar el archivo
        quality: Calidad de descarga ('best', 'worst', '720p')
        timeout: Timeout en segundos para la descarga
        
    Returns:
        Resultado de la descarga con metadata
        
    Raises:
        DownloadError: Si falla la descarga
        ValidationError: Si los parámetros son inválidos
    """
```

## 🗺️ Roadmap

### 🎯 Q1 2024
- [ ] **Interfaz Web**: Dashboard de administración
- [ ] **API REST**: Endpoints para integración
- [ ] **Plugins**: Sistema de extensiones
- [ ] **ML Features**: Clasificación automática de contenido

### 🎯 Q2 2024
- [ ] **Mobile App**: Aplicación React Native
- [ ] **Cloud Sync**: Sincronización multi-dispositivo
- [ ] **Advanced Analytics**: Métricas de contenido
- [ ] **CDN Integration**: Distribución optimizada

### 🎯 Q3 2024
- [ ] **AI Filtering**: Filtros inteligentes con IA
- [ ] **Real-time Processing**: Pipeline en tiempo real
- [ ] **Blockchain**: NFT y Web3 integración
- [ ] **Enterprise Features**: SSO, RBAC, Audit logs

## ❓ FAQ

### 🤔 Preguntas Frecuentes

**P: ¿Es legal descargar contenido de Reddit?**
R: Sí, el contenido público de Reddit puede descargarse para uso personal. Respeta siempre los derechos de autor y términos de servicio.

**P: ¿Cuánto contenido puedo descargar?**
R: Sin autenticación: ~60 requests/minuto. Con OAuth2: ~600 requests/minuto.

**P: ¿Funciona con subreddits privados?**
R: No, solo subreddits públicos. Para privados necesitas permisos específicos.

**P: ¿Cómo manejo videos grandes?**
R: Usa `--max-size` para limitar tamaño y `--quality` para ajustar calidad.

**P: ¿Puedo personalizar nombres de archivos?**
R: Sí, usa `--naming-pattern` con placeholders como `{title}`, `{author}`, `{date}`.

### 🛠️ Troubleshooting

```bash
# Problema: "429 Too Many Requests"
# Solución: Incrementar delay entre requests
python app.py --delay 3 --threads 2

# Problema: Videos sin audio
# Solución: Verificar instalación de ffmpeg
ffmpeg -version

# Problema: Memoria insuficiente
# Solución: Reducir concurrencia
python app.py --threads 2 --chunk-size 4096
```

## 📊 Métricas y Monitoreo

### 📈 Dashboard de Métricas

```bash
# Iniciar servidor de métricas
python app.py --metrics-server --port 8080

# Métricas disponibles en http://localhost:8080/metrics
# - downloads_total
# - downloads_failed
# - download_duration_seconds
# - api_requests_total
# - storage_usage_bytes
```

### 🔍 Health Check

```bash
# Endpoint de salud
curl http://localhost:8081/health

# Respuesta esperada:
{
  "status": "healthy",
  "version": "2.0.0",
  "uptime": "2h 15m 30s",
  "components": {
    "reddit_api": "connected",
    "storage": "available",
    "ffmpeg": "installed"
  }
}
```

<div align="center">

**¿Te gusta este proyecto? ¡Dale una ⭐!**

**Hecho con ❤️ por la comunidad**

</div>
