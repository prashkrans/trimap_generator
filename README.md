# Trimap Generator
Allows a user to paint a trimap for the input image

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
  1. Q: White Mask  
  2. E: Grey Mask
  3. Enter: Save the trimap
  4. Esc: Revert all the changes
- The trimap gets saved in `./resources/output_dir` with the prefix `trimap_`

### Note:
- Large image files may add some delay in mouse pointer movement while masking.