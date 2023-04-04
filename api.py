import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse

app = FastAPI()

@app.post("/grayscale")
async def grayscale(file: UploadFile):
    contents = await file.read()
    np_image = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    buffer = cv2.imencode('.jpg', gray_image)[1].tobytes()
    return StreamingResponse(BytesIO(buffer), media_type="image/jpeg")
