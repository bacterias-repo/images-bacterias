import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/convert_image")
async def convert_image(file: UploadFile = File(...)):
    file_contents = await file.read()
    nparr = np.fromstring(file_contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return {"image": img.tolist()}
