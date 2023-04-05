import io
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, Header
from github import Github

app = FastAPI()

g = Github("<tu-token>")

@app.post("/convert_image")
async def convert_image(file: UploadFile = File(...), api_key: str = Header(None)):
    if api_key != "<tu-api-key>":
        return {"error": "API Key inválida"}
    
    # Obtener el contenido de la imagen en bytes
    file_contents = await file.read()
    
    # Convertir los bytes en un array de numpy
    nparr = np.fromstring(file_contents, np.uint8)
    
    # Leer la imagen usando OpenCV y convertirla a escala de grises
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    
    # Guardar la imagen en GitHub
    repo = g.get_repo("<tu-repositorio>")
    contents = file.file.read()
    repo.create_file("grayscale_image.jpg", "commit message", contents)
    
    # Devolver la imagen en escala de grises
    return {"image": img.tolist()}

