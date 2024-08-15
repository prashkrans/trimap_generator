# Trimap Generator
- Allows the user to paint a trimap on the input image.
- A **trimap** is a grayscale image used in image segmentation or matting, where pixels are categorized into three regions: white (foreground), black (background), and grey (unknown). The white and black areas are clearly identified, while the grey regions are where the algorithm determines whether the pixel belongs to the foreground or background. This helps in accurately separating objects from their backgrounds.
- The source image, along with the trimap, can then be fed into image matting models such as **ViTMatte**.
- **Image matting** is a technique used to accurately separate the foreground (like a person or object) from the background in an image.
- This is particularly useful in tasks like creating transparent backgrounds, adding effects, or changing the background in photos and videos.
- **ViTMatte** can achieve precise and high-quality matting results, even in challenging scenarios like hair or semi-transparent objects.

#### TODO: Implement ViTMatte

### Demo Video:
https://github.com/user-attachments/assets/7b650333-a104-494a-be9d-1468eb583d1f

### Setup:
- Clone the repo and move to the root dir.
- Create a python virtual environment.
- Install the requirements.

### Usage:
- Before running `main.py` put a single image in `./resources/single_input_dir/`
- Run `main.py` as `python3 main.py`
- The source image preview would pop up, use mouse pointer and the below keybinds to create a trimap and then press enter to save it or escape to revert all the changes.
- Keybinds:
  1. 1 or Q: Grey Mask (Unknown Region)
  2. 2 or E: White Mask (Foreground) 
  3. Up arrow or +/=: Increases the brush size
  4. Down arrow or _/-: Decreases the brush size
  3. Enter: Save the trimap
  4. Esc: Revert all the changes
- The trimap gets saved in `./resources/output_dir` with the prefix `trimap_`

### Note:
- Large image files may add some delay in mouse pointer movement while masking.