# Warehouse-Shelf-Space-and-Barcode-Detection-using-YOLO

This project is a web application designed to detect barcodes and empty spaces on warehouse shelves using a YOLO object detection model. The frontend allows users to upload images of warehouse shelves, while the FastAPI backend processes the image and returns object detection results.

## Features

- **Frontend:** A simple, user-friendly interface to upload images for analysis.
  
- **Backend:** FastAPI server running a YOLO model for detecting barcodes and empty spaces on warehouse shelves.
  
- **Real-Time Analysis:** Upon image submission, the backend analyzes the image and returns detection results.

## Technologies Used

- **Frontend:** HTML, CSS (Bootstrap 4), JavaScript.
  
- **Backend:** FastAPI, YOLO (for object detection), Python.

## Setup
**1. Clone the repository:** 

     git clone https://github.com/your-username/warehouse-barcode-detector.git
     
     cd warehouse-barcode-detector

**2. Install backend dependencies:**

    pip install fastapi uvicorn pillow ultralytics torch loguru nest_asyncio

**3. Download and set up the YOLO model:**

Place your trained YOLO model weights (best-2.pt) in the root directory of the project. This model will be used to detect barcodes and empty spaces.

**4. Running the Application:**
  1.  Run the FastAPI server:

    python main.py
    
  2.  Run the Frontend:

Simply open the index.html file in your browser to access the frontend. You can upload images and interact with the app.

**5. API Endpoints**
  1. Prediction Endpoint

    POST /predict/

This endpoint accepts an image file and processes it with the YOLO model to detect barcodes and empty spaces.

- Request:
    - file: The image file to be analyzed.
- Response:
    - Returns a JSON object with the detection results (empty spaces and barcodes).
      
Example usage with curl:

    curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@image2.jpg"

## Frontend Interface
The frontend uses Bootstrap for styling and provides a simple interface to upload images. It allows users to:

  1. Select an image file.
     
  2. Submit the file for analysis.
     
  3. View the results after the backend processes the image.

The UI features a clean, responsive design with a call-to-action to upload warehouse images for barcode and empty-space detection.

## Example Workflow
  1. The user uploads an image via the frontend form.
     
  2. The image is sent to the FastAPI backend for object detection.
     
  3. The backend returns the detection results.
     
  4. The user receives the results in real-time on the frontend.

## Project Structure

    .
    ├── app.py               # FastAPI backend application
    ├── index.html           # Frontend HTML file
    ├── static               # Folder for static files (images, stylesheets, etc.)
    ├── main.py              # Main backend code, including object detection
    ├── best-2.pt              # YOLO model weights for barcode and empty-space detection
    ├── README.md            # This README file

## Future Enhancements
  - **Results Display:** Display object detection results (like bounding boxes) directly on the frontend.

  - **Image Preprocessing:** Add image preprocessing steps like resizing or cropping.

  - **Deployment:** Deploy the FastAPI backend and frontend on a cloud service for broader access.

## Output Images
![image](https://github.com/user-attachments/assets/7584555d-257e-45f4-898e-d1b799191c5a)
![image](https://github.com/user-attachments/assets/637c8465-6cae-4bc2-84c0-c411d95a18b4)
