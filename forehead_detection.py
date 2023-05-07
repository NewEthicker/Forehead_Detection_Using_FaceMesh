# simple forehead shower
import cv2
import mediapipe as mp

# Set up the FaceMesh model
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Set up the video capture device
url = "https://10.130.20.75:8080/video"
cap = cv2.VideoCapture(url)

# Set the center point for the scope
center_x, center_y = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2)

# Initialize variables to keep track of previous x and y positions
prev_x = None
prev_y = None

while True:
    # Read a frame from the capture device
    ret, frame = cap.read()

    # Convert the frame to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the face landmarks using FaceMesh
    results = face_mesh.process(frame)

    # Convert the frame back to BGR format for display
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Check if any landmarks were detected
    if results.multi_face_landmarks:
        # Loop through each detected face
        for face_landmarks in results.multi_face_landmarks:
            # Get the coordinates of the forehead landmark (landmark #151)
            forehead_landmark = face_landmarks.landmark[151]
            x = int(forehead_landmark.x * frame.shape[1])
            y = int(forehead_landmark.y * frame.shape[0])

            # Draw x and y lines
            cv2.line(frame, (x, 0), (x, frame.shape[0]), (255, 255, 255), 1)
            cv2.line(frame, (0, y), (frame.shape[1], y), (255, 255, 255), 1)

            # Calculate the distance between the center point and the forehead landmark
            distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5

            # If the distance is within the scope radius, turn on the LED
            # if distance <= 30:
            #     # Turn on the LED
            #     print("LED ON")

            # Draw a red circle at the center of the x and y lines
            cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)
            cv2.circle(frame, (x, y), 2, (255, 255, 255), -1)
            # Check if the x or y line has moved and print its coordinates
            if prev_x is not None and prev_y is not None:
                if x != prev_x or y != prev_y:
                    print(f"X: {x}, Y: {y}")

            # Update the previous x and y positions
            prev_x = x
            prev_y = y

    # Display the frame
    cv2.imshow('FaceMesh Forehead Detection', frame)

    # Wait for a key press and check if the 'q' key was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture device and close all windows
cap.release()
cv2.destroyAllWindows()