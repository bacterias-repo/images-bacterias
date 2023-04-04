import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
from fastapi import FastAPI
from fastapi import UploadFile

app = FastAPI()

@app.post("/grayscale")
async def grayscale(image: UploadFile):
    # Leer la imagen del archivo subido
    img = Image.open(BytesIO(await image.read()))
    
    # Convertir la imagen a escala de grises
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    
    # Guardar la imagen en un archivo temporal
    temp_file = BytesIO()
    Image.fromarray(img).save(temp_file, format='PNG')
    temp_file.seek(0)
    
    return temp_file

