import os, sys
from PIL import Image
import pillow_heif

# object to allow for more control on save path
if len(sys.argv) > 1:
    save_dir_name = sys.argv[1]  
else:
    save_dir_name = 'heic_img'

# output image file extension to save converted image as
if len(sys.argv) > 2:
    file_ext_str = str(sys.argv[2])
    file_ext_list = [d for d in file_ext_str]
    if "." not in file_ext_str:
        file_ext = file_ext_str
    else:
        dot_idx = file_ext_str.find(".")
        file_ext_list.pop(dot_idx)
        file_ext = "".join(file_ext_list)
else:
    file_ext = 'png'

# set the directory path containing the HEIC files
# first, get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

#then, append current_dir to save folder name 
save_dir = os.path.join(current_dir, save_dir_name)

# create save directory if it does not exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# loop through all files in the directory
for filename in os.listdir(current_dir):
     # check if the file is in HEIC format
    if filename.lower().endswith(".heic"):
        # create an Image object from the HEIC file
        filepath = os.path.join(current_dir, filename)
        print("Converting:", filepath)
        heif_file = pillow_heif.read_heif(filepath)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        # create a new filename for the PNG file
        new_filename = os.path.splitext(filename)[0] + "."+file_ext
        new_filepath = os.path.join(save_dir, new_filename)

        image.save(new_filepath, format(file_ext))


