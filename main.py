import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Starting the webcam

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        print("Error: Failed to grab frame")
        break



    # Convert Image to Image HSV
    # Loading the image in HSV color separates the Hue from the Brightness, so it is easier to detect the colors under various levels of lighting.
    # Disadvantages: RBG is the native format for most displays, is more efficient and simpler to use and understand.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Bright Red
    lower1 = np.array([0, 120, 70])
    upper1 = np.array([10, 255, 255])

    # Deep Red
    lower2 = np.array([170, 120, 70])
    upper2 = np.array([180, 255, 255])

    # Defining the two masks for detecting color
    mask1 = cv2.inRange(hsv, lower1, upper1) # Mask for Bright Red objects
    mask2 = cv2.inRange(hsv, lower2, upper2) # Mask for Deep Red objects

    # Overlaying both masks using the bitwise or function
    mask = cv2.bitwise_or(mask1, mask2)


    # Detecting skin tones alone and removing the objects from the
    # YCrCb color space separates brightness from color, making skin-tone detection more robust under different lighting conditions.
    skin_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    lower_skin = np.array([0, 133, 77]) # Skin tones Lower Bound
    upper_skin = np.array([255, 173, 127]) # Skin tones Upper Bound

    skin_mask = cv2.inRange(skin_img, lower_skin, upper_skin) # Mask containing only skin

    mask = cv2.bitwise_and(mask, cv2.bitwise_not(skin_mask)) # Removing the skin colored objects from the mask using a bitwise not function
    # I added this part to the program because it kept detecting my skin as red for the first few seconds of running the code

    contours, _ = cv2.findContours( # Scans the mask and looks for connected regions
        mask,
        cv2.RETR_EXTERNAL, # Tells OpenCV to retrieve only the outermost contours
        cv2.CHAIN_APPROX_SIMPLE # Stores only key contour points
    )


    output_image = img.copy()  # Create a copy of the original image
    # 'contours' is a list of all red objects found

    # DRAWING BOUNDING CIRCLES ON IMAGE
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        center_x = x + w // 2  # X-coordinate of circle's center
        center_y = y + h // 2  # Y-coordinate of circle's center
        radius = max(w, h) // 2  # Circle's radius is half of the maximum of width or height
        output_image = cv2.circle(output_image, (center_x, center_y), radius, (0, 0, 0),
                                  2)  # drawing outline circle using cv2 package

    # Display image with bounding circles
    cv2.imshow("Detected Objects", output_image)


    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
