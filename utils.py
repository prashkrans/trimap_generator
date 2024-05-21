import os
import json

with open('config.json') as file:
    config = json.load(file)

input_dir = config['SINGLE_INPUT_DIR']
output_dir = config['OUTPUT_DIR']

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
def get_image_name_from_dir(dir):
    # List files in the directory
    files = os.listdir(dir)

    # Check if there is exactly one file in the directory
    if len(files) == 1:
        # Get the image name
        image_name = files[0]
        return image_name
    else:
        print("Error: The directory should contain exactly one image file.")
        print("Fix: Please make sure the direcotry has only one image")




