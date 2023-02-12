from rembg import remove
from PIL import Image
input_path= 'mahir.jpg'
output_path='mahir.jpg'
inp=Image.open(input_path)
output=remove(inp)
output.save(output_path)
#thmahir