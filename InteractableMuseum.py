import cv2 as cv
import pyautogui as pyautogui

# Get screen resolution dynamically
screen_width, screen_height = pyautogui.size()
screen_resolution = (screen_width, screen_height)


def mouseCallback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Condition for opening the "text" window
        if 1 < x < 10 and 1 < y < 10:
            cv.destroyWindow("Interactive window")
            cap = cv.VideoCapture("text.mp4")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                resize_image_to_screen(frame, screen_resolution)
                cv.imshow("Text", frame)
                if cv.waitKey(24) & 0xFF == ord('q'):
                    break  # Exit the loop if 'q' is pressed
            cap.release()
            cv.destroyAllWindows()
            mainImage()

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
            mainImage()

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
            mainImage()


def resize_image_to_screen(img, screen_resolution):
    screen_width, screen_height = screen_resolution
    img_height, img_width = img.shape[:2]

    # Adjust screen height to leave space for the taskbar
    adjusted_screen_height = screen_height - 100  # Adjust this value as needed

    # Calculate scaling factor based on adjusted screen height
    scale = adjusted_screen_height / img_height

    # Resize the image
    resized_img = cv.resize(img, None, fx=scale, fy=scale)

    return resized_img


def draw_rectangles(img):
    # Define rectangle coordinates relative to image size

    # Text
    text_top_left = (int(img.shape[1] * 0.13), int(img.shape[0] * 0.13))
    text_bottom_right = (int(img.shape[1] * 0.35), int(img.shape[0] * 0.17))

    # Cut
    cut_top_left = (int(img.shape[1] * 0.92), int(img.shape[0] * 0.3))
    cut_bottom_right = (int(img.shape[1] * 0.97), int(img.shape[0] * 0.7))

    # Candle wax
    wax_top_left = (int(img.shape[1] * 0.63), int(img.shape[0] * 0.67))
    wax_bottom_right = (int(img.shape[1] * 0.9), int(img.shape[0] * 0.93))

    # Draw rectangles on the image
    cv.rectangle(img, text_top_left, text_bottom_right, (0, 255, 0), thickness=2)
    cv.rectangle(img, cut_top_left, cut_bottom_right, (0, 255, 0), thickness=2)
    cv.rectangle(img, wax_top_left, wax_bottom_right, (0, 255, 0), thickness=2)

    return img


def mainImage():
    img = cv.imread("the scream.jpg")

    print(screen_resolution)

    # Resize the image to fit screen resolution while maintaining aspect ratio
    resized_img = resize_image_to_screen(img, screen_resolution)

    image_with_rectangles = draw_rectangles(resized_img)

    # Display the image with rectangles
    cv.imshow("Interactive window", image_with_rectangles)

    # Set mouse callback function
    cv.setMouseCallback("Interactive window", mouseCallback)

    while True:
        key = cv.waitKey(1)
        if key == ord('q'):
            break


if __name__ == '__main__':
    mainImage()
