import os, json
from PIL import Image

config = json.load(open('config.json'))
directory_list = config["directory_list"]
delete_original = config["delete_original"]

for directory in directory_list:
    webp_images = [filename for filename in os.listdir(directory) if filename.endswith('webp')]

    for  webp_image in webp_images:
        filename_in = directory + "/" + webp_image
        filename_out = directory + "/" + webp_image.replace("webp","jpg")
        img = Image.open(filename_in).convert("RGB")
        img.save(filename_out,"jpeg")
        
        if(delete_original):
            os.remove(filename_in)