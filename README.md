# 🎧 FFmpeg Video-to-Audio API

API ligera basada en **FastAPI + FFmpeg** para convertir cualquier video (MP4, MOV, MKV, etc.) en un archivo de audio MP3.  
Ideal para integraciones con sistemas de transcripción como **Whisper**, **n8n**, o cualquier pipeline multimedia.

---

## 🚀 Características

- Convierte videos a audio (`.mp3`) usando FFmpeg.
- Soporta formatos comunes: `.mp4`, `.mov`, `.mkv`, `.avi`, etc.
- Detecta automáticamente si el video contiene audio.
- Devuelve el audio resultante directamente en la respuesta HTTP.
- Monta una carpeta persistente (`uploads/`) para almacenar archivos.

---

## 🧱 Estructura del proyecto

```
ffmpeg-api/
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── uploads/
```

---

## ⚙️ Requisitos previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- Puerto **8080** libre en tu máquina

---

## 🐳 Ejecución rápida

1. Clona el repositorio o copia los archivos:

   ```bash
   git clone https://github.com/tuusuario/ffmpeg-api.git
   cd ffmpeg-api
   ```

2. Inicia el servicio:

   ```bash
   docker compose up --build
   ```

3. Abre tu navegador en:  
   👉 **http://localhost:8080/docs**

   Aquí encontrarás la interfaz interactiva de Swagger.

---

## 📡 Endpoint principal

### `POST /convert`

Convierte un archivo de video a MP3 y devuelve el audio resultante.

#### **Request (multipart/form-data)**
| Field | Type | Description |
|--------|------|-------------|
| `file` | File | Video a convertir (`.mp4`, `.mov`, etc.) |

#### **Ejemplo con `curl`:**
```bash
curl.exe -X POST -F "file=@mi_video.mp4" http://localhost:8080/convert --output audio.mp3
```

#### **Ejemplo con Postman:**
1. Método: `POST`
2. URL: `http://localhost:8080/convert`
3. Body → `form-data`
   - Key: `file`
   - Type: `File`
   - Value: selecciona tu video

#### **Respuesta**
- Devuelve directamente el archivo `.mp3` convertido.
- Si el video no tiene audio, devuelve:
  ```json
  {
    "detail": "Video does not contain audio stream"
  }
  ```

---

## 🧠 Integración con n8n o Whisper

Este contenedor puede servir como etapa previa en pipelines multimedia.

**Ejemplo flujo n8n:**
1. **HTTP Request Node** → envía el video a `http://ffmpeg-api:8080/convert`
2. **HTTP Request Node 2** → envía el audio resultante a Whisper
3. **Write File Node** → guarda la transcripción o el audio en tu servidor

---

## 🗂️ Carpetas persistentes

- **uploads/**  
  Carpeta compartida con el contenedor (`/app/uploads`) donde se guardan:
  - Archivos de video subidos
  - Archivos MP3 convertidos

---

## 🧰 Solución de problemas

| Problema | Causa | Solución |
|-----------|--------|-----------|
| Archivo MP3 vacío o de 1 KB | El video no tiene pista de audio | Verifica con `ffmpeg -i video.mp4` |
| No aparece el archivo en `uploads/` | Usabas `/tmp` (no montado) | Cambia a `/app/uploads` |
| Error SSL al construir imagen | Problema de CA en red corporativa | Instala `ca-certificates` o usa `--trusted-host` |
| Puerto ocupado | Otro proceso usa 8080 | Cambia `ports` a `9090:8080` |

---

## 🧾 Licencia

Este proyecto se distribuye bajo licencia **MIT**.  
Eres libre de usarlo, modificarlo y redistribuirlo.

---

## 💬 Créditos

Desarrollado con ❤️ usando:
- [FastAPI](https://fastapi.tiangolo.com/)
- [FFmpeg](https://ffmpeg.org/)
- [Docker](https://www.docker.com/)
