import cv2
import requests
import git
from git import Repo
from io import BytesIO
from typing import Optional
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/convert_image")
async def convert_image(file: UploadFile = File(...), github_token: str = ""):
    # Descargar la imagen del archivo subido
    contents = await file.read()
    img = cv2.imdecode(np.fromstring(contents, np.uint8), cv2.IMREAD_COLOR)
    
    # Convertir la imagen a escala de grises
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Escribir la imagen en BytesIO
    buffer = BytesIO()
    cv2.imwrite(buffer, gray_img, [cv2.IMWRITE_JPEG_QUALITY, 90])
    buffer.seek(0)
    
    # Guardar la imagen procesada en GitHub
    try:
        repo = Repo.clone_from("https://github.com/bacterias-repo/images-bacterias.git", "/home/arturo/Documents/PROYECTOS/LAB_RAMOS/Codigos/APIS/vercel_prueba2")
        file_path = "images-bacterias/imagengris.jpg"
        with open(file_path, 'wb') as f:
            f.write(buffer.getvalue())
        repo.index.add([file_path])
        repo.index.commit("Add processed image")
        repo.remotes.origin.push()
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    return {"status": "success", "message": "Image processed and saved successfully."}
