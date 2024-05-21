import cv2
import numpy as np

from math import ceil
from utils import input_dir, output_dir, get_image_name_from_dir


def paint_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Create a window to display the image
    cv2.namedWindow("Paint Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Paint Image", 1280, 1280)
    cv2.imshow("Paint Image", img)

     # Initialize variables for mouse event
    drawing = False
    height, width = img.shape[:2]
    max_val = max(height, width)
    print(f'max_val = {max_val}')
    if  max_val > 4000:
        brush_size = 200  # You can adjust the size of the brush
    elif max_val > 3000:
        brush_size = 120
    elif max_val > 2000:
        brush_size = 75
    elif max_val > 1000:
        brush_size = 30
    else:
        brush_size = 20

    color = (255, 255, 255)  # White color

    # Initialize a mask to track painted pixels
    mask = np.zeros_like(img, dtype=np.uint8)

    # Callback function to handle mouse events
    def draw_circle(event, x, y, flags, param):
        nonlocal drawing, color

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
            # Draw a circle with the current color at the mouse position
            cv2.circle(img, (x, y), brush_size, color, -1)
            cv2.circle(mask, (x, y), brush_size, (255, 255, 255), -1)
            cv2.imshow('Paint Image', img)

    # Set the callback function for mouse events
    cv2.setMouseCallback('Paint Image', draw_circle)

    while True:
        # Display the image and wait for a key press
        cv2.imshow('Paint Image', img)
        key = cv2.waitKey(1) & 0xFF

        # Change color to grey when the user presses 'c' key
        if key == ord('q') or key == ord('1'):
            color = (128, 128, 128)  # Grey color
            brush_size = ceil(0.5*brush_size)
        elif key == ord('w') or key == ord('2'):
            color = (255, 255, 255)  # White color
            brush_size = ceil(2*brush_size)
        elif key == ord('=') or key == 82:  # Increase brush size by pressing '=' or up arrow)
            brush_size += 2
        elif (key == ord('-') or key == 84) and brush_size > 4:  # Decrease brush size by pressing '-' or down arrow)
            brush_size -= 2
        if key == 27:  # Press 'Esc' to reset the mask
            mask = np.zeros_like(img, dtype=np.uint8)
            img = cv2.imread(image_path)
            cv2.imshow('Paint Image', img)
        # Break the loop if the user presses 'Enter' key and save the trimap so created
        elif key == 13:
            break

    # Set unpainted pixels to black
    unpainted_mask = cv2.bitwise_not(cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))
    img[unpainted_mask > 0] = (0, 0, 0)

    # Save the painted image 
    # cv2.imwrite(trimap_path, img)
    cv2.imwrite(trimap_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


    # Close the OpenCV window
    cv2.destroyAllWindows()

    print(f"Painted image saved as {trimap_path}")

if __name__=="__main__":
    # Replace 'your_image.jpg' with the path to your image file
    img_full_name = get_image_name_from_dir(input_dir)
    img_name = img_full_name.split('.')[0]
    img_path = f'{input_dir}/{img_full_name}'

    trimap_path = f'{output_dir}/trimap_{img_name}.png' # You can change the file name and format - .png preferred
    paint_image(img_path)

