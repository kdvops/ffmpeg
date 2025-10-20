curl -X POST -F "file=@mi_video.mp4" http://localhost:8080/convert --output audio.mp3


Invoke-WebRequest -Uri "http://localhost:8080/convert" `
  -Method Post `
  -Form @{ file = Get-Item "C:\repositorio\ffmpeg\mi_video.mp4" } `
  -OutFile "C:\repositorio\ffmpeg\audio.mp3"
