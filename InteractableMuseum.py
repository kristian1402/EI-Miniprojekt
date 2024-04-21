import cv2 as cv


def mouseCallback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Condition for opening the "text" window
        if 148 < x < 293 and 140 < y < 155:
            cv.destroyWindow("Interactive window")
            cap = cv.VideoCapture("text.mp4")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv.resize(frame, (1366,768))
                cv.imshow("Text", frame)
                if cv.waitKey(24) & 0xFF == ord('q'):
                    break  # Exit the loop if 'q' is pressed
            cap.release()
            cv.destroyAllWindows()
            cv.imshow("Interactive window", img)
            cv.setMouseCallback("Interactive window", mouseCallback)
        # Condition for opening the "cut" window
        if 740 < x < 770 and 200 < y < 600:
            cv.destroyWindow("Interactive window")
            cap = cv.VideoCapture("cut.mp4")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv.resize(frame, (1366,768))
                cv.imshow("Cut", frame)
                if cv.waitKey(24) & 0xFF == ord('q'):
                    break  # Exit the loop if 'q' is pressed
            cap.release()
            cv.destroyAllWindows()
            cv.imshow("Interactive window", img)
            cv.setMouseCallback("Interactive window", mouseCallback)
        # Condition for opening the "candle wax" window
        if 520 < x < 700 and 700 < y < 900:
            cv.destroyWindow("Interactive window")
            cap = cv.VideoCapture("candle wax.mp4")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv.resize(frame, (1366,768))
                cv.imshow("Candle Wax", frame)
                if cv.waitKey(24) & 0xFF == ord('q'):
                    break  # Exit the loop if 'q' is pressed
            cap.release()
            cv.destroyAllWindows()
            cv.imshow("Interactive window", img)
            cv.setMouseCallback("Interactive window", mouseCallback)


# Load the image
img = cv.imread("the scream.jpg")

# Resize the image to fit screen resolution
img = cv.resize(img, (805, 1000))

#text indicator box
cv.rectangle(img, (148,140), (293,155), (0, 255, 0), 2)

#cut indicator box
cv.rectangle(img, (740,200), (770,600), (0, 255, 0), 2)

#candle wax indicator box
cv.rectangle(img, (520,700), (700,900), (0, 255, 0), 2)

# Display the image
cv.imshow("Interactive window", img)

# Set mouse callback function
cv.setMouseCallback("Interactive window", mouseCallback)

while True:
    key = cv.waitKey(1)
    if key == ord('q'):
        break
