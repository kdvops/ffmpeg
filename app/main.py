from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import subprocess, os

app = FastAPI(title="FFmpeg Video to Audio API")

UPLOAD_DIR = "/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/convert")
async def convert_to_audio(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.splitext(input_path)[0] + ".mp3"

    # Guardar video recibido
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Detectar pista de audio
    probe = subprocess.run(
        ["ffprobe", "-i", input_path, "-show_streams", "-select_streams", "a", "-loglevel", "error"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if not probe.stdout:
        raise HTTPException(status_code=400, detail="Video does not contain audio")

    # Extraer audio
    cmd = ["ffmpeg", "-y", "-i", input_path, "-vn", "-acodec", "libmp3lame", "-ar", "44100", "-ab", "128k", output_path]
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if not os.path.exists(output_path):
        raise HTTPException(status_code=500, detail="Audio extraction failed")

    # Devuelve el archivo generado
    return FileResponse(output_path, media_type="audio/mpeg", filename=os.path.basename(output_path))
