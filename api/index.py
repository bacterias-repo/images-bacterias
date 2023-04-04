import cv2
import numpy as np
import urllib.request
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/convert_grayscale")
async def convert_grayscale(url: str):
    with urllib.request.urlopen(url) as url:
        img_array = np.asarray(bytearray(url.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
        buf = BytesIO()
        cv2.imwrite(buf, img, format='png')
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")
