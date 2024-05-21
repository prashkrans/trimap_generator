from PIL import Image
import os

def convert_to_png(image_path, png_dir, file_name):
    """
    Convert an image file to PNG format.
    
    Args:
    image_path (str): The path to the image file.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Convert to RGB mode (if not already in RGB)
            #img = img.convert("RGB")
            # Construct the new file name with the .png extension
            new_file_name = file_name.split(".")[0] + ".png"
            new_img_path = png_dir + '/' + new_file_name
            # Save the image as PNG format
            img.save(new_img_path, "PNG", compress_level=5)
            #img.save(new_img_path, format="PNG", optimize=True, palette=Image.ADAPTIVE)
            print(f"Image converted successfully: {new_file_name}")
    except Exception as e:
        print(f"Error converting image: {e}")

def batch_convert_to_png(folder_path, png_dir):
    """
    Batch convert all .jpg and .JPG files in a folder to PNG format.
    
    Args:
    folder_path (str): The path to the folder containing image files.
    """
    try:
        # Iterate through all files in the folder
        for file_name in os.listdir(folder_path):
            # Check if the file is a .jpg or .JPG file
            if file_name.lower().endswith(('.jpg', '.jpeg')):
                # Construct the full path to the image file
                image_path = f'{folder_path}/{file_name}'
                # Convert the image to PNG format
                convert_to_png(image_path, png_dir, file_name)
    except Exception as e:
        print(f"Error converting images: {e}")


if __name__=="__main__":
    # Example usage
    folder_path = "./input_reserves"
    png_dir = "./resources/png_dir"
    batch_convert_to_png(folder_path, png_dir)
