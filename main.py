from rembg import remove
from PIL import Image
input_path = 'IMG_2497.tiff'
output_path = 'varya1.tiff'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)