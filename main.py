from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np
import cv2

app = FastAPI()

model = YOLO('best-2.pt')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image file
    image = Image.open(file.file)
    # image = cv2.imread('file.file', cv2.IMREAD_ANYCOLOR)
    # Save the image temporarily
    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)
    

    # Perform object detection on the image
    results = model(temp_image_path)

    # Convert the results to a NumPy array
    result_array = results[0].plot()

    # Convert BGR to RGB
    result_array = cv2.cvtColor(result_array, cv2.COLOR_BGR2RGB)

    # Convert the NumPy array to a PIL Image
    result_image = Image.fromarray(result_array)

    # Save the result image to a buffer
    buf = io.BytesIO()
    result_image.save(buf, format='JPEG')
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/jpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
