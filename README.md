# Forehead Detection Using FaceMesh


https://user-images.githubusercontent.com/88562515/236703955-ca0144b7-1aa7-4d93-8a87-bf9d5cf7a11a.mp4


This script uses the FaceMesh model from the Mediapipe library to detect the forehead landmark of a face in a video stream. The script then calculates the distance between the forehead landmark and a predefined center point, and displays the x and y positions of the landmark if it moves.

The script requires OpenCV and Mediapipe to be installed. The video capture device can be specified using a URL, and the center point for the scope can be set by adjusting the center_x and center_y variables.

To use the script, simply run it in a Python environment with OpenCV and Mediapipe installed. The script will display the video stream with the x and y lines and a red circle at the position of the forehead landmark. If the landmark moves, the script will print its x and y positions in the console.
