# Face Detection with OpenCV

## Overview
This project implements a simple face detection application using OpenCV. The application captures video from the webcam, detects faces in real-time, and displays the video feed with rectangles drawn around detected faces.

## Requirements
- Python 3.x
- OpenCV library

## Installation
1. **Install Python**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install OpenCV**: You can install OpenCV using pip. Open a terminal or command prompt and run:
   ```bash
   pip install opencv-python
   ```

## Usage
1. **Run the Script**: Save the code to a file named `face_detection.py` and run it using:
   ```bash
   python face_detection.py
   ```

2. **Control the Application**:
   - Press the **"a"** key to exit the application.
   - You can also close the window using the close button (the "X" button) on the window.

## Code Explanation
- **Face Detection Model**: The code uses a pre-trained Haar Cascade classifier for detecting faces. The classifier file is loaded from OpenCV's data directory.
- **Video Capture**: The application captures video from the default webcam (index 0).
- **Frame Processing**:
  - Each frame is converted to grayscale for better face detection performance.
  - Detected faces are highlighted with green rectangles.
- **Display**: The processed video feed is displayed in a window titled "Video_live".

## Troubleshooting
- If the application does not open the webcam, make sure no other application is using the camera.
- Ensure that your environment has access to the webcam.
- If you encounter any errors related to OpenCV, ensure that the library is installed correctly.
